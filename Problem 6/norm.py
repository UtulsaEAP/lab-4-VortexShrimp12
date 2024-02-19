"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:
Lab Time:
"""

def norm():
    # Write your code here
    AmountofNumbers = int(input())
    i = 0
    largestNumber = 0
    numbers = []
    while(i < AmountofNumbers):
        floatingPointNumber = float(input())
        if(floatingPointNumber > largestNumber):
            largestNumber = floatingPointNumber
        numbers.append(floatingPointNumber)
        i+=1
    i = 0
    for floatingPointNumber in numbers:
        floatingPointNumber = numbers[i] / largestNumber
        print(f'{floatingPointNumber:.2f}')
        i+=1





if __name__ == "__main__":
    norm()