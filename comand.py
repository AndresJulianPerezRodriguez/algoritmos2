import os
os.system("cd ..")
os.system("cd ejemplo_git")
os.system("cd algoritmos2")
for i in range(10):
    nombre = 'carpeta'+str(i)
    texto = 'mkdir ' + '"' +nombre+'"'
    print(texto)
    os.system(texto)

