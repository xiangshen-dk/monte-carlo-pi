# monte-carlo-pi


### Monte Carlo Method to calculate Pi:

Here is the repo to demostrate using Monte Carlo method to calculate the Pi.
Monte Carlo methods vary, but tend to follow a particular pattern:

1.  Define a domain of possible inputs
2.  Generate inputs randomly from a probability distribution over the domain
3.  Perform a deterministic computation on the inputs
4.  Aggregate the results

Use it to calculate Pi:

![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Pi_30K.gif/440px-Pi_30K.gif)

Reference: https://en.wikipedia.org/wiki/Monte_Carlo_method

### Setup:

*   Install the dependency.
*   Use a unique bucket name as the parameter for the SAM template and deploy the serverless application.
*   The bucket will be created by CloudFormation once the deployment completes successfully.
*   Open the bucket and create two folders. Name them __input__ and __output__.

### Invoke the application
*   Create some text files each with an integer number in the file.
*   Upload the files to the S3 bucket under the __input__ folder.
*   Files dropped in the __input__ folder of the S3 bucket will trigger the Lambda function. The number indicates how many simulations will be conducted by the Lambda function.
*   Result files will be put under the __output__ folder.

For example:

1. Create three text files:
> ls *.txt

1000.txt    2000.txt    10000.txt

> cat *.txt

10000

1000

2000

2. Upload the files:
```
aws s3 sync .  s3://cloud9-monte-carlo-pi-bucket1-9hdf6bjppr55/input/
```

3. You can find the results at the output folder. For each input file, there will be a text file for the pi value and a picture for visualizaion.
```
aws s3 ls s3://cloud9-monte-carlo-pi-bucket1-9hdf6bjppr55/output/

2018-05-07 20:15:19          0 
2018-05-07 21:00:25      36156 1000.png
2018-05-07 21:00:25         73 1000.txt
2018-05-07 21:00:27      65697 10000.png
2018-05-07 21:00:27         74 10000.txt
2018-05-07 21:00:28      46597 2000.png
2018-05-07 21:00:28         74 2000.txt
```



