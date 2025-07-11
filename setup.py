from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_reuirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if(HYPEN_E_DOT in requirements):
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Ajay Soni',
    author_email='ajaypsoni1509@gmail.com',
    description='A End to End ml project',
    packages=find_packages(),
    install_requires=get_reuirements('requirements.txt'),
)