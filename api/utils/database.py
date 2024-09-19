import sqlite3
import config

# 假设数据库配置信息从config模块获取
db_path = config.get('database', 'path')
db_path = db_path+"/database.db"
# 连接到SQLite数据库
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

def create_table_if_not_exist(table_name, columns):
    # 根据columns参数动态构建SQL语句
    column_definitions = ', '.join([f'{name} {type}' for name, type in columns.items()])
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})')
    connection.commit()

def add_document(collections:str, document:list):
    # 获取表结构
    columns = list(document[0].keys())
    column_types = ['TEXT'] * len(columns)  # 假设所有字段都是文本类型

    # 检查表是否存在，如果不存在则创建
    create_table_if_not_exist(collections, dict(zip(columns, column_types)))

    placeholders = ', '.join(['?'] * len(columns))
    columns_str = ', '.join(columns)
    sql = f'INSERT INTO {collections} ({columns_str}) VALUES ({placeholders})'

    cursor.executemany(sql, [list(d.values()) for d in document])
    connection.commit()
    return cursor.rowcount

def get_document(collections:str, query:dict):
    conditions = ' AND '.join([f"{key} = ?" for key in query.keys()])
    sql = f'SELECT * FROM {collections} WHERE {conditions}'
    cursor.execute(sql, list(query.values()))
    return cursor.fetchall()

def update_document(collections:str, query:dict, new_data:dict):
    set_clause = ', '.join([f"{key} = ?" for key in new_data.keys()])
    where_clause = ' AND '.join([f"{key} = ?" for key in query.keys()])
    sql = f'UPDATE {collections} SET {set_clause} WHERE {where_clause}'

    values = list(new_data.values()) + list(query.values())
    cursor.execute(sql, values)
    connection.commit()
    return cursor.rowcount

def delete_document(collections:str, query:dict):
    conditions = ' AND '.join([f"{key} = ?" for key in query.keys()])
    sql = f'DELETE FROM {collections} WHERE {conditions}'

    cursor.execute(sql, list(query.values()))
    connection.commit()
    return cursor.rowcount