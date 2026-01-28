#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7106708184:AAGCVwbDVeTTO5XAjMgTgVB8BKGaIz9dvhU")
    API_ID = int(os.environ.get("API_ID", "29868104"))
    API_HASH = os.environ.get("API_HASH", "5329d31cf3930620a59c0c46cdd2b50d")
    AUTH_USERS = "7070250147"


