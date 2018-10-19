import os
from flask import Flask
from flask_blueprint import Core
from .base_config import DevelopmentConfig as Config
import inspect

"""
    Bootstrap
        for running flask application
    
    :param import_name
        your application name
        
    :param app_dir
        your main app directory
            example: the start.py in https://github.com/aiscenblue/flask-starter-kit
    
    HOW TO:
        bootstrap = Bootstrap(import_name=__name__, app_dir=__file__, config=DevelopmentConfig, environment='development')
        bootstrap.start()
        
        LINK: https://github.com/aiscenblue/flask-app-core
"""


class Bootstrap:

    __app = None
    __root_dir = None
    _config = Config
    _module_dir = "modules"
    instance_relative_config = True
    static_path = None
    static_url_path = None
    static_folder = "assets"
    template_folder = _module_dir
    instance_path = None

    def __init__(self, import_name, app_dir, **kwargs):

        self.__root_dir = os.path.dirname(os.path.realpath(app_dir))

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.__app = Flask(import_name,
                           instance_relative_config=self.instance_relative_config,
                           static_url_path=self.static_url_path,
                           static_folder=self.static_folder,
                           template_folder=self.template_folder,
                           instance_path=self.instance_path)

        if "config" in kwargs:

            if inspect.isclass(kwargs['config']):
                self._config = kwargs["config"]
            else:
                raise ValueError("config must be a class type")

        if "module" in kwargs:

            if os.path.isdir(kwargs['module']):
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

    def start(self, **kwargs):
        """ for blueprint registration """
        Core(app=self.__app, root_paths=[self.__root_dir + '/' + self._module_dir])
        self.__app.run(host=self._config.HOST, port=self._config.PORT, **kwargs)
        return self.__app
