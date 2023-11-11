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
        result['Gender']=request.form.get('Gender')
        result['Major']=request.form.get('Major')
        lang = [request.form.get('Python'), request.form.get('Java'), request.form.get('HTML'), request.form.get('C++')]
        lang = list(filter(None, lang))
        result['languages']=','.join(lang)
        
        return render_template('result.html',result=result)

if __name__ =='__main__':
    app.run(debug=True)