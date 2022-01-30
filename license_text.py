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
    
    def __init__(self,username,key,id1,url):
        
        self.req={
                   "group": "licenses",
                   "action": "get_information",
                   "data": {
                           "username": username,
                           "key": key,
                           "license_identifier":id1
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
       # x=res_dict["status"]
        #print(res_dict)
       # License_id= b["identifier"]
        count=0
        self.data={}
        if res_dict['status']=='1':
            if res_dict.get('data') is not False:
                res_dict.pop('operation')
                res_dict.pop('status')
                #print(response_data.response.pop('operation'))
              # writer=pd.ExcelWriter("C:\\MYDrive\\update\\BOM_old\\license_info.xlsx", engine ='xlsxwriter')  
                
                for k,v in res_dict.items():
                    data=[]
                    #print(v['name'])
                    if v["text"]!=None:
                       # name= data.append(v["name"])
                       print(v["name"])
                    else:
                        data.append(v['name'])
                    self.data=data
                   
           # print(count)
                        
                    
                        
        
file1 = pd.read_excel("C:\\MYDrive\\update\\BOM_old\\data1.xlsx", 'sheet', on_demand = True)

print(file1.get("identifier"))


                              
res = API_Response('hew1kor','277a63d9',,'https://rb-fossid.de.bosch.com/test/api.php')
  #  print(i)
    #print(file1.get("name"))
        
#writer.save()