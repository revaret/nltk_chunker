import nltk #importing nltk module


text  = raw_input("Enter the sentence to be chunked? \n")
tokenised_sentence= nltk.word_tokenize(text); #tokenising the sentence 
tagged_sentence = nltk.pos_tag(tokenised_sentence) #pos_tagging the sentence
result = nltk.chunk.ne_chunk(tagged_sentence) #chunking the sentence
result.draw()

