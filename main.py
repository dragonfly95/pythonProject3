# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pymysql
import pandas as pd

# http://pythonstudy.xyz/python/article/202-MySQL-%EC%BF%BC%EB%A6%AC

def getConn():
    conn = pymysql.connect(host='localhost', user='root', password='1q2w3e4r5t',
                           db='board_db', charset='utf8')
    return conn

def select(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    conn = getConn()

    curs = conn.cursor()

    sql = "select * from customer"
    curs.execute(sql)

    rows = curs.fetchall()
    for row in rows:
        print(row)

    conn.close()

def insert(name, category, region):
    conn = getConn()
    curs = conn.cursor()
    sql = """insert into customer(name, category, region)
            values (%s, %s, %s)"""
    curs.execute(sql, (name, category, region))
    conn.commit()
    conn.close()
    print('입력완료')

def update(name, category, region, id):
    conn = getConn()
    curs = conn.cursor()
    sql = """update customer set 
               name = %s,
               category = %s,
               region = %s
            where id = %s
          """
    curs.execute(sql, (name, category, region, id))
    conn.commit()
    conn.close()
    print(name, category, region, id)
    print('수정완료')


def delete(id):
    conn = getConn()

    try:
        curs = conn.cursor()
        sql = 'delete from customer where id = %s'
        curs.execute(sql, id)
        conn.commit()
    except Exception as err:
        print(str(err))
    finally:
        conn.close()

    print('삭제완료')


def xlsx_read():
    data = pd.read_excel('./customer.xlsx')
    for entity in data.values:
        print(entity)
        insert(entity[0], entity[1], entity[2])

    select('PyCharm')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # insert('그것이 알고싶다', 1, '서울')
    # update('그것이 알고싶다', 1, '인천', 4)
    # delete(5)
    # select('PyCharm')

    xlsx_read()