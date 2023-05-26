import argparse
import logging
from time import sleep

import uvicorn

from aciniformes_backend.routes.base import app
from aciniformes_backend.scheduler import Scheduler
from aciniformes_backend.settings import get_settings


logger = logging.getLogger(__name__)
settings = get_settings()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--mode', choices=['run_api', 'run_scheduler'], help='Run mode.', required=True
    )
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    args = get_args()
    logger.info(vars(args))

    match args.mode:
        case 'run_api':
            logger.info("Starting API")
            uvicorn.run(app)
            exit(0)
        case 'run_scheduler':
            logger.info("Starting Scheduler")
            scheduler = Scheduler()
            while True:
                scheduler.update(settings.SCHEDULER_FREQUENCY_SEC)
                # TODO Future возможно считать дельту выполнения update
                sleep(settings.SCHEDULER_FREQUENCY_SEC)
