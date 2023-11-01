def find_prime_numbers(ceiling):
    prime_numbers = [2]
    for i in range(2, ceiling+1):
        #print("i", i)
        for j in prime_numbers:
            #print("j", j)
            #print(f"Checking if {i} is divisible by {j}.")
            if i % j == 0:
                if i != j:
                    #print("It is.")
                    #print(prime_numbers)
                    #print()
                    break
                #print("They're the same number.")
                #print(prime_numbers)
                #print()
            else:
                #print("It is not")
                if i not in prime_numbers and j == prime_numbers[-1]:
                    #print("Appending", i)
                    prime_numbers.append(i)
                #print(prime_numbers)
                #print()
    return prime_numbers


print(find_prime_numbers(500))