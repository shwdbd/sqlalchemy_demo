#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_insert_demo.py
@Time    :   2020/09/29 14:54:05
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   Core模式下的数据操作：数据插入

示例代码：
- 使用 table.insert().values模式插入数据
    - table_insert()
- 使用 insert(table).values模式插入数据
    - insert_function()
- 使用 con.execute(ins, values)模式插入数据
    - insert_with_execute()
- 插入多条记录
    - insert_mutile_record()

- 数据重复插入
- 获取自动+1字段的值
- 使用insert().values模式的SQL语句查看

'''
from wdbd.demo.sqlalchemy.db_persistence import (cookies)
import wdbd.demo.sqlalchemy.connect_to_mysql as con
from sqlalchemy import insert


# 使用 table.insert().values模式插入数据
def table_insert():
    """使用 table.insert().values模式插入数据
    """
    print("使用 table.insert().values模式插入数据")
    ins = cookies.insert().values(cookie_name="chocolatechip",
                                  cookie_recipe_url="http://some.aweso.me/cookie/recipe.html", cookie_sku="CC01", quantity="12", unit_cost="0.50")
    print("待执行的语句 = {0}".format(ins))
    print("编译后未执行语句的参数 = {0}".format(ins.compile().params))

    # 执行插入
    conn = con.get_connection()
    result = conn.execute(ins)
    conn.close()
    print("插入一条新记录！")
    print("inserted_primary_key = " + str(result.inserted_primary_key))


# 使用 insert(table).values模式插入数据
def insert_function():
    """使用 insert(table).values模式插入数据
    """
    print("使用 insert(table).values模式插入数据")
    ins = insert(cookies).values(cookie_name="chocolatechip",
                                 cookie_recipe_url="http://some.aweso.me/cookie/recipe.html", cookie_sku="CC01", quantity="12", unit_cost="0.50")
    print("待执行的语句 = {0}".format(ins))
    print("编译后未执行语句的参数 = {0}".format(ins.compile().params))

    # 执行插入
    conn = con.get_connection()
    result = conn.execute(ins)
    conn.close()
    print("插入一条新记录！")
    print("inserted_primary_key = " + str(result.inserted_primary_key))


# 使用 con.execute(ins, values)模式插入数据
def insert_with_execute():
    """使用 con.execute(ins, values)模式插入数据
    """
    print("使用 con.execute(ins, values)模式插入数据")
    ins = cookies.insert()
    print("待执行的语句 = {0}".format(ins))
    print("编译后未执行语句的参数 = {0}".format(ins.compile().params))

    # 执行插入
    conn = con.get_connection()
    result = conn.execute(ins, cookie_name="chocolatechip",
                          cookie_recipe_url="http://some.aweso.me/cookie/recipe.html", cookie_sku="CC01", quantity="12", unit_cost="0.50")
    conn.close()
    print("插入一条新记录！")
    print("inserted_primary_key = " + str(result.inserted_primary_key))


# 插入多条记录
def insert_mutile_record():
    """插入多条记录
    """
    print("使用 con.execute(ins, values)模式插入数据")
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
    print("待执行的语句 = {0}".format(ins))
    print("编译后未执行语句的参数 = {0}".format(ins.compile().params))

    # 执行插入
    conn = con.get_connection()
    result = conn.execute(ins, record_data)
    if result:
        conn.close()
        print("插入2条新记录！")


if __name__ == "__main__":
    insert_mutile_record()
