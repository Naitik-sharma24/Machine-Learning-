from flask import Flask,render_template,request,url_for
app = Flask(__name__)

@app.route('/')   #home page / se define hai
def home():                                    
    return render_template('home.html') ##file ka name aayega 

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':    ###ending point without iske run ni hoga
    app.run(debug=True)      ###ending point without iske run ni hoga  