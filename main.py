#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

from playground.db import *
from playground.settings import LOGGING, DATABASES

logger = logging.getLogger()


def main():
    logging.config.dictConfig(LOGGING)
    Base.metadata.create_all(engine)
    # work with session
    session.add(Member(id=1, name='hello'))
    session.commit()
    

if __name__ == '__main__':
    main()
