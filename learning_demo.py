import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
from scipy.stats import norm
from scipy import stats
from pandas import DataFrame


train_data = pd.read_csv('train.csv')
# 查看特征列名称
print(train_data.columns)
# 查看基本统计
print(train_data.describe())
