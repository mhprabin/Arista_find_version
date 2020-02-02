import re
print heading
print ''
print '+++++++++++++++++++++++++'
version_pattern = re.compile('Software image version: ([0-9]*\.[0-9]*\.[0-9])')
#read all lines of device information from file
file = open('arista_device','r')
for line in file:
    device_info = {}
    version = re.search(version_pattern, line)
    if version:
        version_string = version.group(1)
    else:
        continue
print (version_string)
