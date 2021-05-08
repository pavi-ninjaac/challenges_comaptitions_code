import argparse
import datetime
import pytz
import urllib3
import json
import pandas as pd

def get_all_users():
    """
    Fetches data from database

    Args: No arguments specified
    return: Dataframe of all users
    """
    http = urllib3.PoolManager()
    url = 'https://ingest.omnytraq-api.com/omnytraqCloud/users'
    response = http.request('GET', url)
    return json.loads(response.data.decode('utf-8')) #sting --> json obejct

def getUtcTimestamp(t):
    """ Converting the given time to UTC timzone time"""
    format = '%d-%m-%Y-%H:%M:%S'
    timezone_place = pytz.timezone(timezone)
    date_time = datetime.datetime.strptime(t, format)
    utc_time = timezone_place.localize(date_time) #get the time on that timezone place
    utc_time = utc_time.astimezone(pytz.utc)
    utc_timestamp = round(utc_time.timestamp() * 1000) #microsec --> millisec
    return utc_timestamp 

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
    json_obj = json.loads(response.data.decode('utf-8'))

    #converting json to dataframe
    values = json_obj["queries"][0]["results"][0]["values"]
    columns = ["time",parameter]
    dataframe = pd.DataFrame(values,columns=columns)
    return dataframe

def get_values_comp(parameter,tenantId, userId, now, one_day):
    """
    retrieves comparative data from the database
    parameter: str, a feature of omnytraq ie heartRate/spo2 value
    tenantId: str
    ringId: str
    now: time in milliseconds
    one_day: time in milliseconds

    """
    url = "http://34.208.125.165:8004/api/v1/datapoints/query"
    # payload = {"metrics": [{"tags": {"ringId": [ringId]},
    #                         "name": parameter + "Comp-" + tenantId,  # "heartRate-OMNYK_US",
    #                         "aggregators": [{"name": "avg",
    #                                          "sampling": {"value": "1", "unit": "seconds"}
    #                                          }]
    #                         }],
    #            "plugins": [],
    #            "cache_time": 0,
    #            "start_absolute": one_day,  # 1606513500000,
    #            "end_absolute": now  # 1606602883962
    #            }

    payload = {"metrics": [{"tags": {"userId": [userId]},
                            "name": parameter + "Comp-" + tenantId,  # "heartRate-OMNYK_US",
                            "aggregators": [{"name": "avg",
                                             "sampling": {"value": "1", "unit": "seconds"}
                                             }]
                            }],
               "plugins": [],
               "cache_time": 0,
               "start_absolute": one_day,  # 1606513500000,
               "end_absolute": now  # 1606602883962
               }
    payload = json.dumps(payload)
    http = urllib3.PoolManager()
    response = http.request('POST', url, body=payload)

    if response.status != 200:  # or response.status != 404:
        return
    json_obj = json.loads(response.data.decode('utf-8'))

    #converting json to dataframe
    values = json_obj["queries"][0]["results"][0]["values"]
    columns = ["time",parameter]
    dataframe = pd.DataFrame(values,columns=columns)
    return dataframe

def main():
    strat_day , now = getUtcTimestamp(from_date) , getUtcTimestamp(to_date)
    users = get_all_users()
    from_email_id , password = 'analytics@omnyk.com' , 'Omnyk4you'
    
    for user in users:
        userId,firstName, emailId, tenantId = user["id"],user['firstName'], user['emailId'], user['tenantId']
        if tenantId is None:
            tenantId = 'OMNYK_US'
        if tenantId != 'JAYADEVA-001':
            continue
        ringIds = user['ringId']
        ringIdList = ringIds.split(",") #why

        if ringIdList[0] == '':
            continue #skiping the person who has no ring id
        
        hr_data_omnyk = get_values_omnyk("heartRate", tenantId, userId, now, strat_day)
        spo2_data_omnyk = get_values_omnyk("spo2", tenantId, userId, now, strat_day)
        hr_data_comp = get_values_comp("hearRate", tenantId, userId, now, strat_day)
        spo2_data_comp = get_values_comp("spo2", tenantId, userId, now, strat_day)
        print(hr_data_omnyk , spo2_data_omnyk,hr_data_comp ,spo2_data_comp)
        continue
        if len(hr_data_comp) <=0 or len(spo2_data_comp) <=0:
            print('skipping user')
            continue #no data in 24 hours
        print(hr_data_omnyk , spo2_data_omnyk,hr_data_comp ,spo2_data_comp)
        break



        


    

if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-fd" , dest="from_date" , required=False , help="Enter the From date" , action="store",default=None)
    parser.add_argument("-td", dest="to_date", required=False, help="Enter To Date", action="store", default=None)
    parser.add_argument("-tz", dest="time_zone", required=True, help="Enter Time Zone", default=None)
    parser.add_argument("-r", dest="quick_range", required=False, help="Enter Range")
    parser.add_argument("-s" , dest="sd_5_min" , required=True , help="Enter Stabdard deviation 5min Sample size",default=5)
    parser.add_argument("-p" , dest="sd_15_min" , help="Enter Stabdard deviation 15min Sample size" , default=15)
    args = parser.parse_args()
   
    sds_min, sdp_min , timezone= args.sd_5_min, args.sd_15_min , args.time_zone
    quick_range = args.quick_range 
    if quick_range == None:
        from_date , to_date = args.from_date , args.to_date
    else:
        format = '%d-%m-%Y-%H:%M:%S'
        if quick_range == 'today':
            date = datetime.datetime.now(pytz.timezone(timezone))
            from_date = date.date().strftime(format)
            to_date = date.strftime(format)
            
        elif quick_range == 'yesterday':
            date = datetime.datetime.now(pytz.timezone('UTC'))
            from_date = (date.date() - datetime.timedelta(days=1)).strftime(format)
            to_date = date.strftime(format)
            to_date = datetime.datetime.strptime(to_date, format)
            to_date = (to_date - datetime.timedelta(minutes=1)).strftime(format)
            
        else:
            print("Range can not be recognized :( :(")
            sys.exit()
    main()
    