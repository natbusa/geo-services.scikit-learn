#!/bin/sh

filename=gowalla_venues.csv
if [ ! -f $filename ]; then
    wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/locrec/gowalla-dataset.zip
    unzip gowalla-dataset.zip
    perl -pe 's/POINT\((\-?\d+\.\d+)\s+(\-?\d+\.\d+)\)/$2\t$1/g' ./gowalla-dataset/spots.txt > $filename
    rm -rf gowalla-dataset gowalla-dataset.zip
fi

filename=gowalla_events.csv
if [ ! -f $filename ]; then
  wget https://snap.stanford.edu/data/loc-gowalla_totalCheckins.txt.gz
  gunzip -f loc-gowalla_totalCheckins.txt.gz
  sed -e 's/Z/+0000/' -e 's/T/ /' loc-gowalla_totalCheckins.txt > $filename
  rm loc-gowalla_totalCheckins.txt
fi

filename=gowalla_users.csv
if [ ! -f $filename ]; then
  wget https://snap.stanford.edu/data/loc-gowalla_edges.txt.gz
  gunzip -f loc-gowalla_edges.txt.gz
  mv loc-gowalla_edges.txt $filename
fi