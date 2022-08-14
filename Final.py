# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:53:27 2022

@author: jense
"""

import pandas as pd

YT = pd.read_csv("yellow_tripdata_2022-04.csv")

YT

YT = YT

YT.columns

YT['VendorID']

YT[2:10]

YT.dtypes

YT['tpep_pickup_datetime'].dtypes

YT.head()
YT.tail()

YT['tpep_pickup_datetime'].head()

YT[['total_amount','passenger_count']].head()

YT[['total_amount','passenger_count']].head(10)

YT.describe()

YT['trip_distance'].describe()


YT['trip_distance'].describe().apply("{0:.2f}".format)

pd.set_option('display.float_format', lambda x: '%.5f' % x)

YT[['trip_distance','fare_amount']].describe()

YT.memory_usage(index=False)

YT[['total_amount','VendorID']].dtypes

YT[['total_amount','VendorID']].astype('category').memory_usage(deep=True)

YT[['tpep_pickup_datetime','tpep_dropoff_datetime']].dtypes

YT['tpep_pickup_datetime'].head()

YT['pickup'] = pd.to_datetime(YT['tpep_pickup_datetime'],
                              infer_datetime_format=True)

YT['pickup'].head()

del YT['tpep_pickup_datetime']

YT['dropoff'] = pd.to_datetime(YT['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del YT['tpep_dropoff_datetime']

YT['duration'] = YT['dropoff'] - YT['pickup']

YT[['pickup','dropoff','duration']].head()

YT['trip_distance'].describe()

YT['valid'] = YT['trip_distance'] <= 100

YT['invalid'] = YT['trip_distance'] == 0

YT['invalid'] = YT['passenger_count'] == 0

YT['valid'] = YT['total_amount'] > 0

YT['valid'] = YT['total_amount'] < 1000

YT['valid'] = YT['extra'] >= 0

YT[['trip_distance','valid']].head()

YT['trip_distance'].describe()

YT = YT[YT.valid == True]

YT['trip_distance'].describe()

YT.to_csv('Yellow_Saved.csv', index = False)



import pandas as pd

YT = pd.read_csv("Yellow_Saved.csv")

YT

YT.columns

YT.dtypes

YT['pickup'] = pd.to_datetime(YT['pickup'],
                              infer_datetime_format=True)


YT['dropoff'] = pd.to_datetime(YT['dropoff'],
                              infer_datetime_format=True)

YT['duration'] = pd.to_datetime(YT['duration'],
                              infer_datetime_format=True)


YT[['pickup','dropoff','duration']].head()

# Let's look for other problematic values

YT.describe()

YT.columns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

YT['passenger_count'].describe()

YT['trip_distance'].describe()

YT['fare_amount'].describe()

YT['extra'].describe()

YT['mta_tax'].describe()

YT['tolls_amount'].describe()

YT['improvement_surcharge'].describe()

YT['total_amount'].describe()


import pandas as pd
import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt



figs,subs = plt.subplots(2,sharex=True, sharey=True)
YT1 = YT[YT.passenger_count == 1]
subs[0].scatter(YT1['fare_amount'],YT1['trip_distance'],
            color='red',marker='^',label='1')
YT2 = YT[YT.passenger_count == 2]
subs[1].scatter(YT2['fare_amount'],YT2['trip_distance'],
            color='blue',marker='^',label='2')
plt.xlabel('fare_amount')
plt.ylabel('trip_distance')
plt.axis([-5,300,-1,60])
plt.title('Fare vs Distance by Passenger Count')
plt.figlegend(
    labels=('1 Passenger', '2 Passengers'),
    loc='upper right')
plt.show()