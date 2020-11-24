import os
from scripts import query_data
import shutil

query_data.write_data()
shutil.rmtree('scripts/__pycache__')
