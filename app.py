from flask import Flask, render_template, request
import iris_model
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def basic():
    if request.method == 'POST':
        sepal_length = request.form['sepallength']
        sepal_width = request.form['petalwidth']
        petal_length = request.form['petallength']
        petal_width = request.form['petalwidth']
        y_pred = [[sepal_length,sepal_width,petal_length,petal_width]]
        trained_model = iris_model.training_model()
        prediction_value = trained_model.predict(y_pred)
        setosa = 'The flower is classified as Setosa'
        versicolor = 'The flower is classified as Versicolor'
        virginica = 'The flower is classified as Virginica'
        if prediction_value == 'Iris-setosa':
           return render_template('index.html', setosa = setosa)
        elif prediction_value == 'Iris-versicolor':
            return render_template('index.html', versicolor=versicolor)
        else:
            return render_template('index.html', virginica=virginica)

        #return render_template('index.html', prediction_value=prediction_value)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
