from typing import List
from setuptools import setup, find_packages

def get_requirements(requirement:str)-> List[str]:
    """
    function to get the list of packages to install 
    from the the Requirement.txt file

    Return (List): Return a list of string containing the names
            of the packages to install 

    
    
    """
    try:
        require = []

        with open(requirement, 'r') as file_list:
            require_list =file_list.readlines()
            

            for req in require_list:
                package = req.strip()

                if package and package != '-e .':
                   require.append(package)

        return require

    except FileNotFoundError:
        print('File not found')



setup(
    name= 'Text summarizer',
    version = '0.0.1',
    author='Emmanuel Ajala',
    author_email='ajalae2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)