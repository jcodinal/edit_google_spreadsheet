#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Name    : spread_getRow.py
# Author            : jordi codina
# Created            : 20/06/2016
# Last Modified    : 20/06/2016
# Version            : 1.0.0

# License     :  MIT 

# Description        : get the row named in row_in parameter, return a dictionary {"column title": "cel_value" }, [titles row), row_in


import get_service 

def get_row(row_in):

    range_in = row_in + ':' + row_in
   
    print('INIT_getRow')

    service_in = get_service.get_service()
    service = service_in[0]
    spreadsheetId_in = service_in[1]

    row_titles = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId_in, majorDimension='ROWS', ranges=['1:1']).execute()
    
    row = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId_in, majorDimension='ROWS', ranges=[range_in]).execute()
    

    if row:
        
        dictionary = dict(zip(row_titles['valueRanges'][0]['values'][0], row['valueRanges'][0]['values'][0]))
        titles = row_titles['valueRanges'][0]['values'][0]
        print 'END_get_row'
    return dictionary, titles, row_in

if __name__ == '__main__':
    
    data = [  { "range": "25:25",
                "majorDimension": 'ROWS' },
            ]
    row = '25'
    service = get_service("")
    get_row(row, service)

