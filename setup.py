from setuptools import setup, find_packages

#setup(name='CommonsUtils',
#      version='1.0',
#      url='https://github.com/jobsmanm/CommonsUtil',
#      license='MIT',
#      author='Jobsman Jr',
#      author_email='jobsman_junior@sicredi.com.br',
#      description='Projeto com funcoes uteis para o databricks',
#      packages=find_packages(exclude=['tests']),
#      long_description=open('README.md').read(),
#      zip_safe=True)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="CommonsUtils",
    version="1.0",
    author="Jobsman Jr",
    description="Projeto com funcoes uteis para o databricks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["CommonsUtils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
    dependency_links=['https://github.com/jobsmanm/CommonsUtil'],
    zip_safe=True
)