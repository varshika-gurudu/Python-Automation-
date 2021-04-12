#ConfigParser is a Python class which implements a basic configuration language for Python programs.
# It provides a structure similar to Microsoft Windows INI files.
# ConfigParser allows to write Python programs which can be customized by end users easily

import configparser


#Legacy variant of the ConfigParser. It has interpolation disabled by default and allows for non-string section names,
# option names, and values via its unsafe add_section and set methods,
# as well as the legacy defaults= keyword argument handling
#RawConfigParser to read and update an ini style configuration file

config = configparser.RawConfigParser() # creating an object
config.read(".\\configurations\\config.ini")

#@staticmethod
# is a built-in decorator that defines a static method in the class in Python.
# A static method doesn't receive any reference argument whether it is called by an instance of a class
# or by the class itself.

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','base_url')
        return url

    @staticmethod
    def getUsermail():
        user_mail = config.get('common info','user_mail')
        return user_mail

    @staticmethod
    def getPassword():
        user_password = config.get('common info','user_password')
        return user_password
