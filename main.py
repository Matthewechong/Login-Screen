from utils2 import*
import pandas as pd
from signup import*
from login import*
df = pd.read_csv('credentials.csv')
print(df['Username'].iloc[0])
print(stringToBytes(df['Username'].iloc[0]))