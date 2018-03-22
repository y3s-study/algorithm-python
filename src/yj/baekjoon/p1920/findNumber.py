input()
source = set(int(i) for i in input().split())

input()
for target in input().split():
    print(1 if int(target) in source else 0)
