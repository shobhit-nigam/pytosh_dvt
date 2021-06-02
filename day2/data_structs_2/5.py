# mutable lists
# immutable tuples

ave_one = ["hulk", "captain", "ironman", "blackwidow", "black panther"]
ave_two = ("hulk", "captain", "ironman", "blackwidow", "black panther")

print("ave_one = ", ave_one)
print("ave_two = ", ave_two)

print("type of ave_one = ", type(ave_one))
print("type of ave_two = ", type(ave_two))

# error 
ave_two[3] = 'wanda'
