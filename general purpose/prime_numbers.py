def find_prime_numbers(ceiling):
    prime_numbers = [2]
    for i in range(2, ceiling+1):
        for j in prime_numbers:
            if i % j == 0:
                if i != j:
                    break
            else:
                if i not in prime_numbers and j == prime_numbers[-1]:
                    prime_numbers.append(i)
    return prime_numbers
