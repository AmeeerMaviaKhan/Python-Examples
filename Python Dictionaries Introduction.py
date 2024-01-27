Example 1:
ages ={"Gino": 15, "Nora": 30}
print (ages["Nora"])

Example 2:
ages = {"Gino": 15, "Nora": 30, "talina": 45}
del ages["Gino"]
print(ages)

Example 3:
ages = {"gino": 15, "Nora": 30, "talina": 45}
30 in ages.values()
True
10 in ages.values()
False

Example 4:
ages = {"Gino": 15, "Nora": 30}
len(ages)

Example 5:
ages={"Gino": 15, "Nora": 30, "Talina": 45}
for student in ages:
    print(student)

Example 6:
ages = {"gino": 15, "nora": 30, "Talina": 45}
for pair in ages.items():
    print(pair)
