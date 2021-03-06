# coding=utf-8

from setuptools import setup, find_packages

with open('requirements.txt') as infile:
    dependencies = [line.strip() for line in infile if len(line) > 0]

setup(name='syllable',
      version='0.0.1',
      description='Syllable encoding for words in Turkish',
      url='https://github.com/ftkurt/python-syllable',
      author='Fatih Kurt',
      author_email='ftkurt@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'syllable': ['vectors/tr']},
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'hypothesis'],
      install_requires=dependencies,
      zip_safe=False)
