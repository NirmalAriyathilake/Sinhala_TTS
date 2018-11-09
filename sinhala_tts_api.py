from io import StringIO
from flask import make_response
from flask import Flask, request, send_from_directory, redirect, render_template, flash, url_for, jsonify, \
    make_response, abort

import synthesizer
from flask import send_file

import os
from hyperparams import Hyperparams as hp

app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/tts')
def view_method():

    inputtext = request.args.get('input')
    synthesizer.synthesize(inputtext)

    path_to_file = os.path.join(hp.sampledir, 'test.wav')

    return send_file(
        path_to_file,
        mimetype="audio/wav",
        as_attachment=True,
        attachment_filename="test.wav")


def main():
    app.run(debug=True, use_reloader=False, host='0.0.0.0')


if __name__ == '__main__':
    main()
