"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Isaac Neal    
Lab Time: 3:00 pm
"""

def inc_5():
    # Write your code here
    integerOne = int(input())
    integerTwo = int(input())
    allIntegers = ' '
    while(integerTwo >= integerOne):
        allIntegers += str(integerOne) + " "
        integerOne += 5
    print(allIntegers)
    if(integerOne > integerTwo):
        print("Second integer can't be less than the first.")




if __name__ == '__main__':
    inc_5()