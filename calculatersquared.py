#!/usr/bin/python
import sys
import pandas as pd
import numpy as np
from sqlalchemy import insert, Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///results.db')
session = sessionmaker(bind=engine)()
Base = declarative_base()
class results(Base, object):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    name2 = Column(String)
    r = Column(Float)
    def __init__(self, name: str, name2: str, r: float):
        self.name = name
        self.name2 = name2
        self.r = r
    def __repr__(self):
        return f'{self.name} {self.name2} {self.r}'
# Accept two csv files as command line arguments
if len(sys.argv) != 3:
    print("Usage: python calculatersquared.py <file1> <file2>")
    sys.exit(1)
input_file = sys.argv[1]
input_file1 = sys.argv[2]
data = pd.read_csv(input_file)
data1 = pd.read_csv(input_file1)

r_squared = np.corrcoef(data['Value'], data1['Value'])[0, 1]

session.add(results(name=input_file, name2=input_file1, r=r_squared))
session.commit()
