import csv
import random
import math
import operator

#Function for loading csv file into arrays
def loadDataset(filename,split,trainingSet=[],testSet=[]):
	with open(filename) as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(1, len(dataset)):
			for y in range(15):
				dataset[x][y] = float(dataset[x][y])
			if random.random() < split:	
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])


#Function for calculating the euclidean distance
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
		return math.sqrt(distance)

#KNN Algorithm
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance,trainingSet[x],length)
		distances.append((trainingSet[x],dist))
	distances.sort(key=operator.itemgetter(1))
	neighbours = []
	for x in range(k):
		neighbours.append(distances[x][0])
	return neighbours

#Generate Response
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

#Calculate percentage accuracy
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] is predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0


#Main function
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.67
	loadDataset('credit_train.csv', split, trainingSet, testSet)
	print('Train set: ' + repr(len(trainingSet)))
	print('Test set: ' + repr(len(testSet)))
	# generate predictions
	predictions=[]
	k = 3
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		#print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	
main()