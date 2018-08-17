import csv
import random
def localTrainDataset(filename,Set=[]):
	with open(filename) as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(1, len(dataset)):
			for y in range(16):
				dataset[x][y] = dataset[x][y]
			Set.append(dataset[x])
def localTestDataset(filename,Set=[]):
	with open(filename) as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(1, len(dataset)):
			for y in range(15):
				dataset[x][y] = dataset[x][y]
			Set.append(dataset[x])
trainingSet=[]
testSet=[]
localTrainDataset('credit_train.csv',trainingSet)
localTestDataset('credit_test.csv',testSet)
print('Train:'+repr(len(trainingSet)))
print('Test:'+repr(len(testSet)))