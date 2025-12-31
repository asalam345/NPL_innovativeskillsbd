readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]
print(readings)

for i in range(len(readings)):
    if readings[i] == 'Error':
        readings[i] = 0.0

print(readings)

for i in range(len(readings)):
    readings[i] = round(readings[i] * 1.1, 2)

print(readings)
low_quality_log = []
j = 0

print(readings)

for i in range(len(readings)):
	if readings[i] < 15.0:
		low_quality_log.append(readings[i])
       
readings = [item for item in readings if item >= 15.0]

print(readings)
print(low_quality_log)

#thislist = [item for item in thislist if item != "banana"] 