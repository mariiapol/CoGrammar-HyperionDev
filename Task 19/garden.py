import spacy
# Load the model and assign it to the variable.
nlp = spacy.load("en_core_web_sm")


gardenpathSentences = ["Amelia Earhart flies, like, a plane.", "The tycoon sold the offshore oil tracts for a lot of money wanted to kill JR.",
"British left waffles on Falklands."]

# Add 3 given sentences to the list.
gardenpathSentences.append("Mary gave the child the dog bit a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")

for sentence in gardenpathSentences:
    doc = nlp(sentence)

    print(f"Sentence: {sentence}")

    # Tokenization.
    print("Tokenization:")
    print([token.orth_ for token in doc])
    print([(token, token.orth_, token.orth) for token in doc])

    # Named entity recognition.
    print("Named entity recognition:")
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


# Get an explanation of an entity and print it.
entity_fac = spacy.explain("GPE")
print(f"GPE:{entity_fac}")

entity_fac = spacy.explain("ORG")
print(f"ORG:{entity_fac}")

entity_fac = spacy.explain("NORP")
print(f"NORP:{entity_fac}")


'''Mississippi / GPE:Countries, cities, states. It make sense.

Falklands / ORG:Companies, agencies, institutions, etc. 
I think it should be Geopolitical entity, i.e. countries, cities, states because The Falklands are a group of islands in the South Atlantic Ocean.

British / NORP:Nationalities or religious or political groups. It make sense.'''
