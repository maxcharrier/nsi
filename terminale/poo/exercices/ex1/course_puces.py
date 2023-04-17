import puces

def main():
    #puce1 = puces.Puce("Dolly", "bleu", 0)
    #puce2 = puces.Puce("Billou", "rouge", 0)

    #for _ in range(4):
        #print(puce1.avancer(), puce2.avancer())
    
    dolly = puces.Puce("Dolly", "bleu", 0)
    billou = puces.Puce("Billou", "rouge", 0)
    zitron = puces.Puce("Zitron", "citron", 0)

    course1 = puces.Course(10)

    course1.ajouter_puce(dolly)
    course1.ajouter_puce(billou)
    course1.ajouter_puce(zitron)

    for _ in range(5):
        course1.deplacer_puces()
    

if __name__ == "__main__":
    main()
