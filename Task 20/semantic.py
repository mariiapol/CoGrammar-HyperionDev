# Importing spacy and pandas.
import spacy
import pandas as pd


# Specifying the model we want to use.
nlp = spacy.load('en_core_web_md') 
#nlp = spacy.load('en_core_web_sm') 

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("-------------Words similarity 1--------------")
print(word1.similarity(word2))
print(word2.similarity(word3))
print(word3.similarity(word1))

# Cat and monkey looks to be similar because they are animals.
# The similarity score between monkey and banana is higher than between cat and banana,
# because monkeys are more related to bananas than cats are.


word4 = nlp("dog")
word5 = nlp("cat")
word6 = nlp("kitten")

print("-------------Words similarity 2--------------")
print(word4.similarity(word5))
print(word5.similarity(word6))
print(word6.similarity(word4))


# Cat and kitten looks to be the most similar because kitten is a small cat/ cat gives life to kitten.
# Cat/kitten and dog looks to be similar because they are animals.



print("-------------Working with Vectors---------------")
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))




print("-------------Working with Sentences---------------")
sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my cat go", "Hello, there is my car",
             "I've lost my car in my car", "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - "+ str(similarity)) 

print("-------------Working with Sentences 2---------------")
doc1 = nlp(u'The person wear red T-shirt.')
doc2 = nlp(u'This person is walking.')
doc3 = nlp(u'The boy wear red T-shirt.')


print(doc1.similarity(doc2)) 
print(doc1.similarity(doc3))
print(doc2.similarity(doc3)) 

# Small models, like en_core_web_sm, 
# give less accurate similarity results than big models.
# This is because small models lack word vectors,
# which show word meanings in many dimensions.
# They only have tensors that depend on the context.
# the big model's similarity scores make more sense and vary more, 
# showing the different themes and moods of the sentences.


print("-------------Movie similarity---------------")

# Read the movie data.
df = pd.read_csv('movies.txt', sep=" :", header = None)
#print(df)

# Create a list of movie descriptions
movies = df[1]

# Create a list of movie titles
movies_name = df[0]


# Define the function
def next_movies(description):
    
    model_movie = nlp(description)
    movies_similarity =[]
    for movie in movies:
        if movie != description:
            movies_similarity.append(nlp(movie).similarity(model_movie))
        else:
            # Avoiding 1 for the same movie.
            movies_similarity.append(0)

    # or movies_similarity = 
    #[nlp(movie).similarity(model_movie) if movie != description else 0 for movie in movies]
    #print(movies_similarity)

    # Find the index of the highest similarity.
    movie_index = movies_similarity.index(max(movies_similarity))    
    # Return the recommended movie.  
    return(movies_name[movie_index])
    
print(next_movies('Will he save their world or destroy it? \
                  When the Hulk becomes to dangerous for the Earth, \
                 the illuminati trick into a shuttle and launch him into \
                  space to a planet where the Hulk can leave in peace.\
                 Unfortunately, Hulk land on the planet Sakaar where \
                  he is sold into slavery and trained as a gladiator.'))

