import logging
import os


def logger(logpath="", filename=""):
    logpath = os.getcwd()
    filename = "log.txt"
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(funcName)20s() - %(message)s",
        level=logging.INFO,
        handlers=[
            logging.FileHandler("{0}/{1}.log".format(logpath, filename)),
            logging.StreamHandler(),
        ],
    )
    return logging
