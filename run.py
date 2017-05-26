# -*- coding: utf-8 -*-
import urllib
from datetime import datetime

start = datetime.now()

y = lambda x: (sum(x)/len(x),len(x))

myfile = urllib.URLopener()
myfile.retrieve('https://s3.amazonaws.com/carto-1000x/data/yellow_tripdata_2016-01.csv','yellow_tripdata_2016-01.csv')

with open('yellow_tripdata_2016-01.csv') as data:
    next(data)
    print("{0} (media,len)".format( y([float(line.split(',')[-4]) for line in data]) ))
    
end = datetime.now()
print((end - start).seconds," s.")
