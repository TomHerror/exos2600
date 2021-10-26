#!/usr/bin/env python3

import model
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///logins.db')
session = Session(engine)

for a in session.query(model.Account):
    print(repr(a))
