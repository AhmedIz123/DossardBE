import flask as Flask , request
import numpy as np
import torch


app = Flask(__name__)

model = torch.load('model/best.pt')


@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # features Must be in the form [[a, b]]

    return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))



if __name__ == "__main__":
    app.run()
