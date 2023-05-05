
import sys
import pymongo
from pymongo import MongoClient
import pandas as pd
import csv
import os
from datetime import datetime ,timedelta
import time
import subfunction as sub


    
now=datetime.now()
startnow=datetime.combine(now,datetime.min.time())
endnow=startnow=datetime.combine(now,datetime.min.time())
Search={"Datetime":{'$gte':startnow,"$lte":endnow}}
data_2=sub.WIFI_FindData("AP","Controller4",Search)
print(data_2)