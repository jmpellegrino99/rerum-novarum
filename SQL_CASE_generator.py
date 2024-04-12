import pyperclip

field = ""
thresholds = []
var_name = field + "_TIER"

min_ = thresholds[0]
max_ = thresholds[len(thresholds)-1]

for_print = []

for_print.append("CASE")
for i in range(len(thresholds)):
	if i == 0:
		for_print.append(f"\tWHEN {field} < {thresholds[i]} THEN '0: <{thresholds[i]}'")
	if i == len(thresholds) - 1:
		for_print.append(f"\tWHEN {field} >= {thresholds[i]} THEN '{i+1}: >{thresholds[i]}'")
	else:
		for_print.append(f"\tWHEN {field} >= {thresholds[i]} AND {field} < {thresholds[i+1]} THEN '{i+1}: {thresholds[i]}-{thresholds[i+1]}]}'")
for_print.append(f"\tEND AS {var_name}")

for_print = "\n".join(for_print)
pyperclip.copy(for_print) 
