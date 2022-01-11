from connectors.core.connector import Connector, ConnectorError, get_logger

from .operations import *
from .operations import _check_health

logger = get_logger('dnstwist')

class DnsTwist(Connector):
    def execute(self, config, operation_name, params, **kwargs):
        # raise Exception(operation_name)
        try:
            logger.info("operation_name: {0}".format(operation_name))
            result = None
            if operation_name == 'search':
                result = search(config, params)
            return result
        except Exception as e:
            logger.exception("An exception occurred {0}".format(e))
            raise ConnectorError("{0}".format(e))

    def check_health(self, config):
        try:
            return _check_health(config)
        except Exception as e:
            raise ConnectorError(e)

