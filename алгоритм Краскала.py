E = ["AB", "AC", "AE", "BC", "BE", "CE", "BD", "EG", "ED", "DG", "GH", "DH", "DF", "FH"]
V = set("ABCDEFGH")
weight = [2, 2, 7, 2, 2, 5, 9, 9, 10, 2, 17, 16, 5, 17]
ostov = set("A")
sum = 0
my_dict = {}

for i in range(len(E)):
    my_dict[E[i]] = weight[i]

dict_sorted = {}
for value in sorted(weight):
    for key in E:
        if my_dict[key] == value:
            dict_sorted[key] = value

while ostov != V:
    for key in dict_sorted.keys():
        if key[0] in ostov and key[1] in ostov:
            continue
        elif (key[0] in ostov and key[1] not in ostov) or (key[1] in ostov and key[0] not in ostov):
            ostov.update(key)
            sum += dict_sorted[key]
            break

print(sum)
