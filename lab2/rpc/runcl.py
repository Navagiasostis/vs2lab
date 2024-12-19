import rpc
import logging
import time

from context import lab_logging

lab_logging.setup(stream_level=logging.INFO)

cl = rpc.Client()
cl.run()

def callback(data):
  print("ResultCallback: {}".format(data.value))


base_list = rpc.DBList({'yee'})
cl.append('haw', base_list, callback)

while cl.response is None:
  print("doing other stuff...")
  time.sleep(1)


cl.stop()
