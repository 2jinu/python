# pandas

데이터 조작 및 분석을 위해 Python 프로그래밍 언어로 작성된 소프트웨어 라이브러리이다.

# **INDEX**

**1. [Series](#Series)**

 - [dictionary to Series](#dictionary-to-Series)

 - [Indexing](#Indexing-Series)

**2. [DataFrame](#DataFrame)**

 - [dictionary to DataFrame](#dictionary-to-DataFrame)

 - [Indexing](#Indexing-(DataFrame))

**3. [데이터 입·출력](#데이터-입·출력)**

 - [csv](#csv)

 - [tsv](#tsv)

 - [json](#json)

 - [excel](#excel)

 - [mysql](#mysql)


***


# **Series**

pandas의 Series를 이용하여 데이터를 출력해보자.

```py
import pandas

no_index = pandas.Series([1, 2, 3, 4])
index = pandas.Series([1, 2, 3, 4], index=['one', 'two', 'three', 'four'])

print(no_index)
print(index)

출력 결과
0    1
1    2
2    3
3    4
dtype: int64
one      1
two      2
three    3
four     4
dtype: int64
```

Series 데이터를 분석하기 위한 여러가지 Attribute를 사용하여 데이터를 분석할 수 있다.

```py
[Input]
import pandas

s = pandas.Series([1, 2, 3, 4], index=['one', 'two', 'three', 'four'])
print(s.index)
print(s.values)
print(s.dtype)

출력 결과
Index(['one', 'two', 'three', 'four'], dtype='object')
[1 2 3 4]
int64
```


## **dictionary to Series**

dictionary를 Series로 변환하여 다룰 수 있다.

```py
import pandas

dic   = {'one':1, 'two':2, 'three':3, 'four':4}
dic2s = pandas.Series(dic) # pd.Series([1, 2, 3, 4], index=['one', 'two', 'three', 'four'])와 같음
print(dic2s)

출력 결과
one      1
two      2
three    3
four     4
dtype: int64
```

dictionary는 안되지만 Series는 행렬 연산(Element wise)이 가능하다.

```py
print(dic2s*100)

출력 결과
one      100
two      200
three    300
four     400
dtype: int64
```


## **Indexing Series**

인덱싱을 통해 Series 데이터를 조회할 수 있다.

```py
print(s['one']) # 인덱스 명으로 조회
print(s[0])     # 인덱스 위치로 조회

출력 결과
1
1
```


# **DataFrame**

DataFrame은 여러개의 Series들이 합쳐진 형태이다.

DataFrame을 생성해보자.

```py
import pandas

data = [
    ['사람1', 20, '서울'],
    ['사람2', 32, '대전'],
    ['사람3', 20, '인천'],
    ['사람4', 26, '서울']
    ]

df = pandas.DataFrame(data)
print(df)

출력 결과
     0   1   2
0  사람1  20  서울
1  사람2  32  대전
2  사람3  20  인천
3  사람4  26  서울
```

DataFrame을 생성할 때, 열의 이름을 지정할 수 있다.

```py
df = pandas.DataFrame(data, columns=['이름', '나이', '지역'])

출력 결과
    이름  나이  지역
0  사람1  20  서울
1  사람2  32  대전
2  사람3  20  인천
3  사람4  26  서울
```


## **dictionary to DataFrame**

Series와 마찬가지로 dictionary를 통해서 DataFrame을 생성할 수 있다.

dictionary의 key는 DataFrame으로 생성 시 열의 이름이 된다.

```py
import pandas

data = {
    '이름':['사람1', '사람2', '사람3', '사람4'],
    '나이':[20, 32, 20, 26],
    '지역':['서울', '대전', '인천', '서울']
    }

df = pandas.DataFrame(data)
print(df)

출력 결과
    이름  나이  지역
0  사람1  20  서울
1  사람2  32  대전
2  사람3  20  인천
3  사람4  26  서울
```

행의 이름도 사용자 마음대로 변경할 수 있다.

```py
df = pandas.DataFrame(data, index=['a', 'b', 'c', 'd'])

출력 결과
    이름  나이  지역
a  사람1  20  서울
b  사람2  32  대전
c  사람3  20  인천
d  사람4  26  서울
```

행을 열로 지정할 수도 있다.

```py
df = pandas.DataFrame(data)
df1 = df.set_index('이름')
df2 = df.set_index(['나이', '지역'])

print(df1)
print(df2)

출력 결과
     나이  지역
이름
사람1  20  서울
사람2  32  대전
사람3  20  인천
사람4  26  서울
          이름
나이 지역
20  서울  사람1
32  대전  사람2
20  인천  사람3
26  서울  사람4
```


## **Indexing(DataFrame)**

인덱스를 통해서 데이터를 출력할 수 있다.

```py
df = pandas.DataFrame(data)

print(df.loc[0])                    # 0번째 행 출력
print(df.loc[0:2])                  # 0 ~ 2번째 행 출력
print(df.loc[[0, 2]])               # 0과 2번째 행 출력
print(df.loc[:, '이름'])            # 이름 열 출력 (=df['이름'])
print(df.loc[:, ['이름', '지역']])   # 이름과 지역 열 출력
```

loc과 비슷한 iloc을 사용하여 인덱싱을 할 수 있다.

```py
df = pandas.DataFrame(data)

print(df.iloc[0])           # 0번째 행 출력
print(df.iloc[0:2])         # 0 ~ 1번째 행 출력
print(df.iloc[[0, 2]])      # 0과 2번째 행 출력
print(df.iloc[:, 0])        # 이름 열 출력 (=df['이름'])
print(df.iloc[:, [0, 2]])   # 이름과 지역 열 출력
```

조건을 걸어 특정 데이터만 추출할 수 있다.

```py
df = pandas.DataFrame(data)
df_filter = df.loc[:, '나이'] > 25          # 필터링 할 조건
print(df.loc[df_filter, ['이름', '지역']])  # 나이가 25 초과인 이름, 지역 열 출력
```


DataFrame의 append를 이용하여 Series를 추가할 수 있다.

```py
df1 = pandas.DataFrame(data)
df2 = df1.append({'이름':'사람5', '나이':28, '지역':'부산'}, ignore_index=True)
print(df2)

출력 결과
    이름  나이  지역
0  사람1  20  서울
1  사람2  32  대전
2  사람3  20  인천
3  사람4  26  서울
4  사람5  28  부산
```

DataFrame의 loc을 이용하여 Series를 대체하거나 추가할 수 있다.

```py
df1 = pandas.DataFrame(data) # df1.shape[0] = 4
df1.loc[df1.shape[0]] = ['사람5', 28, '부산']
print(df1)

출력 결과
    이름  나이  지역
0  사람1  20  서울
1  사람2  32  대전
2  사람3  20  인천
3  사람4  26  서울
4  사람5  28  부산
```

DataFrame의 여러가지 Attribute로 데이터를 분석할 수 있다.

```py
df = pandas.DataFrame(data)
print(df.index)
print(df.columns)
print(df.values)
print(df.dtypes)
print(df.info())


출력 결과
1. df.index
RangeIndex(start=0, stop=4, step=1)
2. df.columns
Index(['이름', '나이', '지역'], dtype='object')
3. df.values
[['사람1' 20 '서울']
 ['사람2' 32 '대전']
 ['사람3' 20 '인천']
 ['사람4' 26 '서울']]
4. df.dtypes
이름    object
나이     int64
지역    object
dtype: object
5. df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   이름      4 non-null      object
 1   나이      4 non-null      int64
 2   지역      4 non-null      object
dtypes: int64(1), object(2)
memory usage: 224.0+ bytes
None
```


# **데이터 입·출력**

## **csv**

먼저 예제 데이터 <b>csv</b>형식으로 생성하자.

```py
data    = [['이름', '나이', '주소', '혈액형', '결혼 여부'],
           ['가나', '20', '서울', 'A', 'N'],
           ['다라', '19', '경기', 'B', 'N'],
           ['마바', '38', '대구', 'B', 'Y'],
           ['사아', '15', '서울', 'O', 'N'],
           ['자차', '26', '서울', 'AB', 'Y']]
with open('pandas_csv_data.csv', 'w') as fp:
    for d in data: fp.write(','.join(d)+'\n')
```

데이터를 생성했으니 읽고 데이터를 변경 후 저장해보자.

```py
df          = pandas.read_csv('pandas_csv_data.csv', encoding='cp949')
df['키']    = pandas.Series([160.0, 176.5, 172.3, 170.8, 181.3])
df.to_csv('pandas_csv_data2.csv', index=False, encoding='cp949')
```

## **tsv**

먼저 예제 데이터 <b>tsv</b>형식으로 생성하자.

```py
data    = [['이름', '나이', '주소', '혈액형', '결혼 여부'],
           ['가나', '20', '서울', 'A', 'N'],
           ['다라', '19', '경기', 'B', 'N'],
           ['마바', '38', '대구', 'B', 'Y'],
           ['사아', '15', '서울', 'O', 'N'],
           ['자차', '26', '서울', 'AB', 'Y']]
with open('pandas_csv_data.tsv', 'w') as fp:
    for d in data: fp.write('\t'.join(d)+'\n')
```

데이터를 생성했으니 읽고 데이터를 변경 후 저장해보자.

```py
df          = pandas.read_csv('pandas_csv_data.tsv', encoding='cp949', sep='\t')
df['키']    = pandas.Series([160.0, 176.5, 172.3, 170.8, 181.3])
df.to_csv('pandas_csv_data2.tsv', index=False, encoding='cp949', sep='\t')
```

## **json**

<b>json</b> 형식의 데이터를 DataFrame으로 변경할 수 있다.

```py
import pandas

data    = '{"이름":{"0":"가나","1":"다라","2":"마바","3":"사아","4":"자차"},"나이":{"0":"20","1":"19","2":"38","3":"15","4":"26"},"주소":{"0":"서울","1":"경기","2":"대구","3":"서울","4":"서울"},"혈액형":{"0":"A","1":"B","2":"B","3":"O","4":"AB"},"결혼 여부":{"0":"N","1":"N","2":"Y","3":"N","4":"Y"}}'
df      = pandas.read_json(data)
```

## **excel**

기존 tsv나 csv를 <b>excel</b>로 변경하여 저장한 뒤 데이터를 읽고 써보자.

```py
excel   = pandas.ExcelFile('pandas_excel_data.xlsx')
df      = pandas.read_excel('pandas_excel_data.xlsx', sheet_name=excel.sheet_names[0]) # default = Sheet1
df['키']= pandas.Series([160.0, 176.5, 172.3, 170.8, 181.3])
df.to_excel('pandas_excel_data2.xlsx', index=False, sheet_name='회원')
df      = pandas.read_excel('pandas_excel_data2.xlsx', sheet_name='회원')
```

## **mysql**

sqlalchemy를 통해 <b>mysql</b>의 데이터를 DataFrame으로 변환해보자.

```py
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
```
[aa](aa)