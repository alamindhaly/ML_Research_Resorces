# -*- coding: utf-8 -*-
"""Copy of Fetal Health 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e0KOkKBUj7YK_HM-F-0Wp57mtq04VMsU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from google.colab import files
uploaded= files.upload()
df=pd.read_csv('fetal_health.csv')
df.head(10)

df.info()

df.shape

df.isna().values.any()

df['fetal_health'].value_counts()

#sns.countplot(df['Selectorfield'],label='value')
sns.countplot(df.fetal_health,palette=["#6A1B4D","#35BDD0","#50DBB4"])
#plt.title("[1]----> Secondery Stage  [0]----> Primary Stage"):
plt.ylabel('Combination of two stages values')
plt.xlabel('Predicted_attriute')

df.dtypes



# copy the data
df_min_max_scaled = df.copy()
  
# apply normalization techniques
for column in df_min_max_scaled.columns:
    df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())    
  
# view normalized data
print(df_min_max_scaled)

df=df_min_max_scaled
df

df=(df*10000)
df

df = df.astype(int)
df

df

"""**Feature Selection**

# **Univariate Selection**
"""

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

#apply SelectionKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2,k=21)
fit = bestfeatures.fit(x,y)

dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(x.columns)

#concat two dataframes for better visualization
featurescore = pd.concat([dfcolumns,dfscores],axis=1)
featurescore.columns = ['Specs','Score']   #mapping the dataframe columns

featurescore

print(featurescore.nlargest(50,'Score'))    #print 10 best feature

"""**Feature Importance**"""

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(x,y)

#use inbuilt class feature_importance of tree based classifiers
print(model.feature_importances_)

#plot graph of feature importances for better visualization
feat_importance = pd.Series(model.feature_importances_,index=x.columns)
feat_importance.nlargest(50).plot(kind='barh')
plt.show()

df.corr()

x1=df.iloc[:,:-1].values
y1=df.iloc[:,-1].values
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x1,y1,test_size=0.20,random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

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

def models(x_train,y_train):
 #Logistic Regression    0
  log = LogisticRegression(random_state=42 ) 
  log.fit(x_train,y_train)

  #Random Forest         1
  forest=RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
  forest.fit(x_train,y_train)

                         
  # Decision tree        2
  tree = DecisionTreeClassifier(criterion = 'entropy', max_depth=1, random_state=42)
  tree.fit(x_train,y_train)

                       
                        
  #Gradient Boosting     3   
  gb_clf=GradientBoostingClassifier ( n_estimators=30,max_features=1,random_state=42)
  gb_clf.fit(x_train,y_train)

                        
  #Support Vector Machines  4
  svm = SVC(kernel= 'sigmoid',C=30, gamma=100)
  svm.fit(x_train,y_train)

                       
  #k-Nearest Neighbors  5
  classifier = KNeighborsClassifier(n_neighbors=8)
  classifier.fit(x_train,y_train)

                      
  #Adaboost Classifier   6
  clf = AdaBoostClassifier(n_estimators=100, random_state=30)
  clf.fit(x_train,y_train)

                     
  #Gaussian            7
  gause_clf = GaussianNB()
  gause_clf.fit(x_train,y_train)

                     
  #Gradient Bosting    8
  gb_clf = GradientBoostingClassifier(max_features=2, max_depth=2, random_state=0)
  gb_clf.fit(x_train,y_train)

                    
  #GridSearch CV       9
  #cv=GridSearchCV(log,param,cv=5,n_jobs=-1)
  #cv.fit(x_train,y_train)

                   
  #XGBclassifier      10
  xgb =XGBClassifier(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                     max_depth = 5, alpha = 10, n_estimators = 10)
  xgb.fit(x_train, y_train)


  print('[0]Logistic Regression Training Accuracy:',log.score(x_train,y_train))
  print('[1]Random Forest Training Accuracy:',forest.score(x_train,y_train))
  print('[2]Decision tree Training Accuracy:',tree.score(x_train,y_train))
  print('[3]Gradient Boosting Training Accuracy:',gb_clf.score(x_train,y_train))
  print('[4]Support Vector Machines Training Accuracy:',svm.score(x_train,y_train))
  print('[5]k-Nearest Neighbors Training Accuracy:',classifier.score(x_train,y_train))
  print('[6]Adaboost Classifier Training Accuracy:',clf.score(x_train,y_train))
  print('[7]Gaussian Training Accuracy:',gause_clf.score(x_train,y_train))
  print('[8]Gradient Bosting Training Accuracy:',gb_clf.score(x_train,y_train))
  #print('[9]GridSearch CV Training Accuracy:',cv.score(x_train,y_train))
  print('[9]XGBclassifier Training Accuracy:',xgb.score(x_train,y_train))

  return log,forest,tree,gb_clf,svm,classifier,clf,gause_clf,gb_clf,xgb

model = models(x_train, y_train)

from sklearn.metrics import confusion_matrix,classification_report,log_loss,cohen_kappa_score
from sklearn import metrics
for i in range (len(model)):
  print('confusion matrix of model',i,'is:')
  cm=confusion_matrix(y_test,model[i].predict(x_test))
  TP=cm[0][0]
  TN=cm[1][1]
  FP=cm[0][1]
  FN=cm[1][0]
  print(cm)
  print()
  result1=classification_report(y_test,model[i].predict(x_test))
  print("Classification report:",)
  print(result1)
  print()
  var=((TP+TN)/(TP+TN+FP+FN))*100
  print('testing accuracy:',var)
  print('Sensitivity:',TP/(TP+FN))
  print('Specificity:',TN/(TN+FP))
  print('false positive rate:',FP/(FP+TN))
  print('False negative:',FN/(FN+TP))
  print('Negative Peridictive Value:',TN/(TN+FN))
  print('False Discovery rate:',FP/(TP+FP))
  print('Mean Absolute Eror:',metrics.mean_absolute_error(y_test,model[i].predict(x_test)))
  print('Mean Squared Error:',metrics.mean_squared_error(y_test,model[i].predict(x_test)))
  print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,model[i].predict(x_test))))
  #print('log_loss:',metrics.log_loss(y_test,model[i].predict(x_test)))
  print('??ohen_Kappa_Scorer:',cohen_kappa_score(y_test,model[i].predict(x_test)))
  
  print()
  print()
  name=['LogisticRegression','RandomForestClassifier','DecisionTreeClassifier','GradientBoostingClassifier','SVC','KNeighborsClassifier'
        ,'AdaBoostClassifier','GaussianNB','GradientBoostingClassifier','GridSearchCV','XGBClassifier']
  col_value=['blue','green','purple','blue','green','purple','green','blue','purple','blue','green','blue']
  model_accuracy=pd.Series(data=(var),index=[name[i]])
  fig=plt.figure(figsize=(5,5))
  width=0.75
  model_accuracy.sort_values().plot.bar(alpha=0.8,color=[col_value[i]])
  plt.xticks(rotation=0)
  plt.title('model Accuracy')
  plt.ylabel('Accuracy(%)')
  plt.show()
  print()
  print()



#using Pearson Correlation
plt.figure(figsize=(100,100))
cor=df.corr()
sns.heatmap(cor,annot=True,cmap=plt.cm.Blues)
plt.show()



"""#**Ensemble Method**

#**Voting Classifier**
"""

from sklearn.ensemble import VotingClassifier

G = GradientBoostingClassifier ( n_estimators=30,max_features=1,random_state=42)
K= KNeighborsClassifier(n_neighbors=8)
R = RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
X = XGBClassifier(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,max_depth = 5, alpha = 10, n_estimators = 10)
D = DecisionTreeClassifier(criterion = 'entropy', max_depth=1, random_state=42)
L = LogisticRegression(random_state=42 )
A = AdaBoostClassifier(n_estimators=100, random_state=30) 
evc = VotingClassifier(estimators=[('G',G),('K',K),('R',R),('X',X),('D',D),('L',L),('A',A)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)



"""#**BAGGING**"""

from sklearn.ensemble import BaggingClassifier
bg=BaggingClassifier(RandomForestClassifier(n_estimators=5,criterion='entropy',random_state=30),max_samples=0.5,
                     max_features=7,n_estimators=20)

bg.fit(x_train,y_train)
bg.score(x_test,y_test)

from sklearn.ensemble import BaggingClassifier
bg1=BaggingClassifier(LogisticRegression(random_state=42 ) )

bg1.fit(x_train,y_train)
bg1.score(x_test,y_test)

bg2=BaggingClassifier(DecisionTreeClassifier(criterion = 'entropy', max_depth=1, random_state=42) )

bg2.fit(x_train,y_train)
bg2.score(x_test,y_test)

bg3=BaggingClassifier( SVC(kernel= 'sigmoid',C=30, gamma=100))

bg3.fit(x_train,y_train)
bg3.score(x_test,y_test)

bg4=BaggingClassifier(KNeighborsClassifier(n_neighbors=8))

bg4.fit(x_train,y_train)
bg4.score(x_test,y_test)

bg5=BaggingClassifier(XGBClassifier(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                     max_depth = 5, alpha = 10, n_estimators = 10))

bg5.fit(x_train,y_train)
bg5.score(x_test,y_test)



"""#**BOOSTING**"""

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier

"""**For** **GradientBoostingClassifier**"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# from sklearn.ensemble import AdaBoostClassifier
# bos=AdaBoostClassifier(GradientBoostingClassifier(n_estimators=30,max_features=1,random_state=42))
# bos.fit(x_train,y_train)

bos.score(x_test,y_test)

ypred9 = bos.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred9, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**For AdaBoostClassifier**"""

from sklearn.ensemble import AdaBoostClassifier
bos1=AdaBoostClassifier( AdaBoostClassifier(n_estimators=100, random_state=30))
bos1.fit(x_train,y_train)

bos1.score(x_test,y_test)

ypred9 = bos1.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred9, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""**For XGBClassifier**"""

from sklearn.ensemble import AdaBoostClassifier
bos2=AdaBoostClassifier(XGBClassifier(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                     max_depth = 5, alpha = 10, n_estimators = 10))
bos2.fit(x_train,y_train)

bos2.score(x_test,y_test)

ypred9 = bos2.predict(x_test)
pr, rc, fs, sup = metrics.precision_recall_fscore_support(y_test, ypred9, average='macro')
print("precision :", pr)
print("Recall :", rc)
print("F1 Score :", fs)

"""#**Stacking**"""

!pip

!apt

!apt-get install

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from mlxtend.classifier import StackingClassifier

clf1=GradientBoostingClassifier ( n_estimators=20,loss= 'deviance', max_features=1,learning_rate= 0.50,random_state=40,criterion='mse',verbose= 2,warm_start= 'bool')
clf2=KNeighborsClassifier(n_neighbors=8)
clf3=RandomForestClassifier(n_estimators=5,criterion = 'entropy', random_state=10)
clf4=AdaBoostClassifier(base_estimator=None, n_estimators=40, learning_rate=1, algorithm='SAMME', random_state=60)
log=LogisticRegression(random_state=42 )
sclf=StackingClassifier(classifiers=[clf1,clf2,clf3,clf4],use_probas=True,meta_classifier=log)

"""**Train Test Soplit**"""

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)



"""**MODELS**"""

def models(x_train,y_train):
 #Logistic Regression    0
  log = LogisticRegression(random_state=42 ) 
  log.fit(x_train,y_train)

  #Random Forest         1
  forest=RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
  forest.fit(x_train,y_train)

                         
  # Decision tree        2
  tree = DecisionTreeClassifier(criterion = 'entropy', max_depth=1, random_state=42)
  tree.fit(x_train,y_train)

                       
                        
  #Gradient Boosting     3   
  gb_clf=GradientBoostingClassifier ( n_estimators=30,max_features=1,random_state=42)
  gb_clf.fit(x_train,y_train)

                        
  #Support Vector Machines  4
  svm = SVC(kernel= 'sigmoid',C=30, gamma=100)
  svm.fit(x_train,y_train)

                       
  #k-Nearest Neighbors  5
  classifier = KNeighborsClassifier(n_neighbors=8)
  classifier.fit(x_train,y_train)

                      
  #Adaboost Classifier   6
  clf = AdaBoostClassifier(n_estimators=100, random_state=30)
  clf.fit(x_train,y_train)

                     
  #Gaussian            7
  gause_clf = GaussianNB()
  gause_clf.fit(x_train,y_train)

                     
  #Gradient Bosting    8
  gb_clf = GradientBoostingClassifier(max_features=2, max_depth=2, random_state=0)
  gb_clf.fit(x_train,y_train)

                    
  #GridSearch CV       9
  #cv=GridSearchCV(log,param,cv=5,n_jobs=-1)
  #cv.fit(x_train,y_train)

                   
  #XGBclassifier      10
  xgb =XGBClassifier(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                     max_depth = 5, alpha = 10, n_estimators = 10)
  xgb.fit(x_train, y_train)


  print('[0]Logistic Regression Training Accuracy:',log.score(x_train,y_train))
  print('[1]Random Forest Training Accuracy:',forest.score(x_train,y_train))
  print('[2]Decision tree Training Accuracy:',tree.score(x_train,y_train))
  print('[3]Gradient Boosting Training Accuracy:',gb_clf.score(x_train,y_train))
  print('[4]Support Vector Machines Training Accuracy:',svm.score(x_train,y_train))
  print('[5]k-Nearest Neighbors Training Accuracy:',classifier.score(x_train,y_train))
  print('[6]Adaboost Classifier Training Accuracy:',clf.score(x_train,y_train))
  print('[7]Gaussian Training Accuracy:',gause_clf.score(x_train,y_train))
  print('[8]Gradient Bosting Training Accuracy:',gb_clf.score(x_train,y_train))
  #print('[9]GridSearch CV Training Accuracy:',cv.score(x_train,y_train))
  print('[9]XGBclassifier Training Accuracy:',xgb.score(x_train,y_train))

  return log,forest,tree,gb_clf,svm,classifier,clf,gause_clf,gb_clf,xgb

model = models(x_train, y_train)                       #model fitting

"""**Confusion Matrix**"""

from sklearn.metrics import confusion_matrix,classification_report,log_loss,cohen_kappa_score
from sklearn import metrics
for i in range (len(model)):
  print('confusion matrix of model',i,'is:')
  cm=confusion_matrix(y_test,model[i].predict(x_test))
  TP=cm[0][0]
  TN=cm[1][1]
  FP=cm[0][1]
  FN=cm[1][0]
  print(cm)
  print()
  result1=classification_report(y_test,model[i].predict(x_test))
  print("Classification report:",)
  print(result1)
  print()
  var=((TP+TN)/(TP+TN+FP+FN))*100
  print('testing accuracy:',var)
  print('Sensitivity:',TP/(TP+FN))
  print('Specificity:',TN/(TN+FP))
  print('false positive rate:',FP/(FP+TN))
  print('False negative:',FN/(FN+TP))
  print('Negative Peridictive Value:',TN/(TN+FN))
  print('False Discovery rate:',FP/(TP+FP))
  print('Mean Absolute Eror:',metrics.mean_absolute_error(y_test,model[i].predict(x_test)))
  print('Mean Squared Error:',metrics.mean_squared_error(y_test,model[i].predict(x_test)))
  print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,model[i].predict(x_test))))
  #print('log_loss:',metrics.log_loss(y_test,model[i].predict(x_test)))
  print('??ohen_Kappa_Scorer:',cohen_kappa_score(y_test,model[i].predict(x_test)))
  
  print()
  print()
  name=['LogisticRegression','RandomForestClassifier','DecisionTreeClassifier','GradientBoostingClassifier','SVC','KNeighborsClassifier'
        ,'AdaBoostClassifier','GaussianNB','GradientBoostingClassifier','GridSearchCV','XGBClassifier']
  col_value=['blue','green','purple','blue','green','purple','green','blue','purple','blue','green','blue']
  model_accuracy=pd.Series(data=(var),index=[name[i]])
  fig=plt.figure(figsize=(5,5))
  width=0.75
  model_accuracy.sort_values().plot.bar(alpha=0.8,color=[col_value[i]])
  plt.xticks(rotation=0)
  plt.title('model Accuracy')
  plt.ylabel('Accuracy(%)')
  plt.show()
  print()
  print()

"""**VOTING CLASSIFIER**"""

from sklearn.ensemble import VotingClassifier

D = DecisionTreeClassifier(criterion='entropy', max_depth=1,random_state=42 ) 
R = RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
L = LogisticRegression(random_state=42 )
evc = VotingClassifier(estimators=[('D',D),('R',R),('L',L)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)

D= DecisionTreeClassifier(criterion='entropy', max_depth=1,random_state=42 ) 
R= RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=30)
G=GradientBoostingClassifier ( n_estimators=30,max_features=1,random_state=42)
evc = VotingClassifier(estimators=[('D',D),('R',R),('G',G)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)

R= RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=42)
G= GradientBoostingClassifier ( n_estimators=30,max_features=1,random_state=42)
K=KNeighborsClassifier(n_neighbors=8)
evc = VotingClassifier(estimators=[('R',R),('G',G),('K',K)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)

R= RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=42)
G= GradientBoostingClassifier ( n_estimators=30,max_features=1,random_state=42)
K=KNeighborsClassifier(n_neighbors=8)
evc = VotingClassifier(estimators=[('R',R),('G',G),('K',K)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)

K=KNeighborsClassifier(n_neighbors=8)
R= RandomForestClassifier(n_estimators=2,criterion='entropy',random_state=42)
evc = VotingClassifier(estimators=[('K',K),('R',R)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)

G=GradientBoostingClassifier( n_estimators=30,max_features=1,random_state=42)
A= AdaBoostClassifier(n_estimators=100, random_state=30)
evc = VotingClassifier(estimators=[('G',G),('A',A)],voting='soft' )
evc.fit(x_train,y_train)
evc.score(x_test,y_test)

"""**AUC & ROC CURVE**"""

# multi-class classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

# generate 2 class dataset
X, y = make_classification(n_samples=1000, n_classes=3, n_features=20, n_informative=3, random_state=42)

# split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# fit model
clf = OneVsRestClassifier(LogisticRegression())
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
pred_prob = clf.predict_proba(X_test)

# roc curve for classes
fpr = {}
tpr = {}
thresh ={}

n_class = 3

for i in range(n_class):    
    fpr[i], tpr[i], thresh[i] = roc_curve(y_test, pred_prob[:,i], pos_label=i)
    
# plotting    
plt.plot(fpr[0], tpr[0], linestyle='--',color='orange', label='Class 0 vs Rest')
plt.plot(fpr[1], tpr[1], linestyle='--',color='green', label='Class 1 vs Rest')
plt.plot(fpr[2], tpr[2], linestyle='--',color='blue', label='Class 2 vs Rest')
plt.title('Multiclass ROC curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive rate')
plt.legend(loc='best')
plt.savefig('Multiclass ROC',dpi=300);

"""**SVM**"""

from sklearn.metrics import roc_curve,roc_auc_score
import sklearn.metrics as metrics

#Support Vector Machines Roc Curve 
from sklearn.svm import SVC
svm = SVC(probability=True)
svm.fit(x_train,y_train)
y_score1 = svm.predict_proba(x_test)[:,1]
# Plot Receiving Operating Characteristic Curve
# Create true and false positive rates
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('Score of Support Vector Machines: ', roc_auc_score(y_test, y_score1))
# Plot ROC curves
plt.subplots(1, figsize=(4,4))
plt.title('SVM Roc Curve On Full Features')
plt.plot(false_positive_rate1, true_positive_rate1, label = "SVM")
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0] , c=".7"), plt.plot([1, 1] , c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.show()
print()
print()

#Support Vector Machines AUC Curve
svm = SVC(probability=True)
svm.fit(x_train,y_train)
y_pred = svm.predict(x_test)
#AUC Curve
plt.subplots(1, figsize=(4,4))
y_pred_proba = svm.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.title('SVM Auc Curve On Full Features')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.plot(fpr,tpr,label="auc="+str(auc))
plt.legend(loc=4)
plt.show()
print()
print()



"""**KNeighborsClassifier**"""

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









"""**KFold cross validation**"""

from sklearn.model_selection import KFold
kf = KFold(n_splits=3)
kf

for train_index,test_index in kf.split ([1,2,3,4,5,6,7,8,9]):
   print(train_index, test_index)

def get_score (model, x_train, x_test, y_train, y_test):
  model.fit(x_train, y_train)
  return model.score(x_test, y_test)

get_score(LogisticRegression(), x_train, x_test, y_train, y_test)

get_score(KNeighborsClassifier(), x_train, x_test, y_train, y_test)

get_score(RandomForestClassifier(), x_train, x_test, y_train, y_test)

"""**StratifiedKFold**"""

from sklearn.model_selection import StratifiedKFold
folds = StratifiedKFold (n_splits=3)

scores_1= []
scores_forest= []
scores_logistic = []
scores_classifier = []


for train_index, test_index in folds.split(digits.data,digits.target):
    x_train, x_test, y_train, y_test = digits.data[train_index], digits.data[test_index], \
                                       digits.target[train_index], digits.target[test_index]

scores_logistic.append(get_score(LogisticRegression(solver='liblinear',multi_class='ovr') , x_train, x_test, y_train, y_test)) 
scores_classifier.append(get_score(KNeighborsClassifier(n_neighbors=8), x_train, x_test, y_train, y_test)) 
    
scores_forest.append(get_score(RandomForestClassifier(n_estimators=2), x_train, x_test, y_train, y_test))

scores_forest

scores_logistic

scores_classifier           #KNeighborsClassifier

"""**cross_val_score function**"""

from sklearn.model_selection import cross_val_score

cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'), digits.data, digits.target,cv=3)

cross_val_score(RandomForestClassifier(n_estimators=2),digits.data, digits.target,cv=3)

cross_val_score(KNeighborsClassifier(n_neighbors=8), digits.data, digits.target,cv=3)

"""**Parameter tunning using k fold cross validation**"""

scores1 = cross_val_score(KNeighborsClassifier(n_neighbors=10),digits.data, digits.target, cv=10)
np.average(scores1)

scores2 = cross_val_score(KNeighborsClassifier(n_neighbors=20),digits.data, digits.target, cv=10)
np.average(scores2)

scores3 = cross_val_score(KNeighborsClassifier(n_neighbors=40),digits.data, digits.target, cv=10)
np.average(scores3)

scores4 = cross_val_score(KNeighborsClassifier(n_neighbors=30),digits.data, digits.target, cv=10)
np.average(scores4)







