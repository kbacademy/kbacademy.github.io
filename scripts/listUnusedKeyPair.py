#Author: Karan Brar
#Online Training Address: http://www.kblearningacademy.com
#Infrastructure Support Address: http://www.nixsupport.com

#Please check out the assignment at the end.

import boto3
import sys

#Connect with EC2 service in a user provided region
if len(sys.argv) > 1:
    myRegion = sys.argv[1]
    boto_res = boto3.resource('ec2', region_name=myRegion)
    boto_client = boto3.client('ec2', region_name=myRegion)
else:
    # Connect with Default region is not provided by the user.
    boto_res = boto3.resource('ec2')
    boto_client = boto3.client('ec2')

#Get List of all the KeyPairs in the given region
allKeys = []
availableKeys = boto_res.key_pairs.all()

for key in availableKeys:
    allKeys.append(key.name)

#Get List of all used keys in the given region.
usedKeys = []
allInstances = boto_res.instances.all()
for instance in allInstances:
    usedKeys.append(instance.key_name)

#Get the unused keys
unUsedKeys = list(set(allKeys) - set(usedKeys))

print "All Available keys are: " + str(allKeys)
print "All Used keys are: " + str(usedKeys)
print "All UnUsed keys are: " + str(unUsedKeys)

'''
ASSIGNMENT:
If there are no keys configured, then it should print the message stating no Keys are present. 
'''

