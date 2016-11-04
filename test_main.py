import flask_main
import arrow
from dateutil import tz
import bson

def test_insert_delete():

  flask_main.delete_database()
  flask_main.insert('2016-11-01', 'Test#1')
  memos = flask_main.get_memos()
  assert len(memos) == 1
  print(str(memos[0]['date'].isoformat()))
  assert str(memos[0]['date'].isoformat()) == '2016-11-01T00:00:00-07:00'
  print(memos)
  list = []
  list.append(memos[0]['_id'])
  flask_main.remove(list)
  memos = flask_main.get_memos()
  assert len(memos) == 0
  
  

