import random

print("二つの数字、xとyを入力してください。入力された数字、xからyまでの間で乱数を生成します。\nその乱数を当てれたらゲームクリアです。")
print("")

while 1:
    try:
        min = float(input("最小数xを入力してください。: "))
        max = float(input("最大数yを入力してください。: "))
        if min > max:
            print("正しく数字を入力してください。")
        else:
            break
    except ValueError:
        print("数字を入力してください。")

number_of_attempts = random.randint(1, 10)
print("解答回数は" + str(number_of_attempts) + "回です。ゲームスタート！")

correct_number = random.randint(min, max)
while(number_of_attempts > 0):
    try:
        guessed_number = float(input("推測した数字を入力してください。: "))
    except ValueError:
        print("数字を入力してください。")
        continue
    if guessed_number == correct_number:
        print("正解！")
        break
    print("違います。")
    number_of_attempts -= 1

print("ゲーム終了。正解は" + str(correct_number) + "でした。")