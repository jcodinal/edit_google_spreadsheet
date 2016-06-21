#!/usr/bin/env python
# -*- coding: utf-8 -*-


import get_service 
def edit_spread(cels, row):

    print 'INIT_EDIT'
    print row

    service_in = get_service.get_service()
    service = service_in[0]
    spreadsheetId_in = service_in[1]
    
    row_titles = service.spreadsheets().values().get(spreadsheetId=spreadsheetId_in, majorDimension='ROWS', valueRenderOption='FORMATTED_VALUE', range='1:1').execute()
    print row_titles
    
    ranges = str(row) + ':' + str(row)

    print ranges
    values = []
    
    for title in row_titles['values'][0]:

        value = []

        value.append(cels[title])
        values.append(value)

    data_in = [  { "range": ranges,
                  "majorDimension":"COLUMNS",
                  "values": values  },
            ]
    print data_in
    data_out = {
              "valueInputOption": "RAW",
             
              "data":data_in}
    
    result = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId_in, body=data_out).execute()
    list_update = []
    if result['responses']:
        
        for r in result['responses']:
            list_update.append(r['updatedRange'])
     
    print result      
    print('END EDIT')
    
    return row

if __name__ == '__main__':
    
    data_no = [  { "range": "2:3",
               "majorDimension":"COLUMNS",
                "values": [ ["A1a1a1a1a1a"], ["A1a1a1a1a1a"], ["A1a1a1a1a1a"]]  },
            ]
    data = {"PROVINCE": "BARCELONA", "OWNER": "VODAFONE", "U900_COORDINADO": "NO", "ACCION PTE ASP": "", "site": "0555455", "PLANI 07-05-16": "#N/A", "SUBPROYECTO": "ANE 2016", "AUTOSWAP_3G": "NO", "ESTADO": "", "GOG 07-05-16": "#N/A", "PRIORIDAD_REPLANTEO": "2. MAYOR", "SEG. DIARIO": "SEG2016", "pt": "345587", "PREV ENTREGA": "19/04/2016", "ACCION PTE ERICSSON": "", "D_EMPLAZAMIENTO": "SABADELL/CAN RULL", "ROW": "2", "Fecha comentario": "27/04/2016", "CONTADOR RECHAZOS": "A2", "Fecha ULTIMO RECHAZO": "Bingo!", "LTE_1800": "NO", "ultimo tme": "Bingo!", "ESTADO REPLANTEO ASP": "Bingo!", "OTRAS_ACTIVIDADES": "", "ESTADO REPLANTEO ANE": "01. PTE PLANIFICAR", "Semana replanteo": "Bingo!", "CONTADOR": "A2", "Week rechazo": "#VALUE!", "smartel": "Bingo!", "ASP REPLANTEO": "Bingo!", "TIPO_PLAN": "#N/A", "COMENTARIOS": "25/04/16 editado nuevo", "LTE_800": "NO", "COCs SITE": "201408003659 IMPLANTACI\u0420\u2014?N LTE1800 201407004186 IMPLANTACI\u0420\u2014?N TCU", "ACCION": "", "AUTOSWAP_2G": "NO", "EXPRESS": "", "U900_NO_COORDINADO": "SI (W08/15)", "coc": "", "SITE CODE_F": "0800042", "ESTADO CAP": "#N/A"}
    row = 2
    edit_spread(data, row)

