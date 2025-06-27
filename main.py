from flask import Flask, render_template

app = Flask(__name__)

# بيانات وهمية للهواتف
phones = [
    {"brand": "Samsung", "name": "هاتف سامسونج 1", "image": "samsung1.jpg"},
    {"brand": "Apple", "name": "آيفون 1", "image": "apple1.jpg"},
    {"brand": "Samsung", "name": "هاتف سامسونج 2", "image": "samsung2.jpg"},
    {"brand": "Apple", "name": "آيفون 2", "image": "apple2.jpg"},
]

@app.route('/')
def home():
    return render_template('index.html', phones=phones)

if __name__ == '__main__':
    app.run(debug=True)
