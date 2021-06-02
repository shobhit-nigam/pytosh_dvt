# mutable
# references 
ave_one = ["hulk", "captain", "ironman", "blackwidow", "black panther"]
ave_two = ave_one

print("ave_one = ", ave_one)
print("ave_two = ", ave_two) 

ave_one.reverse()
ave_one.sort()
ave_one.remove('black panther')
ave_one.append('hawk eye')

print("ave_one = ", ave_one)
print("ave_two = ", ave_two)
