"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Isaac Neal
Lab Time: 3:00 pm

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    binaryDigits = ''
    while(user_num >= 1):
        binaryDigits += str(user_num % 2)
        user_num = int(user_num / 2)
    print(binaryDigits)
    

if __name__ == "__main__":
    reverse_binary()