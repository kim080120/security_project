docker stop board-app
docker rm board-app

git pull origin main

docker build -t board-portfolio .
docker run -d -p 8000:8000 --name board-app board-portfolio

# 실행 상태 확인
docker ps

# 로그 확인
docker logs board-app
