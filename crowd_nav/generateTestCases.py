import os

iterations = 50


for i in range(iterations):
    os.system("python test.py --policy orca --phase test --visualize --test_case 0")
