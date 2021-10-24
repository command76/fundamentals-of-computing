slow = 1000
single_slow = 1000/1000
fast = 1
i = 1
year = 1
#while slow > fast:
while year < 4:
    if year == 1:
        slow = 1000
        fast = 1
        i += 1
    else:
        slow = (slow/slow + 1) * slow
        slow = slow * .6
        fast = (fast/fast + 1) * fast
        fast = fast * .7
        i += 1
    year += 1
    print fast, slow, i
        
    # year 47

# question 3
print (13 * 73), (4 * 98)
print 949 - 36.5, 196 - 49

839.5 245
46
912.5 343

top
1 and 3
bottom
2 and 3

251

45