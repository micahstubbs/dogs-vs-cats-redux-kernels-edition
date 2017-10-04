# https://stackoverflow.com/questions/39210765/randomly-distribute-files-into-train-test-given-a-ratio
import os
from sklearn.cross_validation import train_test_split
X = y= os.listdir('data/train1')
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.25, random_state=0)

for x in X_train:
	os.rename('data/train1/'+x , 'data/train/'+x)	

for x in X_valid:
	os.rename('data/train1/'+x, 'data/valid/'+x)