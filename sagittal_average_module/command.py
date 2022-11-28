import sys
from sagittal_average_module.sagittal_brain import *

def process():
    argumens = sys.argv
    file_input = None
    file_output = None
    if len(argumens) > 1:
        file_input = sys.argv[1]
    if len(argumens) > 2:
        file_output = sys.argv[2]
    return run_averages(file_input, file_output)


if __name__ == "__main__":
    process()