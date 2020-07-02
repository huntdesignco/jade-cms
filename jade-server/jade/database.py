import psycopg2, psycopg2.extras, json

class JadeDB(object):

  def __init__(self, app):
    self.app = app
    self.connection = self.connect()

  def connect(self):
    try:
      self.conn = psycopg2.connect(host=self.app.config['DB_HOST'],
                             database=self.app.config['DB_NAME'],
                             user=self.app.config['DB_USER'],
                             password=self.app.config['DB_PASS'],
                             port=self.app.config['DB_PORT'],
                             sslmode=self.app.config['DB_SSL'],
                             connect_timeout=15)

      self.conn.autocommit = True

    except Exception as error:
      return error 

    finally:
      return self.conn

  def reconnect(self):
    del self.connection
    self.connection = self.connect()
  
  def getcursor(self):
    try:
      cur = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
      if cur is not None:
        return cur
      else:
        self.reconnect()
        return None

    except Exception as error:
      print(error)
      return None


  def fetchone(self, query, params=None):
    try:
      cur = self.getcursor()

      if cur is not None:
        cur.execute(query, params)

        result = cur.fetchone()
        cur.close()
        return result

      else:
        self.reconnect()
        return None

    except Exception as error:
      return error

    finally:
      if cur is not None:
        cur.close()
        del cur

  def fetchall(self, query, params=None):
    try:
      cur = self.getcursor()
      if cur is not None:
        cur.execute(query, params)
        return cur.fetchall()
      else:
        self.reconnect()
        return None

    except Exception as error:
      print(error)
      return None

    finally:
      if cur is not None:
        cur.close()
        del cur


  def fetchone_json(self, query, params=None):
    try:
      cur = self.getcursor()

      if cur is not None:
        cur.execute(query, params)
        result = cur.fetchone()

        jsonified = []

        if result is not None:
            
          temp = {}
          c = 0
          for col in cur.description:          
              temp.update({str(col[0]): result[c]})
              c = c+1
          jsonified.append(temp)

        cur.close()

        return jsonified

      else:
        self.reconnect()
        return None

    except Exception as error:
      return error

    finally:
      if cur is not None:
        cur.close()
        del cur

  def fetchall_json(self, query, params=None):
    try:
      cur = self.getcursor()

      if cur is not None:
        cur.execute(query, params)
        results = cur.fetchall()
        
        jsonified = []

        for x in results:
            temp = {}
            c = 0
            for col in cur.description:
                temp.update({str(col[0]): x[c]})
                c = c+1
            jsonified.append(temp)

        return jsonified

      else:
        self.reconnect()
        return None

    except Exception as error:
      print(error)
      return None

    finally:
      if cur is not None:
        cur.close()
        del cur
