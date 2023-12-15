from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')
    
    # return 'Minha página de portfólioaaaa!'

if __name__ == "__main__":
    app.run()