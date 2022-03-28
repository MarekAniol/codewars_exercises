# Given: an array containing hashes of names
#
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
#
# Example:
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
#
# namelist([])
# # returns ''
#
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    name_list = [el["name"] for el in names ]
    print("test", ", ".join([name["name"] for name in names])[::-1])
    return ", ".join(name_list[0:-2]) + ", " + " & ".join(name_list[-2:]) if len(names)>2 else " & ".join(name_list)

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Tom'}, {'name': 'Anna'}, {'name': 'Jane'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist([]))