import json
from jade import app, jadedb

@app.route("/api/v1/objects/", methods=['GET'])
def get_object_types():
  try:
    all_object_types = []

    # Get all object types
    objects = jadedb.fetchall("SELECT * from pg_tables WHERE schemaname='objects'")

    for object_name in objects:
      object_data = {'name': object_name[1]}
      all_object_types.append(object_data)

    resp = app.response_class(
        response=json.dumps(all_object_types),
        status=200,
        mimetype='application/json'
    )
    
    return resp, 200

  except Exception as e:
    return str(e), 500

@app.route("/api/v1/objects/<string:object_type>", methods=['GET'])
def get_object_type_data(object_type):
  try:
    all_object_data = []

    # Get all object data
    results = jadedb.fetchall_json("SELECT * FROM objects.{object_type}".format(object_type=object_type))
    
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