#!/usr/bin/env python3

import hashlib
import model
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pathlib as pl

here = pl.Path('.').resolve()
print(f"CREATE DB HERE {here}")
engine = create_engine('sqlite:///logins.db')
model.Base.metadata.create_all(engine)
