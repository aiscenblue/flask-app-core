# flask-app-core
application core for flask-starter-kit


[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://badge.fury.io/py/flask-app-core)
[![PyPI version](https://badge.fury.io/py/flask-app-core.svg)](https://badge.fury.io/py/flask-app-core)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/aiscenblue/flask-app-core/blob/master/LICENSE)
[![dependencies Status](https://david-dm.org/boennemann/badges/status.svg)](https://github.com/aiscenblue/flask-app-core)

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
#### Create a folder named "module" in your application roon directory before running the application
```
 It states that all your routing config and API modules are located on the "module directory"
```

#### Custom module configuration

```
if __name__ == "__main__":
bootstrap = Bootstrap(
    import_name=__name__, 
    app_dir=__file__, 
    module="to/module/directory"
    config=DevelopmentConfig, 
    environment='development')
    
bootstrap.start()
```

```
If no configuration file feed as parameter it will fetch the default DEVELOPMENT 

configuration choices: 'development' or 'production'
```
### Example config class
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

#### If set to production the debug will be over written to False

# Module Views

```
make_response(render_template('index/view.html', title="Flask Starter Kit!"))
```

#### path
`path starts from your root module directory`

```
~/your_module_directory
---|/module_name
------| view.html
```
`Therefore the path in the example above should be`


```make_response(render_template('module_name/view.html', title="Flask Starter Kit!"))```
