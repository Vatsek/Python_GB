# задача 21
# Напишите программу для печати всех уникальных значений в словаре. 

# inpDict = {
#     "I": "S001",
#     "II": "S002",
#     "III": "S001",
#     "IV": "S005",
#     "V": " S005 ",
#     "VI": " S009 ",
#     "VII": " S007 ",
# }

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# вариант 1
slovar = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", \
          "VII": " S005 ", "V": " S009 ", " VIII ": " S007 "}

slovarB = slovar.values()

print(set(slovarB))


# вариант 2 
def getCountUnicalElements(inputDict):
    outSet = set()
    for value in inputDict.values():
        outSet.add(value)
    return len(outSet)