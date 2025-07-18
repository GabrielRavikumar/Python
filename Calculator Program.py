#calculator program
operator=input("Enter the operator (+, -, *, /, %) : ")
input1=float(input("Enter the first number : "))
input2=float(input("Enter the second number : "))
result=0
if operator=="+":
    result=input1 + input2
if operator == "-":
    result = input1 - input2
if operator == "*":
    result = input1 * input2
if operator == "/":
    result = input1 / input2
if operator == "%":
    result = input1 % input2
print(result)