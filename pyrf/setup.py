from setuptools import setup

setup(name='pyrf',
      version='0.1',
      description='Calculate radiative forcing from GHG emissions',
      url='https://github.com/gschivley/pyRF',
      author='Greg Schivley',
      author_email='greg.schivley@gmail.com',
      license='MIT',
      packages=['pyRF'],
      install_requires=[
          'numpy',
          'scipy',
          'pandas',
          'random'],
      zip_safe=False)