# flask-app-core
application core for flask-starter-kit

## Installation
`pip install flask-app-core`
> view on pypi

> https://pypi.python.org/pypi/flask-app-core

## Create Starter application
> create start.py to your root directory

> paste the code below
```
import sys
from flask_app_core import Bootstrap
from app.config.app import DevelopmentConfig


if __name__ == "__main__":
    bootstrap = Bootstrap(import_name=__name__, main_dir=__file__)
    bootstrap.start()

```

`main_dir=__file__`
```
This points your app root directory __file__ represents your app main filename 
where it will be used for internal pointer to Flask library
```

## Advance Configuration

```
from path.to.your.config.class import DevelopmentConfig


if __name__ == "__main__":
bootstrap = Bootstrap(
    import_name=__name__, 
    app_dir=__file__, 
    config=DevelopmentConfig, 
    environment='development')
    
bootstrap.start()
```
```
If no configuration file feed as parameter it will fetch the default DEVELOPMENT 

configuration choices: 'development' or 'production'
```
> Example config class
```
"""
    flask configuration found in http://flask.pocoo.org/docs/0.12/config/
"""


class BaseConfig:
    HOST = "127.0.0.1"
    PORT = 8000
    ADMINS = frozenset(['aiscenblue@gmail.com'])
    SECRET_KEY = 'SecretKeyForSessionSigning'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"


class ProductionConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True

```
