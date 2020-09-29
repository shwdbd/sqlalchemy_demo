#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_select_demo.py
@Time    :   2020/09/29 16:46:19
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Core模式下数据查询
'''
from wdbd.demo.sqlalchemy.db_persistence import (cookies)
import wdbd.demo.sqlalchemy.db_persistence as db_persistence
import wdbd.demo.sqlalchemy.core_insert_demo as insert_demo
from sqlalchemy import select
import wdbd.demo.sqlalchemy.connect_to_mysql as con


def data_setup():
    """准备试验数据
    """
    insert_demo.insert_mutile_record()
    print("数据准备完成")


def simple_select():
    """简单的数据查询，查出cookies表中所有数据
    """

    conn = con.get_connection()
    s = select([cookies])
    print(type(s))
    for record in conn.execute(s):
        print(record)
    conn.close()



if __name__ == "__main__":
    # data_setup()

    simple_select()
