docker stop stock-flask;
docker build . -t stock-flask ;
docker run -p 5050:5050 -d --name stock-flask stock-flask;