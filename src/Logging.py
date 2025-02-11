import logging


class ProjectLogging:
    def __init__(self, log_file_path='project.log', log_level=logging.INFO):
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers = [
                logging.FileHandler(log_file_path, mode='w'),
                logging.StreamHandler()
            ]
        )
