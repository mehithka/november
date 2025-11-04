numberLargest = int(input('enter Largest number: '))
numberSmallest = int(input('enter smallest  number'))

def hcf(numberSmallest,numberLargest):
 while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
 return numberLargest

lcm = int((numberSmallest/hcf(numberSmallest,numberLargest))*numberLargest)
print(lcm, 'is the lcm')