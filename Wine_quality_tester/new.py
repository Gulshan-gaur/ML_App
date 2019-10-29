from flask import Flask,render_template,request
import joblib 
app = Flask(__name__)
model = joblib.load('rf_regressor.pkl')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('about.html')
    if request.method == 'POST': 
        int_features = [[x for x in request.form.values()]]
        output = model.predict(int_features)
        return render_template('about.html',prediction_text="Wine Quality : " + str(output[0]))

if __name__ == "__main__":
    app.run(debug=True,port=5555)