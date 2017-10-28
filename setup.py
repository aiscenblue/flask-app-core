from distutils.core import setup
from flask_app_core import __version__

setup(
    name='flask-app-core',
    version=__version__,
    description='Flask app core',
    author='Jeffrey Marvin Forones',
    author_email='aiscenblue@gmail.com',
    url='https://github.com/aiscenblue/flask-app-core',
    packages=['flask_app_core'],
    keywords=['flask', 'clask_app_core'],  # arbitrary keywords
    install_requires=['flask', 'flask-app-core', 'flask-application', 'flask-app-builder'],
    entry_points=None
)
