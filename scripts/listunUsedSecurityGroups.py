import boto3

ec2Res = boto3.resource('ec2')

#Create couple of empty lists to capture the details
availableGroups = []
tempGroups = []

#Get all available groups
allGroups = ec2Res.security_groups.all()

for group in allGroups:
    availableGroups.append(group.group_name)

instances = ec2Res.instances.all()

#Get all groups associated with instances
for instance in instances:
    tempGroups.append(instance.security_groups)


#Function to convert list of dictionaries to simple list of groups
def usedGroups(passGroups):
    usedGroupList = []
    for group in passGroups:
        for groupName in group:
            for key, value in groupName.items():
                if key == 'GroupName':
                    usedGroupList.append(value)
    return usedGroupList

getusedGroups = usedGroups(tempGroups)

#Get the final un-used list of groups
unUsedGroups = list(set(availableGroups) - set(getusedGroups))

print "All Available Security Groups are: " + str(availableGroups)
print "All Used Security Groups are: " + str(getusedGroups)
print "All UnUsed Security Groups are: " + str(unUsedGroups)

'''
ASSIGNMENT:
Get the security group details using the client interface of Boto3 to AWS.

Hint: ec2Client = boto3.client('ec2')
'''
