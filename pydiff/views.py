"""This service has a very simple API and thus the views
can be reasonably collapsed into this file.

"""
import json
import flask
from pydiff import app
import pydiff.diff as diff


@app.route('/diff', methods=['POST'])
def post_diff():
    """A POST endpoint that takes a 'left' string and a
    'right' string and performs a diff on it. If 'unified'
    is passed, a unified diff is performed.

    """
    texts = json.loads(flask.request.get_data(as_text=True))
    left = texts['left']
    right = texts['right']
    result = diff.difftexts(left, right, texts.get('unified'))
    return flask.Response(json.dumps(result), mimetype='application/json')


@app.route('/help', methods=['GET'])
def get_help():
    """A GET endpoint that simply redirects to the
    Github README for pydiff.

    """
    url = 'https://github.com/Raynes/pydiff/blob/master/README.md'
    return flask.redirect(url)
