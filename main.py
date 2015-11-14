#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

from playground.db import *
from playground.settings import LOGGING, DATABASES
from playground.service import AccountService
from playground.models import Base

logger = logging.getLogger()


def main():
    logging.config.dictConfig(LOGGING)
    # drop all tables in debug mode
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    #session.commit()
    # work with session
    # session.add(Member(id=1, name='hello'))
    # session.commit()
    # svc = AccountService(session)
    # act = svc.create_new_user('somebody')
    # print(act.create_at)
    # print(act.last_signed_at)
    # 
    # svc.sign_in('somebody')
    # print(act.create_at)
    # print(act.last_signed_at)
    

if __name__ == '__main__':
    main()
