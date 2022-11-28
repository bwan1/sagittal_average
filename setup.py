from setuptools import setup, find_packages

setup(
    name="Sagittal Average",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'sagittal_average_run = sagittal_average_module.command:process'
        ]
    }
)