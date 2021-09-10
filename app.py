import numpy as np
import tensorflow_hub as hub
import tensorflow as tf

# load universal sentence encoder modal
embed = hub.KerasLayer("models/")

def lambda_handler(event, context):
    # get the sentence from the request and embed
    embeddings = embed(event['text'])
    # convert tensor to np array
    a = np.array(embeddings)
    b = a.tolist()
    return {"vector": str(b[0])}