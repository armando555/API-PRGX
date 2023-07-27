import logging
log = logging.getLogger("mylogger")

def get_error_message(ex: Exception):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    log.error("-------------------------------------------------------------ERROR-------------------------------------------------------------")
    log.error(message)
    log.error("-------------------------------------------------------------END ERROR-------------------------------------------------------------\n")
    return message