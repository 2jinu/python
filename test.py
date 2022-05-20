import pandas
from sqlalchemy import inspect, create_engine


dbms        = 'mysql'
database    = 'test'
user        = 'root'
password    = 'root'
host        = '127.0.0.1'
port        = 3306
engine      = create_engine(f'{dbms}://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4')
inspector   = inspect(engine)

table_names = inspector.get_table_names(database) # 데이터베이스의 테이블 명 리스트 반환
column_names= [column if inspector else None for column in inspector.get_columns(table_names[0], schema=database)] # 테이블의 컬럼 이름 리스트 반환

df.to_sql(name=table_names[0], con=engine, if_exists='append', index=False) # 테이블에 데이터 추가
pandas.read_sql('SELECT * FROM {}'.format(table_names[0]), con=engine) # 테이블의 데이터 읽기