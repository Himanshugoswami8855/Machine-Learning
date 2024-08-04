from setuptools import find_packages,setup 
from typing import list 

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->list[str]:
    '''THIS FUNCTION WILL RETURN LIST OF REQUIREMENTS   '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readliness()
        requirements=[req.replace('\n',' ') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements




setup(
    name='MachineLearning',
    version='0.0.1',
    author='Himanshu Goswami',
    author_email='himg548@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)