## ML-Model-Flask-Deployment
This is a Wine Quality Checker deployed on production using Flask API

### Prerequisites
You must have installed joblib(for loading model), Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict wine quality absed on trainign data in 'winequality-red.csv' file.
2. new.py - This contains Flask APIs that receives components details through GUI or API calls, computes the precited value based on our model and returns it.
3. templates - This folder contains the HTML template to allow user to enter features or component details and displays the predicted wine quality.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python new.py
```
Our flask will run on port 5555.

3. Navigate to URL http://localhost:5555

You should be able to view the homepage as below :
![IMAGE1](https://github.com/Gulshan-gaur/ML_App/blob/master/Wine_quality_tester/static/Screenshot%20from%202019-10-30%2018-08-51.png)

Enter valid numerical values in all  input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited quality value on the HTML page!
![IMAGE2](https://github.com/Gulshan-gaur/ML_App/blob/master/Wine_quality_tester/static/Screenshot%20from%202019-10-30%2018-09-24.png)

