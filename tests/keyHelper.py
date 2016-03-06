import os
import sys

pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(pwd, '../config')))
import auth


def grabKey(keyName, envName='', param='key'):
    env = os.environ

    if keyName.upper():
        KEY = env[keyName.upper()]
    elif env or envName.upper() in env:
        KEY = env[envName.upper()]
    else:
        configParser = auth.grab()
        KEY = configParser.get(keyName.lower(), param)
    return KEY
