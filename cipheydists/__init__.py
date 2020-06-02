import json
import os
import pkgutil

def get_dist(name):
  return json.loads(pkgutil.get_data(__name__, os.path.join("dist", name) + ".json"))

def get_charset(name):
  return json.loads(pkgutil.get_data(__name__, os.path.join("charset", name) + ".json"))
