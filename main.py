import shutil
import psutil
import os
import datetime
# os.rmdir("New Directory")

dir = "venv"
os.chdir(os.getcwd())

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

print("Currently we are working in", os.getcwd(), 'directory')


# print("Now making a directory:")
# os.mkdir("New_Directory")
# os.chdir("New_Directory")
# print("Currently we are working in", os.getcwd(), 'directory')

file = 'out.txt'
if os.path.isfile(file):
    print("This is a file and it is located into", os.path.abspath(file), 'location')

# with open("in.txt", 'w') as file:
#     pass

# os.remove("in.txt")
# os.rename("in.txt", "out1.txt")

# print(os.path.exists('out.txt'))
print('out.txt file size:', os.path.getsize('out.txt'), 'Bytes')

timestamp = os.path.getmtime('out.txt')

print('Last modified time:', timestamp, 'Timestamp')

print('Last modified time:', datetime.datetime.fromtimestamp(timestamp), 'using datetime')




def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if check_disk_usage("/") and check_cpu_usage():
    print("Everything is OK")
else:
    print("Error!")
