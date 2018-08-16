import csv
import random
def localDataset(filename,Set=[]):
	with open(filename) as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)-1):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])
				Set.append(dataset[x])
trainingSet=[]
testSet=[]
localDataset('credit_train.csv',trainingSet)
localDataset('credit_test.csv',testSet)
print('Train:'+repr(len(trainingSet)))
print('Test:'+repr(len(testSet)))
