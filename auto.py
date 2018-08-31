import os
a=input('commit message: ')

os.system('git init')
os.system('git add .')
os.system('git commit -m \''+a+'\'')
os.system('git remote add origin https://wizarths.github.io/hufsgvi22.github.io.git')
os.system('git push -u origin master')
