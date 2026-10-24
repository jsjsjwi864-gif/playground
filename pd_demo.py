import pandas as pd
data = {
    "name": ["A", "B", "C", "D", "E"],
    "age": [45, 62, 38, 71, 55],
    "weight": [70, 82, 65, 58, 75],
    "scr": [0.9, 1.3, 0.8, 1.5, 1.0],
}
df = pd.DataFrame(data)
print(df)
print(df["age"])                  # 取一列
print(df["age"].mean())           # 平均年龄
print(df.describe())              # 一键出统计摘要
print(df[df["age"] > 60])         # 筛选：年龄大于 60 的行
df["crcl"] = (140 - df["age"]) * df["weight"] / (72 * df["scr"])
print(df)
print(df[df["crcl"] < 60])
df.to_csv("patients.csv", index=False, encoding="utf-8-sig")
df2 = pd.read_csv("patients.csv")
print(df2)