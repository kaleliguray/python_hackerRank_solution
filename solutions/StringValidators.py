s = input()

print("alphanumeric",any(a.isalnum() for a in s))
print("alphabetical",any(a.isalpha() for a in s))
print("digits",any(a.isdigit() for a in s))
print("lowercase",any(a.islower() for a in s))
print("uppercase",any(a.isupper() for a in s))
