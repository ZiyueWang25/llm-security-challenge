import os
import datetime
import pytz
import pickle

def get_new_version():
  utc = pytz.utc
  dt = datetime.datetime.now()
  return utc.localize(dt).strftime("%Y%m%d-%H:%M")

def save_pkl(obj, save_path):
  dir = os.path.dirname(save_path)
  os.makedirs(dir, exist_ok=True)
  with open(save_path, 'wb') as f:
    pickle.dump(obj, f)

def load_pkl(save_path):
  with open(save_path, 'rb') as f:
    return pickle.load(f)
