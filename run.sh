docker stop stock-flask;
docker container prune;
docker build . -t stock-flask ;
docker run -p 5050:5050 --name stock-flask stock-flask;