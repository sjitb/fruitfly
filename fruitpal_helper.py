# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:33:12 2019

@author: satrajit
"""
import sys
import json

class dataClient(object):
    """
    Class to read Third Party JSON data
    """
    def __init__(self):
        super().__init__()
        self.filepath = 'third_party.json'

    def loadData(self):
        try:
            data = None
            with open(self.filepath) as json_file:
                data = json.load(json_file)
            json_file.close
            return data
        except Exception as e:
            print("Failed loading data from JSON. Exception:{0}".format(e))
            sys.exit(1)    

    def getData(self,commodity = None, country = None):
        """
        Function Description    : Function to get data for commodity.
        Parameters              : commodity <string>
        Return Value            : List of tuples of type [(COUNTRY, VARIABLE_OVERHEAD)]
        """
        try:
            data = self.loadData()
            ret = []
            for item in data:
                if item['COMMODITY'] == commodity:
                    if country and item['COUNTRY'] in country:
                        ret.append((item['COUNTRY'],float(item['VARIABLE_OVERHEAD'])))
                    if country is None:
                        ret.append((item['COUNTRY'],float(item['VARIABLE_OVERHEAD'])))
            return ret
        except Exception as e:
            print("Failed getting data for commodity. Exception:{0}".format(e))
            sys.exit(1)    
    
    def getDataForAPI(self, commodity = None):
        """
        Function Description    : Function to get data for commodity to generate API response.
        Parameters              : commodity <string>
        Return Value            : {'COMMODITY': 'mango', 
                                'DATA': [
                                    {'COUNTRY': 'MX', 'VARIABLE_OVERHEAD': '1.24'}, 
                                    {'COUNTRY': 'BR', 'VARIABLE_OVERHEAD': '1.42'}
                                    ]
                                }
        """
        try:
            data = self.loadData()
            ret = {'COMMODITY':"", 'DATA':[]}
            for item in data:
                if item['COMMODITY'] == commodity:
                    ret['COMMODITY'] = item['COMMODITY']
                    temp = {}
                    temp['COUNTRY'] = item['COUNTRY']
                    temp['VARIABLE_OVERHEAD'] = item['VARIABLE_OVERHEAD']
                    ret['DATA'].append(temp)
#                    if item['COMMODITY'] == ret['COMMODITY']:
#                        temp = {}
#                        temp['COUNTRY'] = item['COUNTRY']
#                        temp['VARIABLE_OVERHEAD'] = item['VARIABLE_OVERHEAD']
#                        ret['DATA'].append(temp)
#                    else:
#                        ret['COMMODITY'] = item['COMMODITY']
#                        temp = {}
#                        temp['COUNTRY'] = item['COUNTRY']
#                        temp['VARIABLE_OVERHEAD'] = item['VARIABLE_OVERHEAD']
                        #ret['DATA'].append(temp)
#                        ret['DATA']=[temp]
            if len(ret['DATA']) == 0:
                print("No Data Available for Commodity {0}".format(commodity))
                sys.exit(1)
            return ret
        except Exception as e:
            print("Failed getting data for commodity. Exception:{0}".format(e))
            sys.exit(1)
