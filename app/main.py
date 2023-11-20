from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['University']=request.form.get('University')
        result['Major']=request.form.get('Major')
        result['Gender']=request.form.get('Gender')
        result['Email']=request.form.get('Email') + "@" + request.form.get('Email2')
        lang = [request.form.get('Python'), request.form.get('Java'), request.form.get('HTML'), request.form.get('C++')]
        lang = list(filter(None, lang))
        result['languages']=','.join(lang)
        
        return render_template('result.html',result=result)

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)