"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Isaac Neal
Lab Time: 3:00 pm
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    # YOUR CODE HERE
    x = -10
    y = -10
    equation = (a * x) + (b * y)
    equation2 = (d * x) + (e * y)

    while(True):
        if((y > 10)):
            print("There is no solution")
            break
        elif(equation == c and equation2 == f):
            print("x = " + str(x) + " , y = " + str(y)) 
            break
        if(x < 10):
            x += 1
        else:
            y += 1
            x = -10
        equation2 = (d * x) + (e * y)
        equation = (a * x) + (b * y)

        
    
if __name__ == "__main__":
    brute_eq()