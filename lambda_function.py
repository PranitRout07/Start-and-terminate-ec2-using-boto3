import json

import boto3
client = boto3.client('ec2')
def create_ec2_instance():
	response = client.run_instances(ImageId='ami-0230bd60aa48260c6',
			InstanceType='t2.micro',
			MinCount=1,
			MaxCount=1)
	print("Ec2 instance created")
	return response

def terminate_ec2_instance(response):
	for instance in response['Instances']:
		id = instance['InstanceId']
	response = client.terminate_instances(
    		InstanceIds=[
        		id,
    			]
		)
	print("Successfully terminated ec2 instance")




def lambda_handler(event, context):
    resp = create_ec2_instance()
    terminate_ec2_instance(resp)
