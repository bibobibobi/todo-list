import random
import sys

again = 'yes'

while again == 'yes':

    ans = random.randint(1, 100) #產生隨機數字
    l,r,count = 1,100,0

    while True:
    #判斷是否正確輸入整數
        while True:
            try:
                guess = int(input(f'Enter your number between {l} to {r} : '))
                count += 1 #統計猜的次數
                break
            except ValueError:
                print('Please enter correct number')
                continue


        if guess == ans:
            print('Your number is right')
            break
        elif guess < ans:
            print('Right answer is bigger')
            l = guess
        elif guess > ans:
            print('Right answer is smaller')
            r = guess

    print(f'You guessed {count} times to find correct number')
    again = input('Do you want to play again? Enter [yes] to play again : ').lower #將使用者的輸入改為小寫 不必擔心大小寫

sys.exit()