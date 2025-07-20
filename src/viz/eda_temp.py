import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os
from dotenv import load_dotenv

# .envの読み込み
load_dotenv()

# .envからの環境変数の取得
csv_path = os.getenv("CSV_PATH")


# データの読み込み
df = pd.read_csv(csv_path, parse_dates=["Date"])

# カラム名を確認
df.rename(columns={"Date": "date" , "Temparature": "temp=max"}, inplace=True)

# 確認
print("=== 全体データの概要 ===")
print(df.head())
print(df.info())
print(df.describe())

# 2015年のデータを抽出
df_2015 = df[df["date"].dt.year == 2015]

# 抽出結果の確認
print("=== 2015年のデータ ===")
print(df_2015.info())
print(df_2015.head())

# グラフ描画：2015年の日次最高気温の推移
df_2015.plot(x="date", y="temp=max", figsize=(12, 4),
             title="Daily Max Temperature in 2015 (°C)")
plt.tight_layout()
plt.show()