import logging

logging.basicConfig(format='%(asctime)-15s %(levelname)-8s %(message)s',
                    filename='testrun.log',
                    level=logging.DEBUG)

log = logging.getLogger(__name__)
