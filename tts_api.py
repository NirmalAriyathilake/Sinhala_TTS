from cStringIO import StringIO
from flask import make_response
from flask import Flask, request, send_from_directory, redirect, render_template, flash, url_for, jsonify, \
    make_response, abort

from Sinhala_TTS import synthesize

app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/tts')
def view_method():

    buf = StringIO()

    # generate_wav_file should take a file as parameter and write a wav in it
    synthesize(buf) 

    response = make_response(buf.getvalue())
    buf.close()
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'
    return response

def main():
    chatbot.test_run()
    app.run(debug=True, use_reloader=False, host='0.0.0.0')


if __name__ == '__main__':
    main()