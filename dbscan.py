import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
lat = np.array([22.45, 29.45, 36.567])
lon = np.array([73.345, 75.34, 95.567])
minimum_samples = 2            
minimum_dist = 2 / 6371.0088 #distance in KM / 6371.0088
X=np.column_stack([np.radian(lat),np.radians(lon)])
db = DBSCAN(eps=minimum_dist, min_samples=minimum_samples, algorithm = 'ball_tree', metric='haversine').fit(X)
db.labels_


#This code was in a Tableau workbookto find hot spots in a geography
