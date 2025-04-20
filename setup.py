from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='decorator_logger',
  version='1.0.3',
  author='argentumx',
  author_email='example@gmail.com',
  description='Simple decorator-logger',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/ArgentumX/decorator-logger-library',
  packages=find_packages(),
  install_requires=['loguru>=0.7.3'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License'
  ],
  keywords='aop logger decorator',
  project_urls={
    'GitHub': 'https://github.com/ArgentumX/'
  },
  python_requires='>=3.6'
)
