from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))
def readme():
    with open('README.md') as f:
        return f.read()
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
setup(
  include_package_data=True,
  name = 'spry',
  license='GNUv3',
  version = '0.1.9',
  description = 'Spry is a social media collector toolsuite',
  long_description = readme(),
  author = 'James Campbell',
  author_email = 'james@jamescampbell.us',
  url = 'https://github.com/jamesacampbell/spry', # use the URL to the github repo
  download_url = 'https://github.com/jamesacampbell/spry/tarball/0.1.9',

  keywords = ['social', 'collector', 'scraper'], # arbitrary keywords
  classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Programming Language :: Python',],
      packages=["spry", "spry.modules"],
    package_data={'spry': ['sociallist/sociallist.txt']},
  install_requires = ['requests>=1.0',],
    entry_points={
        'console_scripts': [ 'spry=spry:main',],
        },
)
