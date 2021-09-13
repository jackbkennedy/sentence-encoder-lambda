## Universal Sentence Encoder Lambda

### Run locally

1. Build Docker container

```bash
docker build --tag sentence-encoder-lambda .
```

2. Run container

```bash
docker run -p 9000:8080  sentence-encoder-lambda:latest 
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

###

Resources

1. Tensorflow Hub - [Universal Sentence Encoder Lambda](https://tfhub.dev/google/universal-sentence-encoder/4)
2. Lambda Function Handelers - [Python](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)
3. Testing Locally - [Lambda Containers](https://docs.aws.amazon.com/lambda/latest/dg/images-test.html)