## Setup

### To build image:

`docker build -t spam_api_docker_image .`

### To run container:

`docker run -d -p 8000:8001 --name spam_detector -e PYTHONUNBUFFERED=1 spam_api_docker_image`

* -d for detached (run in background)
* -p map port 8000 of the host to port 8002 in the container

## Remove, build, run: all in once
```
docker rm -f spam_detector && \
docker build -t spam_api_docker_image . && \
docker run -d -p 8000:8001 --name spam_detector -e PYTHONUNBUFFERED=1 spam_api_docker_image
```

### To send a request:

Good request:
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"post_title": "this is post title", "post_text": "this is post message"}' \
    http://localhost:8000/spam_detector/api/v1.0/detect_spam
```

Bad request:
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"post_title": "this is post title"}' \
    http://localhost:8000/spam_detector/api/v1.0/detect_spam
```

### To log into container and read gunicorn logs:

```
docker exec -it spam_detector sh
cat /var/tmp/gunicorn.logs
```

### To get container logs

`docker logs spam_detector`