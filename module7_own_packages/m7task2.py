from setuptools import setup

"""Add function that calls setup function to setup package

using arg_dict dictionary with following structure:
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
The function should contain the second  parameter 'requires' that should contain
install_requires parameters (dependencies that should be installed before module)

"""


def do_setup(args_dict, requires):
    setup(name=args_dict['name'], 
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires)
    