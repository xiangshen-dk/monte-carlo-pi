from __future__ import print_function

import json
import urllib
import boto3
import io

import matplotlib
# so it would work with Tk lib
matplotlib.use('agg',warn=False, force=True)

import matplotlib.pyplot as plt
from numpy import random,sqrt,pi

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        input_text = response['Body'].read().rstrip()
        print(input_text)

        ret_dict = calc_pi(int(input_text))

        s3.put_object(Bucket=bucket, Key='output/'+input_text+'.txt', Body=ret_dict['result'])
        s3.put_object(Bucket=bucket, Key='output/'+input_text+'.png', Body=ret_dict['img'].getvalue())
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

# monte carlo method to calculate Pi
def calc_pi(n):
    ret = {}
    buf = io.BytesIO()
    # scattering n points over the unit square
    p = random.rand(n,2)
    
    # counting the points inside the unit circle
    idx = sqrt(p[:,0]**2+p[:,1]**2) < 1
    
    fig = plt.figure()
    ax = plt.subplot(111)
    
    plt.title('Monte Carlo - Pi(n=%s)'%n)
    ax.plot(p[idx,0],p[idx,1],'b.') # point inside
    ax.plot(p[idx==False,0],p[idx==False,1],'r.') # point outside
    ax.axis([-0.1,1.1,-0.1,1.1]) 
    fig.savefig(buf)
    
    ret['img'] = buf
    
    estimate_pi = sum(idx).astype('double')/n*4
    # estimation of pi
    ret['result'] = "real pi: %0.16f" % pi
    ret['result'] += "\n\testimation: %0.16f" % estimate_pi
    ret['result'] += "\n\t\t%0.8f%%" % ((pi-estimate_pi)*100/pi)
    return ret
    

