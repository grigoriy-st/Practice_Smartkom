from flask import request, url_for, Flask, Response, render_template, jsonify
from sqlalchemy import create_engine
from flask_mysqldb import MySQL


app = Flask('__name__', static_folder='static')
engine = create_engine('mariadb+mariadbconnector://root:1234@localhost:3306/Project')

# Конфигурация БД
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'Project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
# Проверка подключения
# with engine.connect() as conn:
#     print("Успешное подключение к MariaDB!")


@app.route('/')
def get_page():
    return render_template('index.html')


@app.route('/sign', methods=['POST', 'GET'])
def sign_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        cur = mysql.connection.cursor()
        cur.execute('select * FROM User where username = %s', (username,))

        if not cur.fetchone():
            return jsonify({'error': 'User is not exists'}, 400)

    return render_template('sign.html')


@app.route('/registration', methods=['POST', 'GET'])
def reg_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cur = mysql.connection.cursor()
        cur.execute('select * FROM User where username = %s', (username,))

        if cur.fetchone():
            return jsonify({'error': 'User is exists'}, 400)

        cur.execute(
            'Insert into User (username, password) values (%s, %s)', 
            (username, password)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'User is added'})
        return '''
                <h1>User id added</h2>
                <a href="/">На главную</a>
                '''

    return render_template('registration.html')


@app.route('/user_list', methods=['GET', 'POST'])
def get_user_list():
    return render_template('user_list.html')


app.run(host='127.0.0.1', port='8080')
