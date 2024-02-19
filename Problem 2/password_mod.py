"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Isaac Neal
Lab Time: 3:00 pm
"""

def password_mod():
    word = input()
    password = '' 
    # Type your code here.
    passwordLetters = []
    i = 0
    passwordLetters.extend(word)
        

    for word in passwordLetters:
        if(passwordLetters[i] == "i"):
            passwordLetters[i] = '1'
        if(passwordLetters[i] == ("a")):
            passwordLetters[i] = '@'
        if(passwordLetters[i] == ("m")):
            passwordLetters[i] = 'M'
        if(passwordLetters[i] == ("B")):
            passwordLetters[i] = '8'
        if(passwordLetters[i] == ("s")):
            passwordLetters[i] = '$'
        password += str(passwordLetters[i])
        i = i + 1
    print(password + "!")
    

if __name__ == "__main__":
    password_mod()