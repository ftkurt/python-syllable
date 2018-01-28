# coding=utf-8

from setuptools import setup

with open('requirements.txt') as infile:
    dependencies = [line.strip() for line in infile if len(line) > 0]

setup(name='syllable',
      version='0.0.1',
      description='Syllable encoding for words in Turkish',
      url='https://github.com/ftkurt/python-syllable',
      author='Fatih Kurt',
      author_email='ftkurt@gmail.com',
      license='MIT',
      packages=['vectors'],
      package_data={'': ['*.vec']},
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'hypothesis'],
      install_requires=dependencies,
      zip_safe=False)
