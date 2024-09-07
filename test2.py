import math
import 

def mean(raw_scores):
    return sum(raw_scores)/len(raw_scores)
def standard_deviation(raw_scores, mean):
    return math.sqrt(sum((x - mean) ** 2 for x in raw_scores) / len(raw_scores))
def z_scores(raw_scores, mean, standard_dev):
    z_scores = []
    z_scores.append(((x - mean) / standard_dev) for x in raw_scores) 
    return z_scores

