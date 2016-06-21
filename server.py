#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from scripts import spread_list, spread_edit, spread_getRow

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__,template_folder="./templates",static_folder='./static')

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<secret>'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
 
    cels=spread_list.list("")

    return  render_template('LIST.html', list_cels=cels['cel_list'],titles=cels['titles'])

    
@app.route('/ROW', methods=['POST','GET'])
def ROW():   
    
    if request.method == 'POST':
    
        row =request.form['updated']
        print 'ROW', row
        results = spread_getRow.get_row(row)
        print results[2]
        return render_template('EDIT.html', list_cels= results[0], titles = results[1], row=results[2])
    
    elif request.method == 'GET':
        
        print 'EDIT'
        row_in = request.args['ROW']
        print row_in
        data =request.args
        row_out = spread_edit.edit_spread(data, row_in)
        results = spread_getRow.get_row(row_out)
        
        return render_template('EDIT.html', list_cels= results[0], titles = results[1], row=results[2])


@app.route('/EDIT', methods=['GET'])
def EDIT():   
    
    print 'EDIT'
    row_in = request.args['ROW']
    print row_in
    data =request.args
    row_out = spread_edit.edit_spread(data, row_in)
    results = spread_getRow.get_row(row_out)
        
    return render_template('EDIT.html', list_cels= results[0], titles = results[1], row=results[2])

@app.route('/LIST_SEARCH', methods=['POST'])
def LIST_SEARCH():   
    print 'LIST_SEARCH'
    key_search =request.form['search']
     
    cels=spread_list.list(key_search)
    #print site_list
    return  render_template('LIST.html', list_cels=cels['cel_list'],titles=cels['titles'])
# # Run the app :)
if __name__ == '__main__':
  app.run( 
        host="localhost",
        port=int("5000")
  )
app.debug = True
