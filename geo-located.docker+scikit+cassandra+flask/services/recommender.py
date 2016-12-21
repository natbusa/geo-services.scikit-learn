# cassandra driver
from cassandra.cluster import Cluster
from cassandra.cluster import SimpleStatement, ConsistencyLevel

# serialize/deserialize models
import pickle

# augment data
import urllib, urllib.request
import json

# connect to cassandra
CASSANDRA_NODES = ['127.0.0.1']

cluster = Cluster(CASSANDRA_NODES)
session = cluster.connect()

cql_stmt = "SELECT model from lbsn.models where mid='kmeans'"
rows = session.execute(cql_stmt)
ml = pickle.loads(rows[0].model)

# prepared statement for getting the name of the top venue in a given cluster
cql_prepared = session.prepare("SELECT * from lbsn.kmeans_topvenues where cid= ? LIMIT ?")

def geturl(s):
    s=urllib.parse.quote(s)
    wiki_url = ''
    try:
        url='https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&format=json'.format(s)
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        wiki_url = json.loads(resp.read().decode('utf-8'))[3][0]
    finally:
        return wiki_url

def score(lon, lat):
    cl = ml.predict([[lon, lat]])[0]
    
    keys = cluster.metadata.keyspaces['lbsn'].tables['kmeans_topvenues'].columns.keys()
    rows = session.execute(cql_prepared.bind((cl,1)))
    
    #package result as a dictionary
    d = dict(zip(keys,list(rows[0])))
    
    if d['url'] == None:
        #get the url from wikipedia
        d['url']  = geturl(d['name'])
        
        #cache
        cql_stmt = "UPDATE lbsn.kmeans_topvenues SET url = '{}' WHERE cid = {}".format(d['url'], d['cid'])
        rows = session.execute(cql_stmt)

    return d

def html_template(d):
    def link(url, text):
        return '<a href="{}">{}</a>'.format(url, text) if url else text
    
    # url to html tags
    d['url_html'] = link(d['url'], d['name'])
    
    # template!
    tmpl = 'What about visiting the {url_html}?'
    
    #render
    output = tmpl.format(**d)
    
    return output

def recommender(lon,lat, format='json', notebook=False):
    d = score(lon, lat)
    
    name = d['name']
    url  = d['url']
    
    # optionally add extra data suggestion 
    # based on the information available
    output = html_template(d) if format=='html'else json.dumps(d)
    
    if notebook:
        from IPython.display import HTML
        return HTML(output)
    else:
        return output

from flask import Flask
app = Flask("venue_recommender")

@app.route("/venues/recommender/<lon>,<lat>")
def recommender_api(lon, lat):
        return recommender(float(lon), float(lat))
    
app.run(debug=1)