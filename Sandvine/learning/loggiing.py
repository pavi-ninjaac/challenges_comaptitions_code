import logging

logger = logging.getLogger('pavi')
logger.setLevel(logging.DEBUG)

#creating the handler
handler = logging.StreamHandler()
format = logging.Formatter('%(name)s :: %(message)s')

#set the format to the handler
handler.setFormatter(format)

#set the handler to the logger
logger.addHandler(handler)

logger.info('The meaasge is very')
