 
def OpenMap(Etage : str) :
    f = open("./Samy/Map/"+Etage+".txt", "r")
    content = f.read()
    print(content)

