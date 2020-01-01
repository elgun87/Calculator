print("Hi this is simple calculator that will perform simple tasks")
calc_exit = True
while calc_exit:
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number : "))
    operator = input("Chose the operator ' + ' , ' - ' , ' / ' , ' * ' : ")
    if operator == '+':
        result = num_1 + num_2
        print(num_1,'+',num_2,'=',result)
    elif operator == '-':
        result = num_1 - num_2
        print(num_1,'-',num_2,'=',result)
    elif operator == '/':
        if num_1 % num_2 == 0:
            result = num_1 // num_2
            print(num_1,'/',num_2,'=',result)
        elif num_1 % num_2 != 0:
            result = num_1 / num_2
            print(num_1,'/',num_2,'=',result)
    elif operator == "*":
        result = num_1 * num_2
        print(num_1,'*',num_2,'=',result)
    else:
        print("You chosed wrong operator")

    calc_exit = input("Please enter the 'exit' to end the calculator or just click any button to continue ")
    if calc_exit == 'exit':
        calc_exit = False
    else:
        calc_exit = True
