docker stop docker-flask;
docker image  build -t docker-flask . ;
docker run -p 5555:5555 -d docker-flask;