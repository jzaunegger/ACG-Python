# Alchemical/Magic Circle Generator (ACG/MCG)
Home for the Magic Circle Generator repository. This repository is a series of Python3 scripts and functions that use the PyGraphics Module developed by John Zelle at Wartburg College. It allows you to generate samples of magic or alchemic circles. This is done by generating series of random numbers with pre-defined drawing patterns to generate new and unique images each generation. So far there are only several options that each layer can take, as well as different chances of each layer being drawn. As time goes on more color pallettes and layer designs will be added resulting in more complex and beautiful patterns. I also have plans to use Generative Adversarial Networks to develop new patterns by feeding in samples generated here. I think it could lead to some interesting results. 

If you would like to learn more about how this project works, please read the documentation file listed [here](https://github.com/jzaunegger).

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
