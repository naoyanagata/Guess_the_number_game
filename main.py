import random

def select_mi_max_number():
  number_arr = []

  min_number = int(input("最小数を入力してね！: "))
  max_number = int(input("最大数を入力してね！: "))

  number_arr.append(min_number)
  number_arr.append(max_number)

  return number_arr

def start_game():
  retval = ""
  
  # min_max_number_arr：インデックス０番目に最小数、１番目に最大数を格納
  min_max_number_arr = select_mi_max_number()
  
  while min_max_number_arr[0] > min_max_number_arr[1]:
    print("無効な入力を検知。もう一度入力してね！")
    min_max_number_arr = select_mi_max_number()
  
  random_number = random.randint(min_max_number_arr[0], min_max_number_arr[1])

  flag = False
  while flag == False:
    input_number = int(input("これだと思う数字を入力してね！: "))
    if random_number == input_number:
      retval = "Bingo! クリアだよ！"
      flag = True
    elif (input_number < min_max_number_arr[0]) or (input_number > min_max_number_arr[1]):
      print("入力が範囲外だね！もう一度入力してね！")
    else:
      print("ハズレ！もう一回！")
  
  return retval

print("二つの数字、最小数と最大数を入力してね!\n与えられた最小数〜最大数の範囲内でランダムに数字を選ぶから、その数字を当ててみてね!")

print(start_game())