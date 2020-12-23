# Circle Generator
Home for the Circle Generator repository. This repository is a series of Python3 scripts and functions that use the Pillow module to generate samples of magic or alchemic circles, as well as many other magic-circle like patterns. This is done by generating series of random numbers with pre-defined drawing patterns to generate new and unique images each generation.

There are more example images that can be viewed in the sources listed below.
    * 
    
There is also documentation if you would like to using the drawing components in your own projects. Please see the [Documentation](https://github.com/jzaunegger/ACG-Python/docs/README.md)

## Usage
To use the scripts I have developed you will need to complete several steps. First you will need to clone the repository, you can download it directly or clone it using git. After cloning the repository, navigate into the ACG-Python folder. Then create a virtual environment and activate it. Once activated you can install the dependencies and start generating images. Just remember to exit the virtual environment when you are done.


create and install the dependencies to a virtual environment. After cloning this repository, run the command:
```bash
    # Clone the repository
    git clone https://github.com/jzaunegger/ACG-Python
    cd ACG-Python
    
    # Create the virtual envivornment
    python3 -r venv /venv
    
    # Activate the virtual environment
    source venv/bin/activate
    
    # Install the dependencies from the requirements
    pip3 -r install requirements.txt
    
    # Deactivate the virtual environment
    deactivate
```

## Dependecies
* Pillow 
