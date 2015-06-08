import numpy as np

# Basic script to run network state classfication

from loadSeizureData  import LoadSeizureData
from classifierTester import ClassifierTester
from basicFeatures    import BasicFeatures
from randomForestClassifier import RandomForest

dirpath = '/Users/Jonathan/Documents/PhD /Seizure_related/Network_states/VMData/Classified'


dataobj = LoadSeizureData(dirpath)
dataobj.load_data()

basicStatsExtractor = BasicFeatures()
dataobj.extract_feature_array([basicStatsExtractor])

rf = RandomForest(no_trees = 100)
classtester = ClassifierTester(dataobj.features,np.ravel(dataobj.label_colarray), training_test_split = 80)
(score, predictedlabelsprobs, reallabels) = classtester.test_classifier(rf)
print 'training a random forest classifier!'
print score, 'percent correct!'