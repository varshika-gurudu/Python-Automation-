'''import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automations.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        #logging.basicConfig(filename="logfilename.log", level=logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        #logger.setLevel(logging.ERROR)
        return logger
'''

import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
