import pandas as pd
from datetime import date
import cowsay

import time
import random as rn
def add():
        Brand = input("Enter Brand Name :  ")
        Price = int(input("Enter price :  "))
        Ram = input("Enter Ram :  ")
        Rom = input("Enter Rom :   ")
        Camera = input("Enter Camera :  ")
        Battery = input("Enter Battery :  ")
        ddf = pd.read_csv(r'‪C:\Users\dell\Desktop\Ayush Project\availablemob.csv')
        n = ddf['Brand'].count()
        ddf.at[n] = [Brand,Price,Ram,Rom,Camera,Battery]
        ddf.to_csv(r'‪C:\Users\dell\Desktop\Ayush Project\availablemob.csv',index = False)
        print("Mobile added successfully......")
        print('   ')
        main()
        

def addsells():
        Name = input("Enter Name :   ")
        Brand = input("Enter Mobile Name :   ")
        BillsID = input("Enter Bills ID :   ")
        Price = int(input("Enter price :  "))
        Date = input('Enter Date :   ')
        ddf = pd.read_csv(r'‪C:\Users\dell\Desktop\Ayush Project\sale.csv')
        d = ddf['Brand'].count()
        ddf.at[d] = [Name,Brand,BillsID,Price,date.today()]
        ddf.to_csv(r'‪C:\Users\dell\Desktop\Ayush Project\sale.csv',index=False)
        print('Data added successfully......')
        print('')
        main()


def addreturn():
        Name = input("Enter Name :   ")
        Brand = input("Enter Mobile Name :   ")
        BillsID = input("Enter Bills ID :   ")
        Price = int(input("Enter price :  "))
        Date = input('Enter Date :   ')
        ddf = pd.read_csv(r'‪C:\Users\dell\Desktop\Ayush Project\return.csv')
        d = ddf['Brand'].count()
        ddf.at[d] = [Name,Brand,BillsID,Price,date.today()]
        ddf.to_csv(r'‪C:\Users\dell\Desktop\Ayush Project\return.csv',index=False)
        
        print('Mobile return successfully......')
        print('')
        main()


def main():
        print("\n 1. To display list of mobile \n 2. To display no. of mobile sold \n 3. To display no. of mobile Return \n 4. Add new mobile \n 5. sells new phone \n 6.Return phone \n 7. Game \n 8. Exit  ")
        print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        print('  ')
        ch = int(input("Enter your choice :  "))
        if ch == 1:
                ddf = pd.read_csv(r'C:\Users\dell\Desktop\Ayush Project\availablemob.csv')
                print(ddf)
                main()
                print('  ')
        elif ch == 2:
                ddf = pd.read_csv(r'‪../Ayush Project/sale.csv')
                print(ddf)
                print('  ')
                main()
        elif ch == 3:
                ddf = pd.read_csv(r'‪../Ayush Project/return.csv')
                print(ddf)
                print('  ')
                main()
        elif ch == 4:
                add()
                print('  ')
                main()
        elif ch == 5:
                addsells()
                print('  ')
                main()
        elif ch == 6:
                addreturn()
                print('  ')
                main()
        elif ch == 7:
                print(' ')
                print(' ')
                cho()
        elif ch == 8:
                cowsay.cow("Thank you ")
        else:
                cowsay.daemon("Invalid input ")
                main()


def pas():
        print('⭐',end ='    ')
        print('   ⭐⭐⭐ ',end='  ')
        print('  ⭐⭐⭐',end='   ')
        print(' ⭐⭐⭐',end='  ')
        print('⭐     ⭐')
        
        print('⭐',end='    ')
        print('  ⭐    ⭐',end='    ')
        print('⭐',end='    ')
        print('       ⭐',end='  ')
        print('  ⭐   ⭐⭐')
        
        print('⭐',end='    ')
        print('  ⭐    ⭐',end='    ')
        print('⭐  ⭐⭐',end=' ')
        print('   ⭐',end='  ')
        print('  ⭐  ⭐ ⭐')
        
        print('⭐',end='    ')
        print('  ⭐    ⭐',end='    ')
        print('⭐    ⭐',end='  ')
        print('  ⭐',end='  ')
        print('  ⭐⭐   ⭐')
        
        print('⭐⭐⭐',end='  ')
        print('⭐⭐⭐ ',end='    ')
        print(' ⭐⭐⭐',end='  ')
        print('⭐⭐⭐',end='  ')
        print('⭐     ⭐')
        
        print(' ')
        print(' ')
        pa = input("Enter Password :  ")
        if pa == "1234":
            print("please wait",end='')
            time.sleep(1)
            print(("."),end='')
            time.sleep(1)
            print(("."),end='')
            time.sleep(1)
            print(("."),end='')
        
            print("-_-_-_-_-_-_-_-_-_-_WELCOME _-_-_-_-_-_-_-_  ")
            print('   ')
            main()
        else:
            cowsay.daemon("Invalid Pssword")
            print('  ')
            pas()
                


def game(l):
        a = rn.randint(1,l)
        for i in range(1,7):
                if i == 6:
                        print('  ')
                        print('This is your last chance \n do you want Hints ')
                        h = int(input('1.Yes / 2.No  :   '))
                        if h == 1:
                                if a % 2 == 0:
                                        print('The no. is closes to....',a-1)
                                else:
                                        print('The no. is closes to....',a+1)
                b = int(input("Enter Number :   "))
                if b > a:
                        print('Your number is Greater ')
                if b < a:
                        print('Your number is Lower  ')
                if b == a:
                        print("You win .....")
                        break
        else:
                print('     ')
                print('You lost the game........')
                print(' ')
                print('The no. is........',a)
#Mr_Aayush
def cho():
        ch = int(input("Choose your level:  \n \n 1.Easy \n 2.Medium \n 3.Hard \n  :     "))
        if ch == 1:
                print('guess a number between 1 to 50 ')
                game(50)
        elif ch == 2:
                print('guess a number between 1 to 100 ')
                game(100)
        elif ch == 3:
                print('guess a number between 1 to 200')
                game(200)
        else:#Mr_Ayush
                print('Invalid input.....')
                cho()
        print('  ')
        print('  ')
        print('Do you want to play again...')
        aa = input('1.Yes \n 2.No :   ')
        if aa == '1':
                cho()
        else:
                print('Thank you ')
                main()

pas()
