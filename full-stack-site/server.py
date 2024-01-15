from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/form')
def form_page():
    return render_template('form-page.html')

@app.post('/create-account')
def create_account():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    
    # Create an account...

    return render_template('account-created.html', first_name=first_name)

if __name__ == '__main__':
    app.run(debug=True)