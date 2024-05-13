import os

import plugin.zxc

for filename in os.listdir('plugin'):
    if filename != "__pycache__":
        exec(f'import plugin.{filename.replace(".py", "")}')

class Content:

    def ifContain(self):
        for i in self.keyList:
            if i in self.structure:
                return True
        return False

    def isContain(self):
        for i in self.keyList:
            if i in self.structure:
                return i + ' '
        return False
            
    def returnContent(self):
        if self.isContain() != False:
            return self.structure.split(self.isContain())[len(self.structure.split(self.isContain()))-1]
        return False

    def __init__(self, structure, keyList):
        self.structure = structure
        self.keyList = keyList
        
        

# while True:
    
#     text = input('>> ')
    
#     lista = ['chuj', 'kutas']
    
#     print(Content(text, lista).isContain())
#     print(Content(text, lista).returnContent())