# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, NVARCHAR, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Product1(Base):
    __tablename__ = 'Product1'

    ID = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(100), nullable=False)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class UserDatum(Base):
    __tablename__ = 'user_data'
    __table_args__ = (
        Index('udx_env_jnl', 'env', 'bsm_jnl_no', 'pay_channel_no', unique=True),
    )

    ID = Column(Integer, primary_key=True)
    env = Column(NVARCHAR(100), nullable=False)
    cus_no = Column(NVARCHAR(100), nullable=False)
    bsm_jnl_no = Column(NVARCHAR(100), nullable=False)
    pay_channel_no = Column(NVARCHAR(100), nullable=False)
    has_used = Column(NVARCHAR(100), nullable=False)
    insert_time = Column(DateTime)
    update_time = Column(DateTime)
    rtn_code = Column(String(10))
    rtn_msg = Column(String(500))

if __name__ == '__main__':
    user_data = UserDatum()
