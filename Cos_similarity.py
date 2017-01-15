from collections import Counter
import math

threshold = 0.4

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

def length_similarity(c1, c2):
    lenc1 = sum(c1.itervalues())
    lenc2 = sum(c2.itervalues())
    return min(lenc1, lenc2) / float(max(lenc1, lenc2))

def similarity_score(l1, l2):
    c1, c2 = Counter(l1), Counter(l2)
    score_prob=length_similarity(c1, c2) * counter_cosine_similarity(c1, c2)
    print (score_prob)
    if score_prob>threshold:
    	print "still doing work"
    else:
    	print "Fuck you do work"
    	


input_model="algorithms node current shortest path lol"
input_current="shortest node current"

model=input_model.split()
current=input_current.split()

print similarity_score(model,current)