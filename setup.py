from distutils.core import setup

setup(
    name='flask-app-core',
    version='1.3.1',
    description='Flask app core',
    author='Jeffrey Marvin Forones',
    author_email='aiscenblue@gmail.com',
    license='MIT',
    url='https://github.com/aiscenblue/flask-app-core',
    packages=['flask_app_core'],
    keywords=['flask', 'clask_app_core', 'flask_app_builder'],  # arbitrary keywords
    install_requires=['flask', 'flask-blueprint'],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Framework :: Flask'
    ]
)
