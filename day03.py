import random
from operator import length_hint

drinks = ["와인", "소주", "고량주", "사케", "위스키"]
foods = ["치즈", "삽겹살", "양꼬치", "광어회", "낙곱새"]

menu_list = f'다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i + 1}) {drinks[i]}  '
menu_list = menu_list + f'{str(len(drinks) + 1)}) 아무거나  {str(len(drinks) + 2)}) 종료'
print(menu_list)

# for i in range(len(drinks)):
#     menu_list = menu_list + f'1) {drinks[i]}  '

def change(s):
    return foods[drinks.index(s)]

def num(menu):
    if menu == str(len(drinks) + 1):
        random_drink = random.choice(drinks)
        print(f'{random_drink}에 어울리는 안주는 {change(random_drink)} 입니다')
    elif menu == str(len(drinks) + 2):
        print(f'다음에 또 오세요')
    else:
        print(f'{drinks[int(menu)-1]}에 어울리는 안주는 {change(drinks[int(menu)-1])} 입니다')

while True:
    menu = input()
    num(menu)
    if menu == str(len(drinks) + 2):
        break


# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
#     if menu == '6':
#         random_drink = random.choice(drinks)
#         print(f'{random_drink}에 어울리는 안주는 {change(random_drink)} 입니다')
#     elif menu == '7':
#         print(f'다음에 또 오세요')
#         break
#     else:
#         print(f'{drinks[int(menu) - 1]}에 어울리는 안주는 {change(drinks[int(menu) - 1])} 입니다')
#
#

# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
#     if menu == '1':
#         print(f'{drinks[0]}에 어울리는 안주는 {change(drinks[0])} 입니다')
#     elif menu == '2':
#         print(f'{drinks[1]}에 어울리는 안주는 {change(drinks[1])} 입니다')
#     elif menu == '3':
#         print(f'{drinks[2]}에 어울리는 안주는 {change(drinks[2])} 입니다')
#     elif menu == '4':
#         print(f'{drinks[3]}에 어울리는 안주는 {change(drinks[3])} 입니다')
#     elif menu == '5':
#         print(f'{drinks[4]}에 어울리는 안주는 {change(drinks[4])} 입니다')
#     elif menu == '6':
#         random_drink = random.choice(drinks)
#         print(f'{random_drink}에 어울리는 안주는 {change(random_drink)} 입니다')
#     elif menu == '7':
#         print(f'다음에 또 오세요')
#         break
