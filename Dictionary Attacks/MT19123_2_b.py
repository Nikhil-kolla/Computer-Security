#Rference for accessing one python file in another
#https://www.geeksforgeeks.org/python-call-function-from-another-file/

from MT19123_2_a import *

#Reference for reading file line by line
#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

file1 = open('words_alpha.txt', 'r') 
Lines = file1.readlines()


def dictionaryAttack(len1,Lines):
	same_len_words = []
	for line in Lines:
		if(len(line)-1==len1):
			same_len_words.append(line[:-1])

	final_list = []
	for word in same_len_words:
		final_list.append(encrypt(word))

	print(len(final_list))
	output = open('final_passwords.txt', 'w') 
	for word in final_list:
		output.write(word+"\n") 
	output.close() 


dictionaryAttack(17,Lines)

