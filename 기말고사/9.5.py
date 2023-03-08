s1= '    Hello World!   '
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

s2 = '########this is an example############'
print(s2.strip('#'))
print(s2.lstrip('#'))
print(s2.rstrip('#'))
print(s2.strip('#').capitalize())


s3 = 'Hello, World!'
print(s3.lower())
print(s3.upper())

s4 = 'www.booksr.co.kr'
print(s4.count('.'))
print(s4.find('kr'))
print(s4.find('x'))
