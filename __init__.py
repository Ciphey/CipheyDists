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
    return pkgutil.get_data(__name__, os.path.join("model", name) + ".tflite")

def get_brandon(name: str):
  if check_name(name):
    return json.loads(pkgutil.get_data(__name__, os.path.join("brandon", name) + ".json"))

def get_translate(name: str):
  if check_name(name):
    return json.loads(pkgutil.get_data(__name__, os.path.join("translate", name) + ".json"))

