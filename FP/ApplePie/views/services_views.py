from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from ApplePie import db
from ApplePie.forms import UserCreateForm, UserLoginForm
from ApplePie.models import User

bp = Blueprint('model', __name__, url_prefix='/model')

@bp.route('/service/', methods=('GET', 'POST'))
def service():
    if request.method == 'POST' and request.form['btn']== 'saveImg':
        from ..AI_Model import tesseract

        ocr = tesseract.OCR('test.PNG')
        text = ocr.ImgToText()

        print(text)

        return render_template('services/services.html', text = text)

    elif request.method == 'POST' and request.form['btn']== 'ToTTS' :

        text = request.form['textarea']

        from ..AI_Model import tts

        TT = tts.ToTTS()
        TT.text_to_Voice(text)

        return render_template('services/services.html', text = text, voice = True)
    
    
    return render_template('services/services.html')