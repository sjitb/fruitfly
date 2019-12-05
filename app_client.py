# -*- coding: utf-8 -*-
"""
Created on Mon Dec 02 22:38:52 2019

@author: satrajit
"""
import sys
import requests
import json

class fruitAPIClient(object):
    """
    Description    : Client implementation for REST API
    
    """
    def __init__(self):
        super().__init__()
        self.apiBaseURL = 'http://127.0.0.1:5000/api'
        #self.headers = headers

    def getDataFromAPI(self,commodity):
        """
        Function Description    : Function to get data for commodity.
        Parameters              : commodity <string>
        Return Value            : List of tuples of type [(COUNTRY, VARIABLE_OVERHEAD)]
        """
        try:
            requestURL = self.apiBaseURL + "/"+ "overhead" + "/" + commodity 
            respone = requests.request("Get", requestURL) #, headers=self.headers)
            if respone.status_code != 200:
                print("Failed to get data using API")
                return ""
            data = json.loads(respone.text)
            res = []
            for item in data['DATA']:
                res.append((item['COUNTRY'],float(item['VARIABLE_OVERHEAD'])))
            
            return res
        except Exception as e:
            print("Failed getting data for commodity. Exception:{0}".format(e))
            sys.exit(1)    