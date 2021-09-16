import numpy as np
import tensorflow_hub as hub
import tensorflow as tf

# load universal sentence encoder model
embed = hub.KerasLayer("models/")

def lambda_handler(event, context):
    # get the sentence from the request and embed
    embeddings = embed(event['text'])
    # convert tensor to np array
    a = np.array(embeddings)
    b = a.tolist()
    return {"vector": b[0]}