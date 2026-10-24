import json

# ---------- 1. 读取数据 ----------
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

aliases = data["aliases"]

interactions = {}
for item in data["interactions"]:
    a, b = item["drugs"]
    interactions[(a, b)] = {"level": item["level"], "note": item["note"]}

icons = {"严重": "🔴", "中度": "🟠", "轻度": "🟡"}


# ---------- 2. 函数定义 ----------
def normalize(name):
    name = name.strip().lower()
    return aliases.get(name)


def check(drug1, drug2):
    if (drug1, drug2) in interactions:
        return interactions[(drug1, drug2)]
    if (drug2, drug1) in interactions:
        return interactions[(drug2, drug1)]
    return None


# ---------- 3. 主程序 ----------
while True:
    a = input("第一种药（输入 q 退出）：")
    if a == "q":
        break
    b = input("第二种药：")

    n1 = normalize(a)
    n2 = normalize(b)

    if n1 is None:
        print(f"不认识这个药：{a}")
        continue
    if n2 is None:
        print(f"不认识这个药：{b}")
        continue

    result = check(n1, n2)

    if result:
        icon = icons[result["level"]]
        print(f"{icon} 严重程度：{result['level']}")
        print(f"说明：{result['note']}")
    else:
        print("数据库中没有记录，不代表没有相互作用")
        frist drug for alisses
        print (interactions)
        openloud
        icons=absystems("level")item drugs