#ask user to input a string
original_string = input("Please write a sentence: ")
# this is our first/future alternative string
alternative_string =""

#make a list which elements are  words from entered sentence
list_of_words = original_string.split(" ")


#first alternative string
#for each word in the sentence 
for word in list_of_words:
    
    #for every letter in the word
    for i in range(0,len(word)):

        if i % 2 == 0:
            #if index is even change a letter to upper case
            alternative_string += word[i].upper()             
        else:
            #change every second letter/odd index to lower case
            alternative_string += word[i].lower()     

    #adding space at the end of each word
    alternative_string += " "

print(alternative_string.strip())


    
#second alternative string
for j in range(0,len(list_of_words)):
    
    if j%2 != 0:
        #change every second word/odd index to upper case
        list_of_words[j] = list_of_words[j].upper()
    else:
        list_of_words[j] = list_of_words[j].lower()

print(" ".join(list_of_words))    









