file = open('/.ros/map.txt', 'r')
line = file.readlines().split('\n')
file.close
print(line)