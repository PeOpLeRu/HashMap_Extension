from ilib.specialDict import SpecialDict as sdict

sd = sdict()

sd["0"] = 0
sd["1"] = 1
sd["2"] = 2
sd["3"] = 3

sd["2, 3"] = 23
sd["2, 7"] = 27
sd["5, 7"] = 57
sd["5, 10"] = 510

sd["5, 7, 2"] = 572
sd["5, 10, 4"] = 5104

sd["1, 1, 1, 1"] = 1111
sd["1, 1, 2, 3"] = 1123

sd["value4"] = 4
sd["a_str"] = "str_value"

print("-------------")

print(sd)

print("-------------")

print(sd["1"])
print(sd["a_str"])

print("-------------")

print(f"sd.iloc[0] -> {sd.iloc[0]}")
print(f"sd.iloc[1] -> {sd.iloc[1]}")
print(f"sd.iloc[2] -> {sd.iloc[2]}")
print(f"sd.iloc[3] -> {sd.iloc[3]}")
print(f"sd.iloc[4] -> {sd.iloc[4]}")
print(f"sd.iloc[5] -> {sd.iloc[5]}")
print(f"sd.iloc[7] -> {sd.iloc[7]}")
print(f"sd.iloc[8] -> {sd.iloc[8]}")
print(f"sd.iloc[12] -> {sd.iloc[12]}")

print("-------------")

print(f"sd.ploc['==2, ==3'] -> {sd.ploc['==2, ==3']}")
print(f"sd.ploc['==2 &&$         ==3'] -> {sd.ploc['==2 &&$         ==3']}")
print(f"sd.ploc['>1, <=7'] -> {sd.ploc['>1, <=7']}")
print(f"sd.ploc['==5, <>7, >=3'] -> {sd.ploc['==5, <>7, >=3']}")
print(f"sd.ploc['==1, <2, >=1, >=1'] -> {sd.ploc['==1, <2, >=1, >=1']}")

print(f"sd.ploc['<>2, <>3'].ploc['<>3, <10'] -> {sd.ploc['<>2, <>3'].ploc['<>3, <10']}")