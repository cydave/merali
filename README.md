# In-Memory Rate Limiting

A small demo app demonstrating the [slowapi](https://github.com/laurents/slowapi) rate-limiting library configured
on top of [FastAPI](https://github.com/tiangolo/fastapi), showcasing a faulty
configuration (the default config) of slowapi which may lead to rate limiting
bypasses when used with multiple processes.


## Up and running

1. Build the docker image: `docker build . -t merali`
2. Run it: `docker run --rm -it -p 127.0.0.1:8000:8000 merali:latest`
3. Test it: `curl -i http://127.0.0.1:8000/limited`
