import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,
                                                             'pybo.db'))
# SQLAlchemy의 이벤트 처리하는 옵션, False 비활성화
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"