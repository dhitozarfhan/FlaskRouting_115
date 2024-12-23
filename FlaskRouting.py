from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return f'Halo, {username}! Anda berhasil login.'
        else:
            return 'Login gagal. Periksa username dan password Anda.'
    # Menggunakan file login.html dari folder templates
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    import os



