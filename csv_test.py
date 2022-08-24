import pandas as pd
from flask import Flask,render_template

app = Flask(__name__)

df=pd.read_csv("data.csv")

df.to_csv("data.csv", index=None)

@app.route('/', methods=['GET'])
def sarampion():

    data = pd.read_csv("data.csv")

    return render_template('index.html', tables=[data.to_html()],titles=[''])


if __name__=="__main__":
    app.run(debug=True)
















#filename = 'data.json'
#data = pd.read_json(filename)
#data.to_json('data.json')
#print(data.shape)
#print (data)



#def get_categorias():
#    result = data
#    return jsonify(result)
             

