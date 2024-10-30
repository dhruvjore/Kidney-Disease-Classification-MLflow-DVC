import os
from pathlib import Path
import logging

# We would create a logging string here
# Whatever activity we would do we can see them over the log file

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(levelname)s: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "reasearch/trails.ipynb",
    "templates/index.html",
    "test.py"


]


for filepaths in list_of_files:
    filepaths = Path(filepaths)
    filedir,filename = os.path.split(filepaths)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file:{filename}")

    if(not os.path.exists(filepaths)) or (os.path.getsize(filepaths) == 0):
        with open(filepaths, 'w') as f:
            pass 
    else:
        logging.info(f"File: {filename} already exists")
