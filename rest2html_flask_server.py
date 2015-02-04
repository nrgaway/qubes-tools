import codecs
import sys

import flask
import rest2html

import docutils.core
from docutils.writers.html4css1 import Writer

app = flask.Flask(__name__)


@app.route('/')
def index():
    flask.url_for('static', filename='github.css')
    flask.url_for('static', filename='semantic-1.2.0/semantic.css')
    flask.url_for('static', filename='semantic-1.2.0/semantic.js')
    flask.url_for('static', filename='qubes.css')

    input_filename = '/home/user/w/qubes-tools/NOTES.rst'
    # sys.argv.append('NOTES.rst')

    try:
        #text = codecs.open(sys.argv[1], 'r', 'utf-8').read()
        #with open(input_filename, "r", 'utf-8') as source:
        with open(input_filename, "r") as source:
            text = source.read().encode('utf-8')
    except IOError:  # given filename could not be found
        return ''
    except IndexError:  # no filename given
        text = sys.stdin.read()

    writer = Writer()
    writer.translator_class = rest2html.GitHubHTMLTranslator

    parts = docutils.core.publish_parts(text, writer=writer,
                                        settings_overrides=rest2html.SETTINGS)
    if 'html_body' in parts:
        print parts['html_body']
        html = flask.Markup(parts['html_body'])

        # publish_parts() in python 2.x return dict values as Unicode type
        # in py3k Unicode is unavailable and values are of str type
        if isinstance(html, str):
            return flask.render_template('index.html', html=html)
        else:
            return flask.render_template('index.html', html=html.encode('utf-8'))
    return flask.render_template('index.html', html='')


if __name__ == '__main__':
    app.run(debug=True)
