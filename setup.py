from setuptools import find_packages, setup
from typing import List

# This will automatically find out all the packages that are available 
# in the entire ml application in the directory that we have actually created 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Mausham kumar',
    author_email='maushamkumarr26@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)