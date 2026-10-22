low = 1
high = 100
count = 0

print("请在心里想一个 1 到 100 之间的数，我来猜！")

while True:
    guess = (low + high) // 2
    count = count + 1
    answer = input(f"我猜是 {guess}，对吗？(大了/小了/对了)：")

    if answer == "对了":
        print(f"我用了 {count} 次猜中了！")
        break
    elif answer == "大了":
        high = guess - 1
    elif answer == "小了":
        low = guess + 1