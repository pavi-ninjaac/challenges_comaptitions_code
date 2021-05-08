import datetime
import pytz
"""format = '%d-%m-%Y-%H:%M:%S'
date_time = "7-5-2021-22:40:0" #convert ot the utc time

timezone = pytz.timezone('UTC')
t = datetime.datetime.strptime(date_time, format)
utc_time = timezone.localize(t ,is_dst=None)
print(utc_time.tzinfo)
utc_timestamp = utc_time.astimezone(pytz.utc)
print(utc_timestamp.tzinfo)
print(utc_time == utc_timestamp)
utc_timestamp = round(utc_timestamp.timestamp() * 1000) 
print(utc_timestamp)"""

def getUtcTimestamp(t):
    """ Converting the given time to UTC timzone time"""
    timezone = 'UTC'
    format = '%d-%m-%Y-%H:%M:%S'
    timezone = pytz.timezone(timezone)
    date_time = datetime.datetime.strptime(t, format)
    utc_time = timezone.localize(date_time)# chenge the given time to the timezone spedified
    utc_timestamp = round(utc_time.timestamp() * 1000)
    return utc_timestamp
def getUtcTime(t):
    timezone = 'UTC'
    local = pytz.timezone(timezone)
    format = '%d-%m-%Y-%H:%M:%S'
    timestamp = datetime.datetime.strptime(t, format)
    utc_time = local.localize(timestamp, is_dst=None)
    utc_timestamp = utc_time.astimezone(pytz.utc)
    utc_timestamp = utc_timestamp.timestamp() * 1000 #why
    utc_timestamp = round(utc_timestamp)
    return utc_timestamp
timezone = 'UTC'
print(getUtcTimestamp("7-5-2021-22:40:0"))
print(getUtcTime("7-5-2021-22:40:0"))

# In[2]
def get_values_omnyk(parameter,tenantId, userId, now, one_day):
    """
    retrieves omnytraq data from the database
    parameter: str, a feature of omnytraq ie heartRate/spo2 value
    tenantId: str
    ringId: str
    now: time in milliseconds
    one_day: time in milliseconds

    """
    url = "http://34.208.125.165:8004/api/v1/datapoints/query"
    # payload = {"metrics":[{"tags":{"ringId":[ringId]},
    #                        "name": parameter + "-" + tenantId ,#"heartRate-OMNYK_US",
    #                        "aggregators":[{"name":"avg",
    #                                        "sampling":{"value":"1","unit":"seconds"}
    #                                        }]
    #                        }],
    #            "plugins":[],
    #            "cache_time":0,
    #            "start_absolute": one_day ,#1606513500000,
    #            "end_absolute": now #1606602883962
    #            }
    payload = {"metrics": [{"tags": {"userId": [userId]},
                            "name": parameter + "-" + tenantId,  # "heartRate-OMNYK_US",
                            "aggregators": [{"name": "avg",
                                             "sampling": {"value": "1", "unit": "seconds"}
                                             }]
                            }],
               "plugins": [],
               "cache_time": 0,
               "start_absolute": one_day,  # 1606513500000,
               "end_absolute": now  # 1606602883962
               }
    payload = json.dumps(payload) #json object --> string
    http = urllib3.PoolManager()
    response = http.request('POST', url, body=payload)
    if response.status != 200:# or response.status != 404:
       return
    return json.loads(response.data.decode('utf-8'))

hr_data_omnyk = get_values_omnyk("heartRate", tenantId, userId, now, one_day)

# In[3]
import pandas as pd
df = pd.DataFrame()
print(len(df))
# %%
