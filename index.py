import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

#--------------------------------------
file_contents=open('text.txt', 'r').read()
#print(file_contents)
#--------------------------------------


#--------------------------------------
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text

    uninteresting_words = ["the", "a","in", "on", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",  "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",  "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    #-------------------------------------
    # LEARNER CODE START HERE

    file_without_punctuation=""
    for l in file_contents:
        if l.isalpha()==True or l.isspace():
            file_without_punctuation+=l
    
    file_without_punctuation=file_without_punctuation.split(" ")
    
    file_without_uninteresting_words=[]
    for w in file_without_punctuation:
        if w.lower() not in uninteresting_words and w.isalpha():
            file_without_uninteresting_words.append(w)
    
    
    frequencies={}
    for w in  file_without_uninteresting_words:
        if w not in frequencies:
            frequencies[w]=1
        else:
            frequencies[w]+=1
    



    #---------------------------------------
    #wordcloud

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()
#--------------------------------------
# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()