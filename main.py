from flask import Flask, request, abort, jsonify
import tensorflow

app = Flask(__name__)

log = app.logger

API_VERSION = '1.0'
API_PREFIX =f'/spam_detector/api/v{API_VERSION}'

@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description}, 400)
    return response

@app.route('/')
def index():
    return 'Hello there!'

class DetectSpamMessages(str):
    REQUEST_JSON_MISSING = 'Request must contain post_title and post_text in body as json'
    POST_TITLE_MISSING = 'Request missing post_title in body'
    POST_TEXT_MISSING = 'Request missing post_text in body'

@app.route(f'{API_PREFIX}/detect_spam', methods=['POST'])
def detect_spam():
    if not request.json:
        log.warn(DetectSpamMessages.REQUEST_JSON_MISSIN)
        abort(400, DetectSpamMessages.REQUEST_JSON_MISSING)
    if not 'post_title' in request.json:
        log.warn(DetectSpamMessages.POST_TITLE_MISSING)
        abort(400, DetectSpamMessages.POST_TITLE_MISSING)
    if not 'post_text' in request.json:
        log.warn(DetectSpamMessages.POST_TEXT_MISSING)
        abort(400, DetectSpamMessages.POST_TEXT_MISSING)

    is_spam = True
    score = 0.4

    return jsonify({'is_spam': is_spam, 'score': score}), 201