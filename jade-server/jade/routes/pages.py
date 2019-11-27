#!/usr/bin/env python

import json
from jade import app, jadedb

@app.route("/api/v1/pages/", methods=['GET'])
def get_all_pages():
  # Get all object data
  results = jadedb.fetchall_json("SELECT * FROM public.pages ORDER BY pid ASC")
  
  if results is None:
    data = []
  else:
    data = results

  response = app.response_class(
      response=json.dumps(data),
      status=200,
      mimetype='application/json'
  )
  return response


@app.route("/api/v1/pages/<string:slug>", methods=['GET'])
def get_page_by_slug(slug):
  if slug == 'home' or slug == 'index':
      results = jadedb.fetchone_json("SELECT * FROM public.pages WHERE slug = '/'")
  else:
    results = jadedb.fetchone_json("SELECT * FROM public.pages WHERE slug = %s", ('/' + slug,))

  if results is None:
    data = []
  else:
    data = results

  response = app.response_class(
      response=json.dumps(data),
      status=200,
      mimetype='application/json'
  )
  return response


@app.route("/api/v1/main-menu/", methods=['GET'])
def get_main_menu():
  # Get all object data
  results = jadedb.fetchall_json("SELECT * FROM public.pages WHERE is_nav = true ORDER BY pid ASC")
  
  if results is None:
    data = []
  else:
    data = results
        
  response = app.response_class(
      response=json.dumps(data),
      status=200,
      mimetype='application/json'
  )
  return response