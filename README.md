# Sagittal Average

This is a package used to calculate and produce a file of the sagittal average in a brain sample. 

## Installation

```bash
pip install git+https://github.com/UCL-COMP0233-22-23/sagittal_average/
```

## Usage
    
Invoke the tool with `sagittal_average_run <path/to/csv/with/brain/sample>` or use it on your own library:

```python
from sagittal_average_module import sagittal_brain

sagittal_brain.run_averages(file_input, file_output)
```