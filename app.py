from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('diamondmodeldata.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict(final)
    print(prediction)
    output = prediction[0].round(2)
    # output = round(prediction[0], 2)
    return render_template('home.html', pred=f'Price of the Diamond is ${output}')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array((list(data.values())))])
    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.debug = True
    app.run()

