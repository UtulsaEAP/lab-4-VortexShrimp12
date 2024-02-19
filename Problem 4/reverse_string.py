"""
Complete the following python code to reverse the string entered by the user.

Name: Isaac Neal
Lab Time: 3:00 pm
"""

def reverse_string():
    # YOUR CODE HERE
    user_Input = str(input())

    printedWord = ' '

    while True:
        if(user_Input != 'Done' or user_Input != 'done' or user_Input != 'd'):
            printedWord += user_Input[::-1] + " "
            user_Input = str(input())
            if(user_Input == 'Done' or user_Input == 'done' or user_Input == 'd'):
                break
        else:
            break
    print(printedWord)


if __name__ == "__main__":
    reverse_string()