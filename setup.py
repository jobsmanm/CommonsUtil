from setuptools import setup, find_packages

setup(name='CammonsUtils',
      version='1.0',
      url='https://github.com/jobsmanm/CommonsUtil',
      license='MIT',
      author='Jobsman Jr',
      author_email='jobsman_junior@sicredi.com.br',
      description='Projeto com funcoes uteis para o databricks',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=True)