numberLargest = int(input('enter Largest number: '))
numberSmallest = int(input('enter smallest  number'))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print('HCF is: ',numberLargest)