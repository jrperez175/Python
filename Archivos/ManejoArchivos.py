def runEscribir():
    with open("numero.txt","w") as f:
        for num in range(10):
            f.write(str(num)) 


def runLeer():
    contador=0
    with open("aleph.txt","r",encoding="utf-8") as f:
        for line in f:
            #print(f.readline)
            contador+=  line.count("Beatriz")
    
    print("Beatriz se encuentra {} veces en el texo".format(contador))


if __name__ == "__main__":
    #runEscribir()
    runLeer()