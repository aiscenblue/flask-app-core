from os import path as os_path

from flask import Flask

from .config.app import DevelopmentConfig as Config
from flask_blueprint import Core


class Bootstrap:

    __app = None
    __root_dir = None
    _config = Config

    def __init__(self, import_name, main_dir, *args, **kwargs):
        self.__root_dir = os_path.dirname(main_dir)
        self.__app = Flask(import_name, instance_relative_config=True)
        if "config" in kwargs:
            self._config = kwargs["config"]

        if len(args):
            self.system_config(system=args[0])

        self.configuration(self._config)

    def system_config(self, system):
        if len(system) > 1:
            if '--debug' in system:
                setattr(Config, 'DEBUG', system[2])
        self.configuration(conf=Config)

    def configuration(self, conf):
        """ configuration file fore core module """
        self.__app.config.from_object(conf)

    def start(self):
        """ for blueprint registration """
        Core(app=self.__app, root_path='.module')
        self.__app.run(host=Config.HOST, port=Config.PORT)
        return self.__app
