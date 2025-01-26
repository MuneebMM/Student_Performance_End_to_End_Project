from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    HYPHEN_E_Dot = '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_Dot in requirements:
            requirements.remove(HYPHEN_E_Dot)
    return requirements

    
setup(
    name="mlproject",
    version="0.0.1",
    author="Muneeb",
    author_email="muneebmm007@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),


)