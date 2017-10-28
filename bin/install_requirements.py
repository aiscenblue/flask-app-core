def main():
    """ install flask """
    try:
        from flask import Flask
        from flask_blueprint import Core
    except ImportError:
        from subprocess import call
        import sys

        __pip_call = "pip"
        if sys.version_info[0] >= 3:
            __pip_call = "pip3"
        call([__pip_call, 'install', '-r', 'bin/requirements.txt'])
        print('requirements successfully installed!')

if __name__ == '__main__':
    main()

