# 1) Write a program to accept the number of rows from the
# user and print the following number pattern using a loop
#1
#12
#123
#1234
#12345
def number_pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='',)
        print()
number_of_row=input('Enter number of rows : ')
number_pattern(int(number_of_row))
##############################################################

# 2) Write a program to accept a number from a user and calculate
# the sum of all numbers from 1 to a given number
#Enter the number : 10
#Sum is : 55
def sum_num(num1):
    sum=0
    for i in range(1,num1+1):
        sum+=i
    return sum
number=input('Enter the number : ')
print(f'Sum is : {sum_num(int(number))}')
##############################################################

#3)Write a program to accept a name from a user and print the following output:
your_name=input('Enter your name : ')
def print_name(name):#'zakaria' len=7
             #range(0,7-1) -->range(0,6)
    for i in range(0,len(name)):#i=2
                 #range(0,2)
        for j in range(0,i+1):
            print(name[j],end='')#name[0]=z
                                 #name[0]=z name[1]=a
        print()
        if i==len(name)-1:
                     #range(0,6)
            for x in range(len(name)-1,-1,-1):#x=6
                for j in range(x):
                    print(name[j],end='')
                print()

print_name(your_name)
##########################################################################

#4)Write a program to get a word from a user and print that word reversed.
word=input('Enter a word to reverse  : ')
def word_reverse(word_to_reverse):
    for i in range(len(word_to_reverse)-1,-1,-1):
        print(word_to_reverse[i],end='')

word_reverse(word)
print()
###########################################################################

#5)Write a program to print n natural numbers in descending order using a while loop.
range_num=int(input('Enter range : '))
def print_range(range_of_num):
    while 1<= range_of_num:
        print(range_of_num,' ',end='')
        range_of_num-=1

print_range(range_num)
print()

#6)Write a program to display the first 10 multiples of 5.
def  multiples_of_5():
    for i in range(1,11):
        print(i*5,' ',end='')
print('the first 10 multiples of 5 ')
multiples_of_5()
print()
####################################################################

#7)Write a program that takes 3 numbers from the user:
	#Limit_number: the last number that the loop can reach.
	#Target_number: the number that the loop should start from.
	#Max_display_on_screen: the number of maximum times that the multiple of
    # target_number could display on the screen.
Limit_number=int(input('Enter the Limit number: '))
Max_display_on_screen=int(input('Enter the maximum outputs to display(Max_display_on_screen) : '))
Target_number=int(input('Enter the Target number :'))
def num_display(Limit,Max,Target):#300,8,4
    num = 1
                   # 2      6
    for i in range(Target,Limit+1):#i=4
        #   2 <= 10
        if(num<=Max):
                   #1*2=2 4
            print(num*Target,' ',end='')
            num+=1
            if(Limit==num*Target):
                print(num * Target, ' ', end='')
                break
        else:
            break
num_display(Limit_number,Max_display_on_screen,Target_number)






