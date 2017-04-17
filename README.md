## Geo-Located Data
Extracting Patterns from Mobile Data using Scikit-Learn and Cassandra

Learn how to extract patterns and detect anomalies within geo-located data, using machine learning clustering algorithms. In this tutorial, you’ll prototype a venue recommender and a geo-fencing alerting engine, using geo-located data and machine learning clustering algorithms, practicing the skills you need to build your own geo-located data applications.

You’ll see how geographical analyses enable a wide range of services, from location-based recommenders to advanced security systems, and you’ll learn how to package data-driven applications based on geographical data and expose these insights as (micro) services.

### Important
Make sure you are not running other applications, when running this tutorial.

In particular,
make sure that ports **8888** and **5000** are free,   
and no other application or local jupyter installs is running on that port.

On Linux and Mac,  
If you want to find and kill the process (please do this *after* saving your work)  
`lsof -i4TCP:8888`, and `lsof -i4TCP:5000`, if the port is kept by another process, then the PID (process id) number to `kill` is the second field from the provided `lsof` command.

On Windows, please check the following url:  http://stackoverflow.com/questions/48198

### Download
Download the zip file or clone using git.

### Setup
From a terminal, move into the download directory, and run:  

``` 
cd tutorial; 
docker-compose build
docker-compose up -d 
```

### Requirements
This tutorial requires Docker 1.12+
https://www.docker.com/products/overview

### Run the tutorial
Most of this tutorial will be run straight from the browser, try this link [http://localhost:8888](http://localhost:8888)

During the tutorial, we will also do some direct inspection of the data using the Cassandra cqlsh CLI.
In order to run `cqlsh`, you have to execute it as an attached process on the already running container as follows:

`docker exec -it tutorial_cassandra_1 cqlsh`

### What you’ll learn—and how you can apply it

By the end of this live, hands-on, online course, you’ll understand:

- Machine learning “K-Means” and “DBSCAN” clustering techniques
- How to cluster geo-located data
- How to detect patterns and anomalies
- How to use Cassandra as a datastore for events and models


### And you’ll be able to:

- Use Scikit-Learn for preparing and clustering geo-located data
- Prototype a basic venue recommender
- Prototype a basic geo-fencing alerting engine
- Load and extract geo-located data and models in Cassandra
- Build a data-driven microservice in Python
