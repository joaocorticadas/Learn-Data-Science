def filter_even_numbers(numbers_list):
  result = []
  for x in numbers_list:
    if x % 2 == 0:
      result.append(x)

  return result

test = [1, 2, 3, 4, 5, 6]

print(filter_even_numbers(test))