lin_equation = input("Enter your linear equation in the format [a𝑥+b] where a is the coefficient and b is constant: ")
ran_x = int(input("Enter the range of 𝑥: "))+1
coef = lin_equation.split('x')[0]
print(f"Debug coefficient: {coef}")
cons = lin_equation.split('+')[1]
print(f"Debug constant: {cons}")

#graph
graph_x = []
graph = ""
y = ran_x*int(coef)+int(cons)
# x and y amount of rows print a line that is x characters long y amount of times

#loop y times
for i in range(1, y):
    for i in range(1, ran_x):
        graph_x.append(".")


# table
for i in range(1, ran_x):
    y = i*int(coef)+int(cons)
    print(f"If 𝑥 was {i}, 𝑦 would be: {y}")

print(f"\n{graph_x}")
print(y)
print(ran_x)
