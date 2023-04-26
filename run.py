from flask import Flask, render_template

app=Flask(__name__,template_folder='template')
app.debug = True
app.static_folder = 'static'


@app.route('/')
def index():
    with open('Report.txt', 'r') as f:
        data = f.read()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
