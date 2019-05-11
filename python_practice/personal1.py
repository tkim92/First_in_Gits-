Number_list = []
for i in range(5):
      inputNum0=int(input("정수를 입력해 주세요 :"))
      while (inputNum0 <= 51 or inputNum0 >= 100):
            print("51이상 100이하의 값을 입력해 주세요.")
            inputNum0=int(input("정수를 입력해 주세요 :"))
      Number_list.append(inputNum0)

print(Number_list)
