s = 'Welcome to Python'
print(s.split())

s2 = '2001-12-05'
print(s2.split('-'))

s3 = 'Welcome, to,   Python, and , bla, bla   '
print([x.strip() for x in s3.split(',')])

print(list('Hello, World'))