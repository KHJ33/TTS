import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,
                                                             'FPT.db'))
# SQLAlchemy의 이벤트 처리하는 옵션, False 비활성화
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 암호화 처리 옵션
SECRET_KEY = "dev"

# tersseract.py 경로 설정 부분
TESSERACT_PATH = './ApplePie/package/Tesseract-OCR/tesseract.exe'
IMAGE_PATH = 'ApplePie/saveImg/'

# tts.py 경로 설정 부분
GLOW_TTS_CHECKPOINT_PATH = './ApplePie/AI_Model/glow_tts/checkpoint_39000.pth.tar'
GLOW_TTS_CONFIG_PATH = './ApplePie/AI_Model/glow_tts/config.json'

HIFI_GAN_CHECKPOINT_PATH = './ApplePie/AI_Model/hifi_gan/checkpoint_300000.pth.tar'
HIFI_GAN_CONFIG_PATH = './ApplePie/AI_Model/hifi_gan/config.json'

# SAVE_VOICE_PATH = './ApplePie/saveVoice/'
SAVE_VOICE_PATH = './ApplePie/static/'