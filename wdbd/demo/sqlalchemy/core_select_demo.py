#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_select_demo.py
@Time    :   2020/09/29 16:46:19
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Core模式下数据查询

具体示范代码：
- simple_select : 简单查询全部记录，即select * from xxx
- select_column : 仅访问某些列，即select a, b from xxx
- select_order  : 排序，即 order by desc
- select_limit  : 限制返回记录数量，即 limit 100
- select_sql_inner_function : SQL内部函数，即如count、sum、label
- select_where : TODO 条件过滤，即where语句, = or like
- select_ClauseElement : TODO ClauseElement功能
- select_col_func : TODO 列运算符，即如distinct, between, concate
- select_bool_func : 布尔运算符，即and or


'''
from wdbd.demo.sqlalchemy.db_persistence import (cookies)
from sqlalchemy import select, desc, and_
from sqlalchemy.sql import func
import wdbd.demo.sqlalchemy.connect_to_mysql as con


def data_setup():
    """准备试验数据

    往数据库中插入两条数据

    """
    print("测试用数据库准备")
    ins = cookies.insert()
    record_data = [
        {
            'cookie_name': 'peanutbutter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01', 'quantity': '24', 'unit_cost': '0.25'},
        {
            'cookie_name': 'oatmealraisin',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01', 'quantity': '100', 'unit_cost': '1.00'}
    ]
    # 执行插入
    conn = con.get_connection()
    result = conn.execute(ins, record_data)
    if result:
        conn.close()
        print("插入2条新记录！")
    print("数据准备完成")


# 简单的数据查询，查出cookies表中所有数据
def simple_select():
    """简单的数据查询，查出cookies表中所有数据
    """
    conn = con.get_connection()
    s = select([cookies])
    print(type(s))
    print("执行的SQL是: {0}".format(str(s)))
    for record in conn.execute(s):
        print(record)
        # 三种不同方式，访问字段信息
        print(record[1])
        print(record.cookie_name)
        print(record[cookies.c.cookie_name])
    conn.close()


# 仅访问某些列，即select a, b from xxx
def select_column():
    """仅访问某些列，即select a, b from xxx
    """
    conn = con.get_connection()
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    print("执行的SQL是: {0}".format(str(s)))
    for record in conn.execute(s):
        print("{0} - {1}".format(record.cookie_name, record.quantity))
    conn.close()


# 排序，即 order by desc
def select_order():
    """排序，即 order by desc
    """
    conn = con.get_connection()
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.order_by(desc(cookies.c.quantity))
    print("执行的SQL是: {0}".format(str(s)))
    for record in conn.execute(s):
        print("{0} - {1}".format(record.cookie_name, record.quantity))
    conn.close()


# 限制返回记录数量，即 limit 100
def select_limit():
    """限制返回记录数量，即 limit 100
    """
    conn = con.get_connection()
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.limit(1)
    print("执行的SQL是: {0}".format(str(s)))
    for record in conn.execute(s):
        print("{0} - {1}".format(record.cookie_name, record.quantity))
    conn.close()


# 布尔运算符，即 and or not
def select_bool_func():
    """布尔运算符，即and or
    """
    # and_(), or_(), not_()
    conn = con.get_connection()
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.where(
        and_(cookies.c.quantity > 23, cookies.c.unit_cost < 0.40)
    )
    print("执行的SQL是: {0}".format(str(s)))
    for record in conn.execute(s):
        print("{0} - {1}".format(record.cookie_name, record.quantity))
    conn.close()


# SQL内部函数，即如count、sum、label
def select_sql_inner_function():
    """[summary]
    """
    conn = con.get_connection()

    # sum:
    s = select([func.sum(cookies.c.quantity).label("sum_quan")])
    print("执行的SQL是: {0}".format(str(s)))
    rp = conn.execute(s)
    print("sum of quan is {0}".format(rp.first().sum_quan))

    # count
    s = select([func.count(cookies.c.cookie_name).label("count_name")])
    print("执行的SQL是: {0}".format(str(s)))
    rp = conn.execute(s)
    print("count of name is {0}".format(rp.first().count_name))

    # distinct
    s = select([func.distinct(cookies.c.cookie_name).label("distinct_name")])
    print("执行的SQL是: {0}".format(str(s)))
    for record in conn.execute(s):
        print("{0}".format(record.distinct_name))

    conn.close()


if __name__ == "__main__":
    # data_setup()      # 准备测试数据

    # simple_select()   # 简单的数据查询，查出cookies表中所有数据
    # select_column()   # 仅访问某些列，即select a, b from xxx
    # select_order()    # 排序，即 order by desc
    # select_limit()    # 限制返回记录数量，即 limit 100
    # select_bool_func()  # 布尔运算符，即 and or not
    select_sql_inner_function()     # SQL内部函数，即如count、sum、label
