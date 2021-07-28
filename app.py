import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split  
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

users = pd.read_csv(r'NewDataset.csv') 


from sklearn.model_selection import train_test_split
X = users.drop(columns='isFake')
y = users['isFake']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20,criterion='entropy',random_state=1,bootstrap=True,max_features=2)
classifier.fit(X_train, y_train)
scores = cross_val_score(classifier, X_train,y_train, cv=5)
# print('Estimated score: %0.5f (+/- %0.5f)' % (scores.mean(), scores.std() / 2))


filename = 'NewProfile.pkl'
pickle.dump(classifier, open(filename, 'wb'))
from flask import Flask, render_template, request

import pickle
import numpy as np
filename = 'NewProfile.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getvalue():
       
 if request.method == 'POST':

    a = int (request.form['userfollowercount'])
    b = int (request.form['userfollowingcount'])
    c = int (request.form['userbiographylength'])
    d = int (request.form['usermediacount'])
    e = int (request.form['userhasprofilepic'])
    f = int (request.form['userisprivate'])
    g = int (request.form['usernamedigitcount'])
    h = int (request.form['usernamelength'])
    
    data = np.array([[a,b,c,d,e,f,g,h]])
    my_prediction = classifier.predict(data)

    return render_template('op.html',prediction=my_prediction)

if __name__ == "__main__":
    app.run(debug=True)
