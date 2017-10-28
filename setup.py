from distutils.core import setup

# this grabs the requirements from requirements.txt
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='flask-app-core',
    version='1.0.0',
    description='Flask app core',
    author='Jeffrey Marvin Forones',
    author_email='aiscenblue@gmail.com',
    url='https://github.com/aiscenblue/flask-app-core',
    packages=['flask_app_core'],
    keywords=['flask', 'flask_blueprint'],  # arbitrary keywords
    install_requires=REQUIREMENTS,
    entry_points=None
)
