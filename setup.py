from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function return all the required packages as a list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[rep.replace("\n"," ") for rep in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="E2E ML Project",
    version="0.0.1",
    author="Jai Rahul",
    author_email="jrinifinity2806@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   #If 3 packages then-["numpy","pandas","seaborn"]
)