#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_update_demo.py
@Time    :   2020/09/30 08:48:52
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Core模式下的记录更新
'''
from wdbd.demo.sqlalchemy.db_persistence import (cookies)
from sqlalchemy import select, update
import wdbd.demo.sqlalchemy.connect_to_mysql as con


# TODO 更新数据不存在的情况

# 数据记录更新
def record_update():
    """数据记录更新
    """
    conn = con.get_connection()
    u = update(cookies).where(cookies.c.cookie_name == "peanutbutter")
    u = u.values(quantity=(cookies.c.quantity + 120))
    print("执行的SQL是: {0}".format(str(u)))
    result = conn.execute(u)
    print("更新的记录数量 = {0}".format(result.rowcount))
    # 更新后的情况
    print("更新后：")
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.where(cookies.c.cookie_name == "peanutbutter")
    for record in conn.execute(s):
        print("{0} - {1}".format(record.cookie_name, record.quantity))
    conn.close()


if __name__ == "__main__":
    record_update()
