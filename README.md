## Universal Sentence Encoder Lambda

### Run locally

1. Build Docker container

```bash
docker build --tag text-similarity .
```

2. Run container

```bash
docker run -p 9000:8080  text-similarity:latest 
```

3. Make cURL request

```curl
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"text":["are you open?"]}'
```

### Result 

The endpoint returns a 512 dimension dense vector, which can be used when implementing e.g. a similarity search

```json
{"vector":"[-0.01935427635908127, ....]"}
```
