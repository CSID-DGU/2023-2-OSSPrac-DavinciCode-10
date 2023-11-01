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
        
        return render_template('result.html',result=result)


if __name__ =='__main__':
    app.run(debug=True)