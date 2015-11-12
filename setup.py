from setuptools import setup

setup(name='FlaskApp',
      version='1.0',
      description='A tool to import liked links from Twitter to Readability.',
      author='Deepanshu Mehndiratta',
      author_email='contact@deepanshumehndiratta.com',
      url='http://www.python.org/sigs/distutils-sig/',
     install_requires=['Flask>=0.10.1', 'flask-mail', 'readability-api', 'python-twitter'],

     )
