docker stop stock-flask;
export FLASK_APP=src/app.py;
export FLASK_ENV=development;
docker build . -t stock-flask ;
docker run -p 5050:5050 -d --name stock-flask stock-flask;