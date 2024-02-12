# 1, 2
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13  # 5
generator = square_root_generator(limit)

sum1 = 0
for sqrt_value in generator:
    sum1 += sqrt_value
    print(sqrt_value)

print(sum1)
