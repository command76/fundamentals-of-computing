n = 100
numbers = range(2, n)
results = []
i = 0
j = 2

#print numbers
while 0 <= numbers:
#    print i
#    print numbers[i]
    results.append(numbers[i])
    value = results[-1]
#    for j in numbers:
    while j / value % 2 == 0:
        if j < numbers:
#            print value, numbers[j]
#            print "value = " + str(value)
#            print "j = " + str(j)
#        print len(numbers)
#        print float(j/value)
#            print len(results)
            print "popped = " + str(numbers.pop(j))
            j += 1
#        print j
    print len(results)
#    value
    i += 1


#
#for i in range(len(numbers)):
#    results.append(numbers[i])
#    value = results[i]
#    for j in range(len(numbers)):
#        if j / value % 2 == 0:
#            numbers.pop()
#    print len(results)
#    



#for i in numbers:
#    print i
#    results.append(numbers[i])
#    value = results[-1]
##    for j in numbers:
#    while value / numbers[j] % 2 == 0:
#         numbers.pop(j)
##        print j
#    print len(results), len(numbers), i
    

    