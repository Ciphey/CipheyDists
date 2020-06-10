import json
import os
import pkgutil
import sys

def check_name(name: str):
  return '/' not in name and '\\' not in name

def get_dist(name: str):
  if check_name(name):
    return json.loads(pkgutil.get_data(__name__, os.path.join("dist", name) + ".json"))

def get_charset(name: str):
  if check_name(name):
    return json.loads(pkgutil.get_data(__name__, os.path.join("charset", name) + ".json"))

def get_list(name: str):
  if check_name(name):
    return json.loads(pkgutil.get_data(__name__, os.path.join("list", name) + ".json"))

def get_model(name: str):
  if check_name(name):
    # The code for this was taken from the pkgutil docs
    d = os.path.dirname(sys.modules[__name__].__file__)
    return os.path.join(d, "model", name + ".h5")
