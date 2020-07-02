#!/usr/bin/env python

import json
from jade import app, jadedb

@app.route("/api/v1/pages/", methods=['GET'])
def get_all_pages():
  try:
    # Get all object data
    results = jadedb.fetchall_json("SELECT * FROM public.pages ORDER BY pid ASC")

    if results is None:
      data = []
    else:
      data = results

    resp = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return resp

  except Exception as e:
    return str(e), 500


@app.route("/api/v1/pages/<string:slug>", methods=['GET'])
def get_page_by_slug(slug):
  try:
    if slug == 'home' or slug == 'index':
        results = jadedb.fetchone_json("SELECT * FROM public.pages WHERE slug = '/'")
    else:
      results = jadedb.fetchone_json("SELECT * FROM public.pages WHERE slug = %s", ('/' + slug,))

    if results is None:
      data = []
    else:
      data = results

    resp = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return resp

  except Exception as e:
    return str(e), 500

@app.route("/api/v1/pages/<string:slug>/content", methods=['GET'])
def get_page_content(slug):
  try:
    # Get all object data

    if slug == 'index': 
      slug = '/' 
    else:
      slug = '/' + slug

    result = jadedb.fetchone("SELECT data FROM public.content WHERE slug = %s", (slug,))
    
    if result is None:
      data = '<p>No content assigned</p>'
    else:
      data = result['data']
          
    resp = app.response_class(
        response=data,
        status=200,
        mimetype='text/html'
    )    
    return resp

  except Exception as e:
    return str(e), 500

@app.route("/api/v1/main-menu/", methods=['GET'])
def get_main_menu():
  try:
    # Get all object data
    results = jadedb.fetchall_json("SELECT * FROM public.pages WHERE is_nav = true ORDER BY pid ASC")

    if results is None:
      data = []
    else:
      data = results
          
    resp = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return resp

  except Exception as e:
    return str(e), 500
