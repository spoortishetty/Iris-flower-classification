import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

csv_file_path = 'Iris.csv'
data = pd.read_csv(csv_file_path)

X = data.drop(columns=['Species','Id'])  
y = data['Species']  

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1,test_size=0.3)

def training_model():
    model = DecisionTreeClassifier()
    trained_model = model.fit(X_train, y_train)
    return trained_model
