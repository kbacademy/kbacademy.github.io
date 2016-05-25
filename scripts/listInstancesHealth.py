#Author: Karan Brar
#Online URL: http://www.kblearningacademy.com

#This script will list out health of all the instances configured in all available regions.

import boto3

ec2_res=boto3.resource('ec2')
ec2_client=boto3.client('ec2')

availRegions=[]
for region in ec2_client.describe_regions()['Regions']:
    availRegions.append(region['RegionName'])

for everyRegion in availRegions:
    client=boto3.client('ec2',region_name=everyRegion)
    print "Connecting with region %s" %(everyRegion)
    for status in client.describe_instance_status(IncludeAllInstances=True)['InstanceStatuses']:
        if any(status):
            print status
        else:
            print "No Instance running in Region %s" % (everyRegion)

