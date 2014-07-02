'''
Created on Jul 2, 2014

@author: viejoemer

How can I merge (union) two Python dictionaries?

¿Cómo puedo combinar (unión) dos diccionarios de Python?

The method update() adds dictionary dict2's key-values pairs 
in to dict. This function does not return anything.
'''

#dict with two values and keys
d = {'Name': 'Emerson', 'Age': 27}

#dict with one value and key
d2 = {'Sex': 'Male' }

#Merge in one dict
d.update(d2)

print (d)

