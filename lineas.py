filein =open("numeros.txt","r")
lineas = filein.readlines()
n_lineas=len(lineas)

fileout = open("lineas.txt", "w")
fileout.write("{}".format(n_lineas))
fileout.close()
