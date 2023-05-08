# coding=utf8
import datetime
import os
import sys
import uuid
from enum import Enum

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

sys.path.insert(0, os.path.abspath("."))
import settings

engine = create_engine(settings.MysqlConnStr, echo=True)

connect = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class QAsType(Enum):
    CHOICE = 0
    COMPLETION = 1
    JUDGEMENT = 2


class QA(Base):
    __tablename__ = 't_qas'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    UUID = Column(String(50))
    Topic = Column(String(100))
    Ans = Column(String(10))
    Point = Column(String())
    Type = Column(Integer)
    CreateTime = Column(DateTime)
    UpdateTime = Column(DateTime)


with open('.\\tools\\题库01.txt', 'r', encoding='utf8') as f:
    line = f.readline().strip()
    while line:
        if line:
            strs = line.split('+')
            topic = strs[0][0:-3]
            topic += '\n'
            topic += strs[1]

            ans = strs[0][-2]
            point = 1
            topic_type = QAsType.JUDGEMENT.value

            session.add(QA(
                UUID=uuid.uuid1(),
                Topic=topic,
                Ans=ans,
                Point=point,
                Type=topic_type,
                CreateTime=datetime.datetime.now(),
                UpdateTime=datetime.datetime.now()
            ))

            session.commit()

        line = f.readline().strip()


with open('.\\tools\\题库02.txt', 'r', encoding='utf8') as f:
    line = f.readline().strip()
    while line:
        if line:
            strs = line.split('+')
            topic = strs[0][:-3]
            topic += '\n'
            topic += ''.join(strs[1:])

            ans = strs[0][-2]
            point = 1
            topic_type = QAsType.JUDGEMENT.value

            session.add(QA(
                UUID=uuid.uuid1(),
                Topic=topic,
                Ans=ans,
                Point=point,
                Type=topic_type,
                CreateTime=datetime.datetime.now(),
                UpdateTime=datetime.datetime.now()
            ))

            session.commit()

        line = f.readline().strip()

