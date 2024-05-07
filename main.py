import sys
sys.path.append('src')  

from load import load
from register import register
from save import save
from exit import exit

dict = load()
if dict is not None :
    register(dict['user'])
    save(dict)