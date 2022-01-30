# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:00:08 2020

@author: BMM2KOR
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:15:26 2020

@author: BMM2KOR
"""
import json
import requests
import ssl
import pandas as pd
from pandas.io.json import json_normalize
from pandas import ExcelWriter
from collections import OrderedDict
import xlsxwriter
#writer=ExcelWriter('C:\\Required_documents\\New_folder\\test_updated.xlsx',engine ='xlsxwriter')
class API_Response:
    def __init__(self,username,key,url):
        self.req={
                   "group": "licenses",
                   "action": "list_licenses",
                   "data": {
                           "username": username,
                           "key": key
                                  #"scan_code": scan_code
                           }

                   }
                
             #self.req=open('./response/request.txt','r')
             #req=json.loads(self.req.read())
        context=ssl.create_default_context()
        der_certs=context.get_ca_certs(binary_form=True)
        pem_certs=[ssl.DER_cert_to_PEM_cert(der) for der in der_certs]
             #print(pem_certs)
        with open('wincacerts.pem', 'w') as outfile:
            for pem in pem_certs:
                outfile.write(pem + '\n')
        response = requests.post(url,
                                  headers = {'Content-type': 'application/json'},
                                  data=json.dumps(self.req),verify='wincacerts.pem')
            # self.response = json.loads(response.decode("utf-8"))
        self.response=json.loads(response.text)
        res_dict= json.loads(response.text)
        x=res_dict["status"]
       # print(x)
        #workbook = xlsxwriter.Workbook('C:\\MYDrive\\update\\BOM_old\\data.xlsx')
       # worksheet = workbook.add_worksheet()
        writer=pd.ExcelWriter("C:\\MYDrive\\test_sources\\license_list.xlsx", engine ='xlsxwriter')
        if res_dict['status']=='1':
            if res_dict.get('data') is not False:
                res_dict.pop('operation')
                res_dict.pop('status')
                #print(response_data.response.pop('operation'))
                    
                for k,v in res_dict.items():
                  #  print(v)
                   # data=[]
                    y=pd.DataFrame.from_dict(v, orient='index')
                    #for a,b in v.items():
                       # y=pd.DataFrame.from_dict(b, index)
                    print(y)
                    y1=y.iloc[y.identifier.str.lower().argsort()]
                    y1.to_excel(writer, sheet_name ='sheet', index=False)
                writer.save()
                                
       # workbook.close()
                       #print(b["identifier"])
                       # License_id= b["identifier"]
                        #file = open('C:\\MYDrive\\update\\BOM_old\\sample.txt', 'w')
                       # file.write(b["identifier"])
                        
                        
                  
res = API_Response('hew1kor','0a4cdaaf','https://rb-fossid.de.bosch.com/CM/api.php')
        
        
#writer.save()