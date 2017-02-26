fruits = "banana apple melon apple"
print (fruits.split())
basket = {}

for fruit in fruits.split():
	basket[fruit] = basket.get(fruit, 0) + 1

print (basket)

sen = "From Carson Leung"

words = sen.split()
print (words)

if 'From' in words:
	print ("Here it is", words[1])
