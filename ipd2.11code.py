from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog, filedialog
import os
import numpy as np
import pandas as pd
import re as regex
from sklearn.preprocessing import LabelEncoder, normalize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

main = Tk()
main.title("Smart Cyber Attack Detection Using AI and NLP")
main.geometry("1300x1200")

global filename, dataset, vector, rf_model
X, Y = None, None
X_train, X_test, y_train, y_test = None, None, None, None

precision, accuracy, recall, fscore = [], [], [], []
textdata, labels = [], []

def upload():
    global filename, dataset
    filename = filedialog.askopenfilename(initialdir="Dataset", filetypes=[("CSV Files", "*.csv")])
    pathlabel.config(text=filename)
    text.delete('1.0', END)

    if filename:
        dataset = pd.read_csv(filename, sep=",")
        text.insert(END, filename + " loaded\n\n")
        text.insert(END, str(dataset) + "\n")
        
        if 'payload' not in dataset.columns or 'label' not in dataset.columns:
            messagebox.showerror("Error", "Dataset must contain 'payload' and 'label' columns.")
            return
        
        dataset['label']=dataset['label'].astype(str).str.strip().str.lower()
        dataset['label'].value_counts().plot(kind="bar")
        plt.title("Normal & SQL Injection Query Distribution")
        plt.show()
    else:
        messagebox.showerror("Error", "No file selected!")

def processDataset():
    global X_train, X_test, y_train, y_test, vector, dataset, X, Y, textdata, labels

    text.delete('1.0', END)
    textdata.clear()
    labels.clear()

    if dataset is None:
        messagebox.showerror("Error", "Please upload a dataset first!")
        return

    dataset['label'] = LabelEncoder().fit_transform(dataset['label'].astype(str))

    for i in range(len(dataset)):
        query = dataset.iloc[i]['payload']
        label = dataset.iloc[i]['label']
        query = regex.sub(r'[^a-zA-Z\s]+', '', query)
        textdata.append(query)
        labels.append(label)

    vector = CountVectorizer()
    X = vector.fit_transform(textdata).toarray()

    # Save vectorizer
    os.makedirs("model", exist_ok=True)
    with open('model/vectorizer.pkl', 'wb') as file:
        pickle.dump(vector, file)

    df = pd.DataFrame(X, columns=vector.get_feature_names_out())
    text.insert(END, str(df.head()) + "\n")
    X = normalize(df.values)
    Y = np.array(labels)
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    text.insert(END, "Dataset processed successfully!\n")
    print("X_train shape:", X_train.shape, "y_train shape:", y_train.shape)

def test(cls, name):
    predict = cls.predict(X_test)
    acc = accuracy_score(y_test, predict) * 100
    p = precision_score(y_test, predict, average='macro') * 100
    r = recall_score(y_test, predict, average='macro') * 100
    f = f1_score(y_test, predict, average='macro') * 100

    text.insert(END, f"{name} - Accuracy: {acc:.2f}% | Precision: {p:.2f}% | Recall: {r:.2f}% | F1-Score: {f:.2f}%\n")
    precision.append(p)
    accuracy.append(acc)
    recall.append(r)
    fscore.append(f)

def runProposeAlgorithm():
    global rf_model

    if X_train is None or y_train is None:
        messagebox.showerror("Error", "Please process the dataset first!")
        return

    precision.clear()
    accuracy.clear()
    recall.clear()
    fscore.clear()

    text.delete('1.0', END)

    if os.path.exists('model/rf.pkl'):
        with open('model/rf.pkl', 'rb') as file:
            rf_model = pickle.load(file)
        text.insert(END, "Loaded trained Random Forest model.\n")
    else:
        text.insert(END, "Training Random Forest...\n")
        rf_model = RandomForestClassifier(n_estimators=200, random_state=0)
        rf_model.fit(X_train, y_train)
        with open('model/rf.pkl', 'wb') as file:
            pickle.dump(rf_model, file)
        text.insert(END, "Random Forest trained and saved!\n")

    test(rf_model, "Random Forest")

def runExistingAlgorithms():
    if X_train is None or y_train is None:
        messagebox.showerror("Error", "Please process the dataset first!")
        return

    text.delete('1.0', END)

    svm_cls = svm.SVC()
    svm_cls.fit(X_train, y_train)
    test(svm_cls, "SVM Algorithm")

    dt_cls = DecisionTreeClassifier()
    dt_cls.fit(X_train, y_train)
    test(dt_cls, "Decision Tree Algorithm")

    nb_cls = GaussianNB()
    nb_cls.fit(X_train, y_train)
    test(nb_cls, "Naive Bayes Algorithm")

    knn_cls = KNeighborsClassifier()
    knn_cls.fit(X_train, y_train)
    test(knn_cls, "KNN Algorithm")

def predict():
    text.delete('1.0', END)

    if not os.path.exists('model/vectorizer.pkl') or rf_model is None:
        messagebox.showerror("Error", "Model or vectorizer is missing! Train the model first.")
        return

    testFile = filedialog.askopenfilename(initialdir="Dataset", filetypes=[("CSV Files", "*.csv")])
    if not testFile:
        messagebox.showerror("Error", "No file selected!")
        return

    dataset = pd.read_csv(testFile, sep="@")

    with open('model/vectorizer.pkl', 'rb') as file:
        vector = pickle.load(file)

    for i in range(len(dataset)):
        query = regex.sub(r'[^a-zA-Z\s]+', '', dataset.iloc[i, 0])
        process = vector.transform([query]).toarray()

        if process.shape[1] != X_train.shape[1]:
            text.insert(END, f"Error: Test data has {process.shape[1]} features, expected {X_train.shape[1]}!\n")
            return

        prediction = rf_model.predict(process)[0]
        result = "SQL Injection" if prediction == 1 else "Normal Query"
        text.insert(END, f"{dataset.iloc[i, 0]} => Predicted as: {result}\n")

# GUI Buttons
font=('times',14,'bold')
font1=('times',12,'bold')
title = Label(main, text='Smart Cyber Attack Detection Using AI and NLP', bg='blue', fg='white', font=('times', 14, 'bold'))
title.config(height=3,width=120)
title.place(x=0, y=5)

uploadButton = Button(main, text="Upload Dataset", command=upload)
uploadButton.place(x=50, y=150)
uploadButton.config(font=font1)

pathlabel = Label(main, text="", bg='brown', fg='white')
pathlabel.config(font=font1)
pathlabel.place(x=460, y=100)

processButton = Button(main, text="Process Dataset", command=processDataset)
processButton.place(x=370, y=150)
processButton.config(font=font1)

proposeButton = Button(main, text="Run Random Forest", command=runProposeAlgorithm)
proposeButton.place(x=710, y=150)
proposeButton.config(font=font1)

existingButton = Button(main, text="Run Existing Algorithms", command=runExistingAlgorithms)
existingButton.place(x=50, y=200)
existingButton.config(font=font1)

predictButton = Button(main, text="Predict Attack", command=predict)
predictButton.place(x=370, y=200)
predictButton.config(font=font1)

text = Text(main, height=20, width=150)
text.place(x=10, y=250)
text.config(font=font1)

main.mainloop()
