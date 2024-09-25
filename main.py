import random

print("2つの数字、最小数と最大数を入力してね!\n与えられた範囲内の乱数を当てたらクリア!")
min_number = int(input("最小数を入力してください。: "))
max_number = int(input("最大数を入力してください。: "))

if min_number > max_number:
  print("無効な入力です。ゲームを開始できません。")
else:
  random_number = random.randint(min_number, max_number)

  flag = False
  while flag == False:
    input_number = int(input("推測した乱数を入力してください。: "))
    if random_number == input_number:
      print("Bingo!")
      flag = True
    elif (input_number < min_number) or (input_number > max_number):
      print("範囲外の数値です。")
    else:
      print("残念！もう一回！")
      
