age = float(input("请输入年龄（岁）："))
weight = float(input("请输入体重（公斤）："))
scr = float(input("请输入血肌酐（mg/dL）："))

sex = input("请输入性别（男/女）：")

crcl = (140 - age) * weight / (72 * scr)

if sex == "女":
    crcl = crcl * 0.85

print(f"你的 CrCl 是 {crcl:.1f} mL/min")
