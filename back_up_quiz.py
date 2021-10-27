n  = 100
numbers = range(2, n)
results = []
while numbers:
    i = numbers[0]
    results.append(i)
    for number in numbers:
        if number % i == 0:
            numbers.remove(number)
 
print numbers
print len(results)

#=================================

n = 1000
numbers = range(2, n)
results = []
j = 2

while numbers:
    results.append(numbers[0])
    value = results[-1]
    for j in numbers:
        if j % value == 0:
         numbers.remove(j)
print len(results), j