#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Name    : get_service.py
# Author            : jordi codina
# Created            : 20/06/2016
# Last Modified    : 20/06/2016
# Version            : 1.0.0

# License     :  MIT 

# Description        : return one instance of service whit spreadsheet scope oauth2client authorized 

import os
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials



def get_service():
    
    spreadsheetId = "1KgohInVdjEUiV6FzrgTWMi-gZtOmiVfEblNUvSNUkAA"
    
    scopes = 'https://www.googleapis.com/auth/spreadsheets'
    credentials_in = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join('./scripts', 'client_secret.json'), scopes=scopes) # 
    service = discovery.build('sheets', 'v4', credentials=credentials_in)

   
    print(service.__str__())
    
    print('end get services')
    return  service, spreadsheetId


    


if __name__ == '__main__':
    
    get_service()
