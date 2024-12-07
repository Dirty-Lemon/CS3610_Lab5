from AbstractFactoryA2.ApplicationClass import Application
from AbstractFactoryA2.MacFactoryClass import MacFactory
from AbstractFactoryA2.WinFactoryClass import WinFactory
from AbstractFactoryA2.IButtonClass import IButton
from AbstractFactoryA2.ICheckboxClass import ICheckbox

    #returns the factory with window being the base factory
observation="mac"
factory = None
if observation == 'mac': factory=MacFactory()
elif observation == 'win': factory=WinFactory()
else: print ("no such factory exists")

myapp = Application(factory)
print(myapp.createUI())
myapp.paint()