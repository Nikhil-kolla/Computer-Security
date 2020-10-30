
#Reference for changing the list into string
#https://www.geeksforgeeks.org/python-convert-list-characters-string/
def convert(l):
	new_string = ""
	for x in l:
		new_string+=x
	return new_string

def encrypt(str):
	s = list(str)
	for i in range(0,len(s)):
		n = ord(s[i])
		if(i%2==0):
			c = chr(n+i)
			s[i]=c
		else:
			c = chr(n-i)
			s[i]=c
	return convert(s)

str = input("Enter the password: ")
print(encrypt(str))