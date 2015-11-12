#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

from playground.db import *
from playground.settings import LOGGING, DATABASES

logger = logging.getLogger()


def main():
    logging.config.dictConfig(LOGGING)
    query_test()
    
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
