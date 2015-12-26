import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    flask.url_for('static', filename='semantic-1.2.0/semantic.css')
    flask.url_for('static', filename='sphinx/basic.css')
    flask.url_for('static', filename='sphinx/pygments.css')
    flask.url_for('static', filename='qubes.css')

    flask.url_for('static', filename='semantic-1.2.0/semantic.js')
    flask.url_for('static', filename='bootstrap-sphinx.js')
    flask.url_for('static', filename='sphinx/js/jquery-1.11.1.min.js')
    flask.url_for('static', filename='sphinx/underscore.js')
    flask.url_for('static', filename='sphinx/doctools.js')

    return flask.render_template('qubes.html', html='')


if __name__ == '__main__':
    app.run(debug=True)
