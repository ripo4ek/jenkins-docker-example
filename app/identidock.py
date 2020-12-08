from flask import Flask, Response, request, render_template
import requests
import hashlib
import redis
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = "UNIQUE_SALT"
default_name = 'Joe Bloggs'


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']

    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
            #   '''.format(name, name_hash)
    return render_template('index.html', first=name,second=name_hash)


@app.route('/monster/<name>')
def get_identicon(name):

    image = cache.get(name)
    if image is None:
        print ("Cache miss", flush=True)
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9090)