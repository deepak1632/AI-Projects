import os
from pathlib import Path # A modern way to handle file system paths in an object-oriented manner. Easier and safer than using raw strings with os.
import logging # Python’s built-in module to log messages (info, warnings, errors) for tracking program execution.

# Logging setup
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [ 
     ".github/workflows/.gitkeep",
     f"src/{project_name}/__init__.py", # __init__.py is a special file in Python that is automatically executed when a package or module is imported. It is used to define the package’s initialization code.
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/utils/__init__.py",
     f"src/{project_name}/utils/common.py",
     f"src/{project_name}/logging/__init__.py",
     f"src/{project_name}/config/confiuration.py",
     f"src/{project_name}/pipeline/__init__.py",
     f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/constants/__init__.py",
     "config/config.yaml",
     "params.yaml",
     "app.py",
     "main.py",
     "Dockerfile",
     "requirements.txt",
     "setup.py",
     "research/trails.ipynb" 
]

for filepath in list_of_files:
    filepath = Path(filepath) # Convert the string to a Path object 
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Create the directory if it doesn't exist
        logging.info(f"Creating Directory:{filedir} for the file {filename}")
        # exist_ok=True means that if the directory already exists, it won't raise an error and won't create a new directory.
     
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filename} is already exist")