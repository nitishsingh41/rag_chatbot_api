import os


# Set environment variables
os.environ['CMAKE_ARGS'] = "-DLLAMA_CUBLAS=on"
os.environ['FORCE_CMAKE'] = "1"

# Run pip install for requirements.txt
os.system("pip install -r requirements.txt")
