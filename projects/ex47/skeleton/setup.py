try:
    from setuptools import setup
except ImportError :
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'My Name',
    'url' : 'URL to get it at',
    'download_url' : 'Where to download it',
    'author_email' : 'my Email',
    'version' : '1.0',
    'install_requires' : ['nose'],
    'packages' : ['WWW'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)