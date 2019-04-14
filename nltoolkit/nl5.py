import nltk

Alchemist = """The boy's name was Santiago . Dusk was falling as the boy arrived with his herd at an abandoned
church. The roof had fallen in long ago, and an enormous sycamore had grown on the spot where the
sacristy had once stood."""



words = nltk.word_tokenize(Alchemist)            #Tokenizing the sentences to form a list of words
tagged_words = nltk.pos_tag(words)              #tagging each words by it's parts of speech
namedEntity = nltk.ne_chunk(tagged_words)       #tagging each named entity
namedEntity.draw()                              #drawing the tree 
    
    
