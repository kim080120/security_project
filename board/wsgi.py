import os
from django.core.wsgi import get_wsgi_application

# 환경 변수를 Django 프로젝트 설정 모듈로 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board.settings')  # 'board'는 프로젝트 이름입니다.

# WSGI 애플리케이션 객체 생성
application = get_wsgi_application()
