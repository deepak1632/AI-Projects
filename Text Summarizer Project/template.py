import os
from pathlib import Path # A modern way to handle file system paths in an object-oriented manner. Easier and safer than using raw strings with os.
import logging # Python’s built-in module to log messages (info, warnings, errors) for tracking program execution.

# Logging setup
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [ 
     ".github/workflows/.gitkeep",
     f"src/{project_name}/__init__.py", # __init__.py is a special file in Python that is automatically executed when a package or module is imported. It is used to define the package’s initialization code.
     f"src/{project_name}/components__init__.py",
     f"src/{project_name}/utils__init__.py",
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