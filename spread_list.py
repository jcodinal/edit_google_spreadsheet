#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Name    : spread_list.py
# Author            : jordi codina
# Created            : 20/06/2016
# Last Modified    : 20/06/2016
# Version            : 1.0.0

# License     :  MIT 

# Description        : return a list of dictionries {row_title: cel content}
import re
import get_service 

def list(site_in):


    print('INIT_list')
    service_in = get_service.get_service()
    service = service_in[0]
    spreadsheetId = service_in[1]
    rangeName = 'A1:2000'# this range referred to the first sheet if you want to point a concrete one change it to sheet_name!A1:2000
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    
    values = result.get('values')
       
    titles = values[0]
    nrow = 0
    dictionary = {}
    dictionary_list = []
    
   
    if not values:
        print('No data found.')
        
    elif not site_in:
        nrow = 1
        for row in values[1:]:            
            nrow = nrow + 1            
            site = []
            dictionary = dict(zip(titles, row))
            site.append(nrow)
            site.append(dictionary)
            dictionary_list.append(site)   
       
    else :        
        for row in values:
            nrow = nrow + 1
            for s in row:                
                if re.findall(site_in, s):   
                    site = []
                    dictionary = dict(zip(titles, row))
                    site.append(nrow)
                    site.append(dictionary)
                    dictionary_list.append(site)
                
               
    print(len(dictionary_list))

    print('end_list')
    return  {'cel_list':dictionary_list, 'titles':titles}


    


if __name__ == '__main__':
    
     
    list("", get_service())
