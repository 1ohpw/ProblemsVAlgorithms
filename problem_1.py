def sqrt(number):
   if number < 0:
      raise ValueError("number must be non-negative")

   def sqrt_helper(left, right):
      if left > right:
         return left
      
      lower = (left + right) // 2
      upper = lower + 1
   
      if lower * lower <= number and upper * upper > number:
         return lower
      elif lower * lower > number:
         return sqrt_helper(left, lower - 1)
      else:
         return sqrt_helper(upper, right)
   
   return sqrt_helper(0 , number)


#Test Case 1
print(sqrt(16))
#expected: 4

#Test Case 2
print(sqrt(9))
#expected: 3

#Test Case 3
print(sqrt(27))
#expected: 5

#Test Case 4
print(sqrt(13))
#expected: 3

#Test Case 5
print(sqrt(0))
#expected: 0

#Test Case 6
print(sqrt(1))
#expected: 1

#Test Case 7
print(sqrt(1000000))
#expected: 1000

#Test Case 8
print(sqrt(-4))
#expected: ValueError: number must be non-negative