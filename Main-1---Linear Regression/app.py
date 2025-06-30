from flask import Flask,render_template,request,url_for
import joblib,pickle
import pandas as pd

##load the model 

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')   #home page / se define hai
def home():                                    
    return render_template('home.html') ##file ka name aayega 

@app.route('/Project')
def contact():
    return render_template('Projects.html')

@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST" :
        try:
            brand_name = request.form['brand_name']
            owner_name = int(request.form['owner'])
            age_bike = int(request.form['age'])
            power_bike = int(request.form['power'])
            kms_driven_bike = int(request.form['kms_driven'])
    
            bike_numbers ={'TVS': 0,
                                            'Royal Enfield': 1,
                                            'Triumph': 2,
                                            'Yamaha': 3,
                                            'Honda': 4,
                                            'Hero': 5,
                                            'Bajaj': 6,
                                            'Suzuki': 7,
                                            'Benelli': 8,
                                            'KTM': 9,
                                            'Mahindra': 10,
                                            'Kawasaki': 11,
                                            'Ducati': 12,
                                            'Hyosung': 13,
                                            'Harley-Davidson': 14,
                                            'Jawa': 15,
                                            'BMW': 16,
                                            'Indian': 17,
                                            'Rajdoot': 18,
                                            'LML': 19,
                                            'Yezdi': 20,
                                            'MV': 21,
                                            'Ideal': 22}
            brand_name_encoded = bike_numbers.get(brand_name)
            input_data = [(owner_name,
                           brand_name_encoded,        ##single point ke uper prediction le rahe hai in 3  
                           kms_driven_bike,                  #line me
                             age_bike,power_bike)]
            prediction = model.predict(input_data)
            prediction = round(prediction[0],2)
            return render_template("Projects.html",prediction=prediction)
        except:
            return 'something is wrong'
if __name__=='__main__':    ###ending point without iske run ni hoga
    app.run(debug=True)      ###ending point without iske run ni hoga  

