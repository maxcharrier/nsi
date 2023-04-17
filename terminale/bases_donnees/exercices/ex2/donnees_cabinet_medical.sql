insert into Medecin ("idMedecin", "nom", "specialite")
values
    (0, "POIRET Louis", "Rhumatologue"),
    (1, "PETIT Jean-Pierre", "Pédiatre"),
    (2, "LENFANT Marie-Claude", "Pédiatre"),
    (3, "FROMENTIN Louis", ""),
    (4, "LAMBERT Francoise", "Homéophate"),
    (5, "DUBREUIL Pierre", "Généraliste");

insert into Personne ("idPersonne", "nom", "age", "ville")
values
    (0, "LE PETIT Marien", 3, "Vannes"),
    (1, "L'ABBE Henri", 56, "Larmor-Baden"),
    (2, "ABJEAN Adrien", 32, "Vannes"),
    (3, "DUJARDIN Laurent", 24, "Baden"),
    (4, "ABJEAN Marie", 30, "Vannes"),
    (5, "ROBERT Claude", 85, "Séné"),
    (6, "ABJEAN Chloé", 1, "Vannes");

insert into Maladie ("idMaladie", "nom", "symptomes")
values
    (0, "Grippe", "fièvre, maux de tête"),
    (1, "Varicelle", "boutons rouges suintants, fièvre"),
    (2, "Bronchite", "forte toux grasse"),
    (3, "Rubéole", "qu'est-ce que j'en sais !"),
    (4, "Oreillons", "je n'en sais rien"),
    (5, "Angine", "");

insert into Soin ("idSoin", "idPersonne", "idMedecin", "idMaladie", "date", "prix")
values
    (0, 0, 1, 1, "2010-10-15", 28),
    (1, 0, 2, 4, "2017-10-24", 50),
    (2, 0, 1, 0, "2017-10-24", 28),
    (3, 1, 0, 0, "2017-04-20", 23),
    (4, 1, 3, 0, "2017-09-15", 23),
    (5, 1, 3, 5, "2017-09-30", 50),
    (6, 2, 4, 2, "2016-10-08", 28),
    (7, 2, 4, 5, "2017-04-12", 28),
    (8, 2, 4, 0, "2017-09-22", 28),
    (9, 3, 3, 0, "2017-02-17", 23),
    (10, 4, 4, 2, "2016-10-08", 28),
    (11, 4, 4, 0, "2017-09-22", 28),
    (12, 5, 3, 0, "2017-01-02", 23),
    (13, 6, 1, 4, "2017-04-10", 23),
    (14, 6, 4, 0, "2017-09-22", 25),
    (15, 6, 2, 1, "2017-10-28", 34),
    (16, 3, 3, 2, "2017-11-03", 27);
