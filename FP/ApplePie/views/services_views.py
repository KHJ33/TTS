from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from ApplePie import db
from ApplePie.forms import UserCreateForm, UserLoginForm
from ApplePie.models import User

import os
import config
import time

bp = Blueprint('model', __name__, url_prefix='/model')

@bp.route('/service/', methods=('GET', 'POST'))
def service():
    if request.method == 'POST' and request.form['btn']== 'Text Extraction':
        from ..AI_Model import tesseract

        while True :
            if os.path.isfile(config.IMAGE_PATH+'test_IMG.PNG'):
                break
            time.sleep(0.1)

        ocr = tesseract.OCR('test_IMG.PNG')
        text = ocr.ImgToText()

        print('aaaaa')

        if not text :
            text = '인식된 문자가 없습니다.'

        # print(text)

        return render_template('services/services.html', text = text)

    elif request.method == 'POST' and request.form['btn']== 'TTS Start' :

        text = request.form['textarea']

        from ..AI_Model import tts

        TT = tts.ToTTS()
        TT.text_to_Voice(text)

        return render_template('services/services.html', text = text, voice = True)
    
    
    return render_template('services/services.html')