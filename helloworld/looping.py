primes = [2, 3, 5, 7]
for number in primes:
    print(number)

for i in range(5):
    print(i)

for x in range(1,99,2):
    print(x)

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

'''
Task 
Read an integer N . For all non-negative integers , print i2. See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .
'''

if __name__ == '__main__':
    n = int(input())
    if(n>1 and n<20):
        for i in range(n):
            print(i ** 2)