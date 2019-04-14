from nltk import word_tokenize, pos_tag, ne_chunk
 
sentence = "Mark and John are working at Google."
 
tree = ne_chunk(pos_tag(word_tokenize(sentence)))       # combining word tokenizing, parts of speech tagging, named entity chunking

print(tree)

tree.draw()