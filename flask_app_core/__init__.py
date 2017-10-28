from os import path as os_path
from flask import Flask
from .base_config import DevelopmentConfig as Config
from flask_blueprint import Core
import inspect


__version__ = '1.0.6'


class Bootstrap:

    __app = None
    __root_dir = None
    _config = Config
    _module_dir = ".module"

    def __init__(self, import_name, app_dir, **kwargs):
        self.__root_dir = os_path.dirname(app_dir)
        self.__app = Flask(import_name, instance_relative_config=True)
        if "config" in kwargs:
            if inspect.isclass(kwargs['config']):
                self._config = kwargs["config"]
            else:
                raise ValueError("config must be a class type")
        if "module" in kwargs:
            if os_path.isdir(kwargs['module']):
                self._module_dir = kwargs["module"]
            else:
                raise ValueError("module is not a directory")
        if "environment" in kwargs:
            self.set_environment(kwargs['environment'])

        self.configuration(self._config)

    """ 
        set default as Development configuration
        hot to create module
            python 2
                https://docs.python.org/2/tutorial/modules.html
            python 3
                https://docs.python.org/3/tutorial/modules.html
    """
    def set_environment(self, environment_name='development'):
        debug_testing_conf = True
        setattr(self._config, 'DEBUG', debug_testing_conf)
        setattr(self._config, 'TESTING', debug_testing_conf)

        """ reserved string value for environment name """
        if environment_name == "production":
            debug_testing_conf = False
            setattr(self._config, 'DEBUG', debug_testing_conf)
            setattr(self._config, 'TESTING', debug_testing_conf)

    def configuration(self, conf):
        """ configuration file fore core module """
        self.__app.config.from_object(conf)

    def start(self):
        """ for blueprint registration """
        Core(app=self.__app, root_path=self._module_dir)
        self.__app.run(host=self._config.HOST, port=self._config.PORT)
        return self.__app
