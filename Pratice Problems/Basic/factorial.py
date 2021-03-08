# find the factorial of the entered number

fact = 1


def fact_of_num(number):
    global fact
    for i in range(1, number +  1):
        fact = fact * i

    print("Factorial of the numebr is : ", fact)


fact_of_num(5)
