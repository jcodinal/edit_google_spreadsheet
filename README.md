# edit_google_spreadsheet
a little  flask app to serach/list/edit google spreadsheet 
is neded a service account oauth2client  
it looks like:

{
  "type": "service_account",
  "project_id": "nnnnnn",
  "private_key_id": "xxxxxxxxxxxxxxxxxxxxxx",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMI.............
  "client_email": "mmmmmmm.com",
  "client_id": "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com"
}

by default the active sheet is the first sheet os the spread sheet is you want work over a particular sheet is neded to change the range 
to "sheet_name!A1:2000"
