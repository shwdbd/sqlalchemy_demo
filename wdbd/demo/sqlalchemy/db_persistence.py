#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   db_persistence.py
@Time    :   2020/09/29 11:26:27
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   数据库表持久化示例

构建表结构，并在数据库中create表

'''
from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Boolean,
                        Numeric, String, DateTime, ForeignKey)
import wdbd.demo.sqlalchemy.connect_to_mysql as conn


# 元数据
metadata = MetaData()

# 表定义
cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2)))

users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('customer_number', Integer(), autoincrement=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email_address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now,
                     onupdate=datetime.now))

orders = Table('orders', metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('user_id', ForeignKey('users.user_id')),
               Column('shipped', Boolean(), default=False))

line_items = Table('line_items', metadata, Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('orders.order_id')),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2)))


if __name__ == "__main__":
    # 数据库表持久化
    engine = conn.get_engine()

    if not engine:
        print("数据库连接失败！")
    else:
        try:
            metadata.create_all(engine)
            print("重构数据库表完成！")
        except Exception as err:
            print("数据库持久化失败，原因：" + str(err))
