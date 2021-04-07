"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []
final = []
def main():
	"""
	TODO:
	"""
	read_dictionary()
	temp = ''
	word_lst = []
	for i in range(4):

		while True:
			row = input(str(i + 1) + ' row of letters: ')
			ch = row.split()
			if len(ch)!= 4 or len(ch[0])!=1 or len(ch[1])!=1 or len(ch[2])!=1 or len(ch[3])!=1:
				print('illegal input')
			else:
				break
		for j in range(4):
			word_lst.append(ch[j])

	for start in range(16):
		temp = word_lst[start]
		word_lst[start] = ''

		find_word(word_lst,[temp],start)
		word_lst[start] = temp
	print(f'There are {len(final)} words in total.')


def find_word(word_lst,current,now):

	if now == 0 or now ==4 or now == 8 or now == 12:
		nums = [-4,-3,1,4,5,1000]
	elif now ==1 or now ==5 or now ==9 or now ==13 or now ==2 or now ==6 or now ==10 or now ==14 :
		nums = [-5, -4, -3, -1, 1, 3, 4, 5,1000]
	elif now == 3 or now == 7 or now == 11 or now ==15:
		nums =[-5,-4,-1,3,4,1000]

	# print(current)



	temp = ''
	temp2 = ''
	a = ''
	for word in current:
		a+=word
	for dict in dict_list:
		if len(dict)>=4:
			if dict == a:
				if a not in final:
					final.append(a)
					print('Found "'+a+'"')

	for num in nums:
		# credential = 0
		# if 16 > (now+num) > 0:
		# 	if word_lst[now+num] != '':
		# 		credential = 1
		# if credential == 0:
		# 	pass
		# print(num)
		if num > 100:
			break
		else:
			# for num in nums:
			# print('now:',now)
			# print(num)
			# print(word_lst,current)
			if 0 <= now + num < 16:
				if word_lst[now+num] != '':
					temp=''
					for ch in current:
						temp += ch
					# print(word_lst)
					# print(temp+word_lst[now+num])
					if has_prefix(temp+word_lst[now+num]):
						current.append(word_lst[now+num])
						temp2 = word_lst[now+num]
						word_lst[now+num] = ''
						find_word(word_lst,current,now+num)
						word_lst[now+num] = temp2
						current.pop()
						# print('--')
						# print(word_lst)
						# print(current)
						# print('--')

'roof coif hoof '







	# nums = [-5,-1,-1,-1,1,3,4,5]
	# a = 0
	# temp=''
	# sub=''
	# a=''
	# for ch in word_lst:
	# 	if ch != '':
	# 		a =1
	# if a == 0:
	# 	print(current)
	# else:
	# 	for i in range(16):
	# 		if word_lst[i] != '':
	# 			current.append(word_lst[i])
	# 			a = word_lst[i]
	# 			word_lst[i] = ''
	# 			for num in nums:
	# 				if 0 < i+num < 16:
	# 					if word_lst[i+num] != '':
	# 						for ch in current:
	# 							temp += ch
	# 						if has_prefix(temp+word_lst[i+num]):
	# 							print('-----------')
	# 							print(temp+word_lst[i+num])
	# 							print('-----------')
	# 							current.append(word_lst[i+num])
	# 							sub = word_lst[i+num]
	# 							word_lst[i+num] = ''
	# 							find_word(word_lst,current)
	# 						else:
	# 							word_lst[i+num] = ''
	# 						if len(current)!=0:
	# 							current.pop()
	# 						word_lst[i+num] = sub
	# 			word_lst[i] = a
	# 			if len(current) != 0:
	# 				current.pop()
	# 		print(i)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			dict_list.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
