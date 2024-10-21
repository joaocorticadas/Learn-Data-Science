#a)

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

for x in words:
  print(x + ": " + str(len(x)))

#b)
numbers = [10, 55, 75, 85, 95, 105, 115]

x = 0
while x < len(numbers):
  if numbers[x] >= 100:
    print(numbers[x])
    break
  x = x + 1