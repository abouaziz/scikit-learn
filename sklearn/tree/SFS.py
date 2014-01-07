# -*- coding: utf-8 -*-
import _tree
import tree
#trouver le topic le plus proche d'un mot       
def findSemanticWord(word,topics,threshold=0):
    
    maxWeight = 0
    topicChoisi = 0
    listmotAajouter = []
           
    for topic in topics:
       for m in topic.keys():
            listMotsDansTopic = topic[m]
                
            try:
                    
                for mot in listMotsDansTopic:
                    if word== mot:
                       if maxWeight < m:
                            maxWeight = m
                            topicChoisi = topic  
			    break;
            except:
                print("Comparaison impossible")
    
    
    if(maxWeight>0):
        for j in topicChoisi.keys():
	     if(j>threshold):
	     	  listmotAajouter = listmotAajouter + topicChoisi[j]
                  
    if not listmotAajouter:
	listmotAajouter.append(word)
    
    return listmotAajouter





