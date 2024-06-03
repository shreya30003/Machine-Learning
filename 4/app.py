from flask import Flask, render_template, send_file
import pickle
import io
import base64

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

import matplotlib.pyplot as plt
from sklearn import tree

@app.route('/')
def home():
    fig,ax = plt.subplots(figsize=(10,10))
    tree.plot_tree(model,filled=True)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    return render_template("index.html", img_url=img_url)

if __name__ == '__main__':
    app.run(debug=True)
