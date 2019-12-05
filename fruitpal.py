# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:15:16 2019

@author: satrajit
"""
import sys
import getopt
import json

from fruitpal_helper import dataClient
from app_client import fruitAPIClient

def generateResultFromAPI(commodity, price, quantity):
    """
    Function Description    : Generate result using API
    Parameters              : commodity <string>
                              price [Price Per Ton] <float>
                              quantity [In Tonnes] <float>
    """
    try:
        ac = fruitAPIClient()
        data = ac.getDataFromAPI(commodity)
        output = []
        for item in data:
            overhead = item[1]
            finalPrice = price + overhead
            #totalPrice = round(quantity*finalPrice, 2)
            totalPrice = "{:.2f}".format(quantity*finalPrice)
            ans = "{ct} {p}".format(ct=item[0], p=totalPrice)
            output.append(ans)        
        return output
    except Exception as e:
        print("Failed generating result. Exception:{0}".format(e))
        return None

def generateResult(commodity, price, quantity):
    """
    Function Description    : Generate result using library function
    Parameters              : commodity <string>
                              price [Price Per Ton] <float>
                              quantity [In Tonnes] <float>
    """
    try:
        dc = dataClient()
        data = dc.getData(commodity)
        output = []
        for item in data:
            overhead = item[1]
            finalPrice = price + overhead
            totalPrice = round(quantity*finalPrice, 2)
            output.append((item[0],totalPrice))
        output.sort(key = lambda x: x[1], reverse=True )        
        return output
    except Exception as e:
        print("Failed generating result. Exception:{0}".format(e))
        return None

def generateResultNew(commodity, price, quantity):
    """
    Function Description    : Generate result using library function
    Parameters              : commodity <string>
                              price [Price Per Ton] <float>
                              quantity [In Tonnes] <float>
    """
    try:
        dc = dataClient()
        data = dc.getDataForAPI(commodity)
        output = []
        for item in data['DATA']:
            overhead = float(item['VARIABLE_OVERHEAD'])
            finalPrice = price + overhead
            totalPrice = round(quantity*finalPrice, 2)
            res={}
            res['COUNTRY'] = item['COUNTRY']
            res['TOTALPRICE'] = totalPrice 
            output.append(res)        
        output.sort(key = lambda x: x['TOTALPRICE'], reverse=True )
        return output
    except Exception as e:
        print("Failed generating result. Exception:{0}".format(e))
        return None

def main(argv):
    """
    Main function to drive the call to fruitpal.py
    """
    if len(argv) < 4:
        print("Error: Requires 3 arguments, COMMODITY, PRICE, QUANTITY ")
        sys.exit(1)
    commodity = argv[1]
    price = float(argv[2])
    quantity = float(argv[3])
    res = generateResultNew(commodity, price, quantity)
    #res = generateResultFromAPI(commodity, price, quantity)

    if res and len(res) > 0:
        for item in res:
            totalPrice = "{:.2f}".format(item['TOTALPRICE'])
            ans = "{ct} {p}".format(ct=item['COUNTRY'], p=totalPrice)
            print(ans)
    
    
if __name__=='__main__':
    
    main(sys.argv)