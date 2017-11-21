def str_reverse(string):
	reversed_str = ''
	string_len = len(string)- 1
	i= string_len
	while i>=0:
		reversed_str = reversed_str + string[i]
		i = i -1
	return reversed_str

def wordwise_reverse(word_list):
	sentence_words = len(word_list) -1
	i = sentence_words
	reversed_sentence = []

	while i >= 0:
		reversed_sentence.append(word_list[i])
		i = i -1
	return reversed_sentence

def make_list(sentence):
	sentence_length = len(sentence)
	space = [" "]
	i = 0
	word_list = []
	while i < sentence_length:
		if sentence[i] not in space:
			word_start = i
			while i < sentence_length and sentence[i] not in space:
				i = i+1
			word_list.append(sentence[word_start:i])
		i = i + 1

	return word_list

def word_reverse(word_list):
	reversed_word_list = []
	for i in word_list:
		reversed_word_list.append(str_reverse(i))
	return reversed_word_list


print(" ".join(wordwise_reverse(make_list("Hello! how are you?"))))
