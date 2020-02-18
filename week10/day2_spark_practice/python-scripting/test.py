import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.5)
from sklearn.datasets import load_boston
from sklearn.pipeline import Pipeline
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import joblib
import pickle
data = load_boston()
X = data.data
y = data.target
scaler = StandardScaler()
model = RidgeCV(alphas=np.logspace(-4, 4, 9), cv=5)
pipe = Pipeline([('scaler', scaler), ('model', model)])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
pipe.fit(X_train, y_train)
pipe.score(X_train, y_train)
model_fitted = pipe.named_steps['model']
joblib.dump(pipe, 'pipe_test.jlib')
pipe_reloaded = joblib.load('pipe_test.jlib')
pipe_reloaded
pipe_reloaded.named_steps['model'].coef_
with open('model_test_1.pkl', 'wb') as file:
    pickle.dump(model_fitted, file)
with open('model_test_1.pkl', 'rb') as file:
    model_reloaded_1 = pickle.load(file)
model_reloaded_1.coef_
fig, ax = plt.subplots()
ax.barh(data.feature_names, model_reloaded_1.coef_)
plt.show()
fig.savefig('coefficients.pdf', bbox_inches='tight')