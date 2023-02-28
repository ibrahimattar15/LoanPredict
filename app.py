from flask import Flask,render_template,request,jsonify
from util import LoanPrediction
import config

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/loan/status/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":
        data = request.form.get
        Gender = data('Gender')
        Married = data('Married')
        Dependents = int(data('Dependents'))
        Education = data('Education')
        SelfEmployed = data('SelfEmployed')
        ApplicantIncome = int(data('ApplicantIncome'))
        CoapplicantIncome = int(data('CoapplicantIncome'))
        LoanAmount = eval(data('LoanAmount'))
        LoanAmountTerm = int(data('LoanAmountTerm'))
        CreditHistoty = int(data('CreditHistory'))
        PropertyArea = data('PropertyArea')
        target_obj = LoanPrediction(Gender,Married,Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome,LoanAmount,LoanAmountTerm,CreditHistoty,PropertyArea)
        status = target_obj.get_status()
        return render_template('index.html',prediction = status)
    else:
        data = request.args.get
        Gender = data('Gender')
        Married = data('Married')
        Dependents = int(data('Dependents'))
        Education = data('Education')
        SelfEmployed = data('SelfEmployed')
        ApplicantIncome = int(data('ApplicantIncome'))
        CoapplicantIncome = int(data('CoapplicantIncome'))
        LoanAmount = eval(data('LoanAmount'))
        LoanAmountTerm = int(data('LoanAmountTerm'))
        CreditHistoty = int(data('CreditHistory'))
        PropertyArea = data('PropertyArea')
        target_obj = LoanPrediction(Gender, Married, Dependents, Education, SelfEmployed, ApplicantIncome,CoapplicantIncome, LoanAmount, LoanAmountTerm, CreditHistoty, PropertyArea)
        status = target_obj.get_status()
        return render_template('index.html', prediction=status)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port= config.PORT_NO)

