import logging
logging.basicConfig(level=logging.INFO) # default: WARNING
logger = logging.getLogger('System')

def run():
    logger.info('flc-callhome-manager started.')

if __name__ == '__main__':
    run()