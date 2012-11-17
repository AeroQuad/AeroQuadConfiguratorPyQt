'''
Created on Nov 16, 2012

@author: Ted Carancho
'''

xmlString = "test1.test2.test3.test4"
      
splitString = xmlString.split('.')
package = splitString[0]+'.'+splitString[1]
print(package)
for n in splitString[1:]:
    print(n)
