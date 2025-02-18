def count_word(sentence,*words):


#splitting the given string in sentence
    word_tokenization=sentence.split()
    
#creating an empty dictionary to store key value pair
    word_dictionary={}

    for word in words:
        word_count=word_tokenization.count(word)
        word_dictionary[word]=word_count

    return word_dictionary



sentence= "I love coding, and coding loves me"
count=count_word(sentence,"love","coding","loves")
print(count)        