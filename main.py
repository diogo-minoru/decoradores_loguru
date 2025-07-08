from loguru import logger
from sys import stderr

'''
logger.debug("Mensagem")
logger.info("Mensagem")
logger.error("Mensagem")
logger.warning("Mensagem")
logger.critical("Mesagem")
'''

logger.add(
    "meulog.log",
    format = "{time} {level} {message} {file}",
    level = "INFO")

logger.add(
    "arquivo_critico.log",
    format = "{time} {level} {message} {file}", 
    level = "CRITICAL")


def soma(x, y):
    resultado = x + y
    try:
        return logger.info(f"Você obteve o resultado de {resultado}")
    except Exception as e:
        return e
    
soma(2, 2)