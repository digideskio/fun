# -*- coding: utf-8 -*-

import json

counter = 0
def my_initializer(context):
    global counter
    counter += 1
    return counter

def my_handler(event, context):
    global counter
    res = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'content-type' : 'text/plain'
        },
        'body': counter
    }
    return json.dumps(res)