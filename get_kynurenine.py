#! /usr/bin/env python

import os,sys
from pymed import PubMed
import nltk
import subprocess

#dictionary source and duplication were removed
#https://www.medo.jp/ben.htm
#https://www.mayoclinic.org/diseases-conditions/index
#https://www.health.harvard.edu/a-through-c
#https://icd.who.int/browse10/2016/en

disease_dict = []
with open("./disease_dict.tsv", "r") as f:
    lines = f.read().split("\n")
    for line in lines:
        if line == "":
            continue
        buf = line.split("\t")
        disease_dict.append(buf[0])

#word = "kynurenine"
word = "AMINOACYL-TRNA BIOSYNTHESIS"

pubmed = PubMed(tool="MyTool", email="aaa@gmail.com")
results = pubmed.query(word, max_results=10000)

debug = open("./debug.txt", "w")

result_count = {}
result_file = open("./result_count.txt", "w")


for item in results:
    #print (item.doi)
    #print (item.keywords)
    #print (item.abstract)
    abst = item.abstract
    
    if abst is None:
        continue
    
    ##debug.write("doi: "+str(item.doi)+"\n")
    ##debug.write("abst: "+str(item.abstract)+"\n")
    #debug.write("keywords: "+",".join(item.keywords)+"\n")

    #words = nltk.word_tokenize(abst)
    #clean_words = []
    #postag = nltk.pos_tag(words)
    #for pos in postag:
    #    if pos[1].find("JJ") != -1 or pos[1].find("NN") != -1:
    #        clean_words.append(pos[0])

    #bigrams = nltk.bigrams(clean_words)
    #for w in bigrams:
    #    print (w)
    #    bi_word = " ".join(w)
    #    if bi_word in disease_dict:
    #        debug.write("a:  "+item.pubmed_id+"\n")
    #        debug.write(bi_word+"\n")
    #        debug.write(abst+"\n")

    for disease in disease_dict:
        if (disease.lower() in abst.lower()):
            ##debug.write("disease: "+disease+"\n")
            if not disease in result_count:
                result_count[disease] = 1
            else:
                result_count[disease] += 1

            #if disease == "cancer":
            #    debug.write(disease+"\n")
            #    debug.write(abst+"\n")
            #    debug.write("----------\n")

    ##debug.write("--------------\n")


result_count_sorted = sorted(result_count.items(), key=lambda x:-x[1])

for buf in result_count_sorted:
    disease = buf[0]
    count = buf[1]
    result_file.write(disease+","+str(count)+"\n")


result_file.close()
debug.close()
