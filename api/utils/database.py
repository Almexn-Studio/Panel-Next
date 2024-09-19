import sqlite3
import threading
import config

# 假设数据库配置信息从config模块获取
db_path = config.get('database', 'path')
db_path = db_path + "/database.db"

# 创建线程局部存储
local_storage = threading.local()

def get_connection():
    """为当前线程获取数据库连接"""
    if not hasattr(local_storage, 'connection'):
        local_storage.connection = sqlite3.connect(db_path)
    return local_storage.connection

def get_cursor():
    """为当前线程获取游标"""
    connection = get_connection()
    return connection.cursor()

# 创建锁对象
lock = threading.Lock()

def create_table_if_not_exist(table_name, columns):
    with lock:  # 使用锁确保线程安全
        column_definitions = ', '.join([f'{name} {type}' for name, type in columns.items()])
        cursor = get_cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})')
        connection = get_connection()
        connection.commit()

def add_document(collections: str, document: list):
    with lock:  # 使用锁确保线程安全
        columns = list(document[0].keys())
        column_types = ['TEXT'] * len(columns)  # 假设所有字段都是文本类型

        # 检查表是否存在，如果不存在则创建
        create_table_if_not_exist(collections, dict(zip(columns, column_types)))

        placeholders = ', '.join(['?'] * len(columns))
        columns_str = ', '.join(columns)
        sql = f'INSERT INTO {collections} ({columns_str}) VALUES ({placeholders})'

        cursor = get_cursor()
        cursor.executemany(sql, [list(d.values()) for d in document])
        connection = get_connection()
        connection.commit()
        return cursor.rowcount

def get_document(collections: str, query: dict):
    try:
        with lock:  # 使用锁确保线程安全
            conditions = ' AND '.join([f"{key} = ?" for key in query.keys()])
            sql = f'SELECT * FROM {collections} WHERE {conditions}'
            cursor = get_cursor()
            cursor.execute(sql, list(query.values()))
            return cursor.fetchall()
    except sqlite3.OperationalError:
        return []

def update_document(collections: str, query: dict, new_data: dict):
    with lock:  # 使用锁确保线程安全
        set_clause = ', '.join([f"{key} = ?" for key in new_data.keys()])
        where_clause = ' AND '.join([f"{key} = ?" for key in query.keys()])
        sql = f'UPDATE {collections} SET {set_clause} WHERE {where_clause}'

        values = list(new_data.values()) + list(query.values())
        cursor = get_cursor()
        cursor.execute(sql, values)
        connection = get_connection()
        connection.commit()
        return cursor.rowcount

def delete_document(collections: str, query: dict):
    with lock:  # 使用锁确保线程安全
        conditions = ' AND '.join([f"{key} = ?" for key in query.keys()])
        sql = f'DELETE FROM {collections} WHERE {conditions}'

        cursor = get_cursor()
        cursor.execute(sql, list(query.values()))
        connection = get_connection()
        connection.commit()
        return cursor.rowcount