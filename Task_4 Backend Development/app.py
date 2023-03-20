# 1. Import Library
from flask import Flask, request, render_template
import re

# 2. Create the object with a parameter __name__
app = Flask(__name__)

# 3. Create an end points using routes and bind them with a functionality
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        string = request.form['string']
        regex = request.form['regex']
        matches = re.findall(regex, string)
        counts = len(matches)
        return render_template('index.html', matches=matches, count=counts)
    else:
        return render_template('index.html')
    
@app.route('/about')
def regex():
    return render_template('regex.html')

# 4. Run the App
if __name__ == '__main__':
    app.run(debug=True)