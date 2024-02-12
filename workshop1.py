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


# 3
ages = 0

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)
    ages += person["Age"]


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
    print(person)
    ages += person["Age"]

print(ages)

# 4.
ages = {}

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)
    ages[person["ID"]] = person["Age"]


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
    print(person)
    ages[person["ID"]] = person["Age"]

a_sum = 0
for i in ages:
    a_sum += ages[i]

print(a_sum)
