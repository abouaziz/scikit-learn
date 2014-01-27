# -*- coding: utf-8 -*-
import _tree
import tree
import random
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


def collectFeaturesFromTopics(topics,featuresToAdd,max_features):
    UsedFeatures=[]
    for topic in topics:
        random.shuffle(topic)
        for i in range(2):
            UsedFeatures.append(topic[i])
    random.shuffle(featuresToAdd)
    featuresNotAssigned= max_features-len(UsedFeatures)
    print "le nombre de caract aleatoire à ajouter est",featuresNotAssigned
    for f in range(featuresNotAssigned):
        UsedFeatures.append(featuresToAdd[f])
    return UsedFeatures



	 


