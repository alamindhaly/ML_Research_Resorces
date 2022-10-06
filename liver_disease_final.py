# -*- coding: utf-8 -*-
"""Liver Disease Final

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x8atIogp0xaFhtp1Q5eFxhqgFLQFRJ-a
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from google.colab import files
uploaded= files.upload()
df=pd.read_csv('Liver.csv')
df.head(10)

df.info()

df.shape

df.isna().values.any()

df['Selectorfield'].value_counts()

df.loc[df["Selectorfield"]==2,"Selectorfield"]=0
df['Selectorfield'].value_counts()

df.loc[df["gender"]==2,"gender"]=0
df['gender'].value_counts()

#sns.countplot(df['Selectorfield'],label='value')
sns.countplot(df.Selectorfield,palette=["#FF0000","#0000FF"])
#plt.title("[1]----> Secondery Stage  [0]----> Primary Stage"):
plt.ylabel('Combination of two stages values')
plt.xlabel('Predicted_attriute')

df.dtypes

df = df.replace({'Female':1,'Male':0})

df

df.dtypes

"""**Train Test Split**"""

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

#using Pearson Correlation
plt.figure(figsize=(10,10))
cor=df.corr()
sns.heatmap(cor,annot=True,cmap=plt.cm.YlGn_r)
plt.show()

plt.figure(figsize=(10,10))
matrix = np.triu(df.corr())
sns.heatmap(df.corr(), annot=True, mask=matrix)

"""**FILE IMPORT**"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
digits= load_digits()

pip install vaex

"""**MODELS**"""

def models(x_train,y_train):
  #Random Forest         0
  forest=RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
  forest.fit(x_train,y_train)

  #Gradient Boosting     1   
  gb_clf=GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,random_state=40,criterion='mse',verbose= 2,warm_start= 'bool')
  gb_clf.fit(x_train,y_train)

                       
  #k-Nearest Neighbors  2
  classifier = KNeighborsClassifier(n_neighbors=8)
  classifier.fit(x_train,y_train)


  #Adaboost Classifier   3
  clf = AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', random_state=60)
  clf.fit(x_train,y_train)
 
  print('[0]Random Forest Training Accuracy:',forest.score(x_train,y_train))
  print('[1]Gradient Boosting Training Accuracy:',gb_clf.score(x_train,y_train))
  print('[2]k-Nearest Neighbors Training Accuracy:',classifier.score(x_train,y_train))
  print('[3]Adaboost Classifier Training Accuracy:',clf.score(x_train,y_train))

  return forest,gb_clf,classifier,clf

model = models(x_train, y_train)                       #model fitting

"""**Confusion Matrix**"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# df
# from sklearn.metrics import confusion_matrix,classification_report,log_loss,cohen_kappa_score
# from sklearn import metrics
# for i in range (len(model)):
#   print('confusion matrix of model',i,'is:')
#   cm=confusion_matrix(y_test,model[i].predict(x_test))
#   TP=cm[0][0]
#   TN=cm[1][1]
#   FP=cm[0][1]
#   FN=cm[1][0]
#   print(cm)
#   print()
#   result1=classification_report(y_test,model[i].predict(x_test))
#   print("Classification report:",)
#   print(result1)
#   print()
#   var=((TP+TN)/(TP+TN+FP+FN))*100
#   print('testing accuracy:',var)
#   print('Sensitivity/recall:',TP/(TP+FN))
#   print('Precision : ', TP/(TP+FP))
#   print('F1 Score: ', (2*(TP/(TP+FN))*(TP/(TP+FP)))/(TP/(TP+FN))+(TP/(TP+FP)))
#   print('Specificity:',TN/(TN+FP))
#   print('false positive rate:',FP/(FP+TN))
#   print('False negative:',FN/(FN+TP))
#   print('Negative Peridictive Value:',TN/(TN+FN))
#   print('False Discovery rate:',FP/(TP+FP))
#   print('Mean Absolute Eror:',metrics.mean_absolute_error(y_test,model[i].predict(x_test)))
#   print('Mean Squared Error:',metrics.mean_squared_error(y_test,model[i].predict(x_test)))
#   print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,model[i].predict(x_test))))
#   print('log_loss:',metrics.log_loss(y_test,model[i].predict(x_test)))
#   print('Çohen_Kappa_Scorer:',cohen_kappa_score(y_test,model[i].predict(x_test)))
#   
#   print()
#   print()
#   name=['RandomForestClassifier','GradientBoostingClassifier','KNeighborsClassifier','AdaBoostClassifier']
#   col_value=['blue','green','purple','red']
#   model_accuracy=pd.Series(data=(var),index=[name[i]])
#   fig=plt.figure(figsize=(5,5))
#   width=0.75
#   model_accuracy.sort_values().plot.bar(alpha=0.8,color=[col_value[i]])
#   plt.xticks(rotation=0)
#   plt.title('model Accuracy')
#   plt.ylabel('Accuracy(%)')
#   plt.show()
#   print()
#   print()

"""**Voting**"""

from sklearn.ensemble import VotingClassifier

from sklearn import metrics

R = RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
G = GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,random_state=40,criterion='mse',verbose= 2,warm_start= 'bool')
K=KNeighborsClassifier(n_neighbors=8)
A=AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', random_state=60)
evc = VotingClassifier(estimators=[('R',R),('G',G),('K',K),('A',A)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)


ypred0 = evc.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred0, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**AUC & ROC CURVE**

**KNeighborsClassifier**
"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#KNeighborsClassifier Roc Curve 
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=8)
classifier.fit(x_train,y_train)
y_score1 = classifier.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of KNeighborsClassifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('KNeighborsClassifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "KNeighborsClassifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#KNeighborsClassifier AUC Curve
classifier = KNeighborsClassifier(n_neighbors=8)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = classifier.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('KNC Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**RandomForestClassifier**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#RandomForestClassifier Roc Curve 
from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
forest.fit(x_train,y_train)
y_score1 = forest.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of RandomForestClassifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('RandomForestClassifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "RandomForestClassifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#RandomForestClassifier AUC Curve
forest = RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
forest.fit(x_train,y_train)
y_pred = forest.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = forest.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('RandomForestClassifier Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**Gradient Boosting**

"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Gradient Boosting Roc Curve 
gb_clf=GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,random_state=40,criterion='mse',verbose= 2,warm_start= 'bool')
gb_clf.fit(x_train,y_train)
y_score1 = gb_clf.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of Gradient Boosting: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('Gradient Boosting Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "Gradient Boosting")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#Gradient Boosting AUC Curve
gb_clf=GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,random_state=40,criterion='mse',verbose= 2,warm_start= 'bool')
gb_clf.fit(x_train,y_train)
y_pred = gb_clf.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = gb_clf.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('Gradient Boosting Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**Adaboost classifier**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Adaboost classifier Roc Curve 
clf = AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', random_state=60)
clf.fit(x_train,y_train)
y_score1 = clf.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of AdaBoost Classifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('AdaBost classifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "AdaBoost Classifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#AdaBoost Classifier AUC Curve
clf = AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', random_state=60)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = clf.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('KNC Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**Bagging 1**"""

from sklearn.ensemble import BaggingClassifier
bg=BaggingClassifier(RandomForestClassifier(n_estimators=5,criterion = 'entropy', random_state=10),max_samples=0.5,
                     max_features=7,n_estimators=20)

bg.fit(x_train,y_train)

bg.score(x_test,y_test)

ypred5 = bg.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred5, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**RF AUC & ROC test**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#RandomForestClassifier Roc Curve 
from sklearn.ensemble import RandomForestClassifier
bg=BaggingClassifier(RandomForestClassifier(n_estimators=5,criterion = 'entropy', random_state=10),max_samples=0.5,
                     max_features=7,n_estimators=20)
bg.fit(x_train,y_train)
y_score1 = bg.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of RandomForestClassifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('RandomForestClassifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "RandomForestClassifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#RandomForestClassifier AUC Curve
bg=BaggingClassifier(RandomForestClassifier(n_estimators=5,criterion = 'entropy', random_state=10),max_samples=0.5,
                     max_features=7,n_estimators=20)
bg.fit(x_train,y_train)
y_pred = bg.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = bg.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('RandomForestClassifier Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**2**"""

bg1 = BaggingClassifier(GradientBoostingClassifier ( n_estimators=20,loss= 'deviance', max_features=1,learning_rate= 0.2,random_state=60,
                                                    criterion='mse',verbose= 2,warm_start= 'bool'))
bg1.fit(x_train,y_train)

bg1.score(x_test,y_test)

ypred6 = bg1.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred6, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**GB AUC & ROC test**"""

#Gradient Boosting Roc Curve 
from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Gradient Boosting AUC Curve
bg1 = BaggingClassifier(GradientBoostingClassifier ( n_estimators=20,loss= 'deviance', max_features=1,learning_rate= 0.2,random_state=60,
                                                    criterion='mse',verbose= 2,warm_start= 'bool'))
bg1.fit(x_train,y_train)
y_pred = bg1.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = bg1.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('Gradient Boosting Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()
gb_clf.fit(x_train,y_train)
y_score1 = gb_clf.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of Gradient Boosting: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('Gradient Boosting Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "Gradient Boosting")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#Gradient Boosting AUC Curve
bg1 = BaggingClassifier(GradientBoostingClassifier ( n_estimators=20,loss= 'deviance', max_features=1,learning_rate= 0.2,random_state=60,
                                                    criterion='mse',verbose= 2,warm_start= 'bool'))
bg1.fit(x_train,y_train)
y_pred = bg1.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = bg1.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('Gradient Boosting Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**3**"""

bg2 = BaggingClassifier(AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME',
                                           random_state=60))
bg2.fit(x_train,y_train)

bg2.score(x_test,y_test)

ypred7 = bg2.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred7, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**AB AUC & ROC test**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Adaboost classifier Roc Curve 
bg2 = BaggingClassifier(AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME',
                                           random_state=60))
bg2.fit(x_train,y_train)
y_score1 = bg2.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of AdaBoost Classifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('AdaBost classifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "AdaBoost Classifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#AdaBoost Classifier AUC Curve
bg2 = BaggingClassifier(AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME',
                                           random_state=60))
bg2.fit(x_train,y_train)
y_pred = bg2.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = bg2.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('KNC Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**4**"""

bg3 = BaggingClassifier(KNeighborsClassifier(n_neighbors=8))
bg3.fit(x_train,y_train)

bg3.score(x_test,y_test)

ypred8 = bg3.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred8, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**KNN AUC & ROC test**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#KNeighborsClassifier Roc Curve 
from sklearn.neighbors import KNeighborsClassifier
bg3 = BaggingClassifier(KNeighborsClassifier(n_neighbors=8))
bg3.fit(x_train,y_train)
y_score1 = bg3.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of KNeighborsClassifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('KNeighborsClassifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "KNeighborsClassifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#KNeighborsClassifier AUC Curve
bg3 = BaggingClassifier(KNeighborsClassifier(n_neighbors=8))
bg3.fit(x_train,y_train)
y_pred = bg3.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = classifier.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('KNC Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**Boosting 1**"""

from sklearn.ensemble import AdaBoostClassifier
bos=AdaBoostClassifier(AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', 
                                          random_state=60),n_estimators=10)
bos.fit(x_train,y_train)

bos.score(x_test,y_test)

ypred9 = bos.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred9, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**AB AUC & ROC test**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Adaboost classifier Roc Curve 
bos=AdaBoostClassifier(AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', 
                                          random_state=60),n_estimators=10)
bos.fit(x_train,y_train)
y_score1 = bos.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of AdaBoost Classifier: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('AdaBost classifier Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "AdaBoost Classifier")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#AdaBoost Classifier AUC Curve
bos=AdaBoostClassifier(AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1.75, algorithm='SAMME', 
                                          random_state=60),n_estimators=10)
bos.fit(x_train,y_train)
y_pred = bos.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = bos.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('KNC Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**2**"""

bos1=AdaBoostClassifier(GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,
                                                    random_state=40,criterion='mse',verbose= 2,warm_start= 'bool'),n_estimators=12)
bos1.fit(x_train,y_train)

bos1.score(x_test,y_test)

ypred10 = bos1.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred10, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**GB AUC & ROC test**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Gradient Boosting Roc Curve 
bos1=AdaBoostClassifier(GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,
                                                    random_state=40,criterion='mse',verbose= 2,warm_start= 'bool'),n_estimators=12)
bos1.fit(x_train,y_train)
y_score1 = bos1.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of Gradient Boosting: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('Gradient Boosting Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "Gradient Boosting")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#Gradient Boosting AUC Curve
bos1=AdaBoostClassifier(GradientBoostingClassifier ( n_estimators=30,loss= 'deviance', max_features=1,learning_rate= 0.1,
                                                    random_state=40,criterion='mse',verbose= 2,warm_start= 'bool'),n_estimators=12)
bos1.fit(x_train,y_train)
y_pred = bos1.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = bos1.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('Gradient Boosting Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**Stacking 1**"""

from sklearn.linear_model import LogisticRegression
from mlxtend.classifier import StackingClassifier

clf1=GradientBoostingClassifier ( n_estimators=20,loss= 'deviance', max_features=1,learning_rate= 0.50,random_state=40,criterion='mse',verbose= 2,warm_start= 'bool')
clf2=KNeighborsClassifier(n_neighbors=8)
clf3=RandomForestClassifier(n_estimators=5,criterion = 'entropy', random_state=10)
clf4=AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1, algorithm='SAMME', random_state=60)
log=LogisticRegression(random_state=42 )
sclf=StackingClassifier(classifiers=[clf1,clf2,clf3,clf4],use_probas=True,meta_classifier=log)

sclf.fit(x_train,y_train)

sclf.score(x_test,y_test)

ypred11 = sclf.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred11, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""#AUC ROC FOR STACKING"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Gradient Boosting Roc Curve 
sclf=StackingClassifier(classifiers=[clf1,clf2,clf3,clf4],use_probas=True,meta_classifier=log)
sclf.fit(x_train,y_train)
y_score1 = sclf.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of Stacking: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('Stacking Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "Stacking")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#Gradient Boosting AUC Curve
sclf=StackingClassifier(classifiers=[clf1,clf2,clf3,clf4],use_probas=True,meta_classifier=log)
sclf.fit(x_train,y_train)
y_pred = sclf.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = sclf.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('Stacking Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()

"""**Hyper parameter tuning using grid search cv 2**"""

param_grid = {  'bootstrap': [True],'max_depth': [5, 10, None], 'max_features': ['auto', 'log2'], 'n_estimators': [5, 6, 7, 8, 9, 10, 11, 12, 13, 15]}

rfc=RandomForestClassifier(random_state=30)

g_search = GridSearchCV(estimator = rfc, param_grid = param_grid,cv = 15, n_jobs = 1, verbose = 0, return_train_score=True)

g_search.fit(x_train, y_train);
g_search.cv_results_

print(g_search.best_params_)

print(g_search.score(x_test, y_test))

df = pd.DataFrame(g_search.cv_results_)
df

df[['mean_test_score']]

dir(g_search)

g_search.best_score_