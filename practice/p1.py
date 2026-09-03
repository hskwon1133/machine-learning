import pandas as pd


#데이터 불러오기
train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')

#데이터 정보 [train, test 모두]
train_null = train.isna().sum()[train.isna().sum()>0].sort_values(ascending=False)
test_null = test.isna().sum()[test.isna().sum()>0].sort_values(ascending=False)
#
# print(f'info : {train.info()}') #train : float64(3), int64(35), str(43) / test:  float64(11), int64(26), str(43)
# print(f'shape : {train.shape}') #train: 1460row, 81 columns / test: (1459, 80)
# print(f'null : {train_null}')


# 타입별 구분하기
'''
'object' 타입 = pandas가 "문자열(또는 다양한 타입이 섞인 것)"이라고 판단한 컬럼
숫자 타입(float64, int64 등) = 순수하게 숫자만 있는 컬럼
'''

# print(train.columns)
col_total = list(set(train.columns) | set(test.columns)) # 합집합

cat_col = []
cat_num = []
for col in col_total:
    if train[col].dtypes == 'string':
        cat_col.append(col)
    else :
        cat_num.append(col)


# print(cat_col)
# print('SalePrice' in cat_num) # 리스트 안에서 데이터 정보를 찾고 싶으면 in


# 문자형은 모두 50% null 이상은 None으로 나머지는 최빈값으로

over_halfratio = ['MiscFeature', 'Alley', 'Fence', 'MasVnrType', 'FireplaceQu']
for col in cat_col:
    if col in over_halfratio:
        train[col] = train[col].fillna('None')
        test[col] = test[col].fillna('None')
    else:
        mode_val = train[col].mode()
        train[col] = train[col].fillna(mode_val)
        test[col] = test[col].fillna(mode_val)

for col in cat_num:
    if col in over_halfratio:
        train[col] = train[col].fillna(0)
        test[col] = test[col].fillna(0)
    else:
        median_val = train[col].median()
        train[col] = train[col].fillna(median_val)
        test[col] = test[col].fillna(median_val)