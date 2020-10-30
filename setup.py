from setuptools import setup
#https://docs.python.org/2/distutils/setupscript.html
#Info on including data files

setup(name="pinterest_scraper",version='0.2',description='Automatically find \
      and download images from Pinterest boards.',
      author='Xiaojian Deng',author_email="xjd001@gmail.com",license='MIT',\
      maintainer='Thomas Gorence',maintainer_email="thomas@thomas.codes",\
      packages=['pinterest_scraper'],
      url="https://github.com/ThomasDotCodes/pinterest-image-scraper",zip_safe=False)