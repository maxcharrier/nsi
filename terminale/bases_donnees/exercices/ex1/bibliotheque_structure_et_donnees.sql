BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Pays" (
	"idPays"	INTEGER NOT NULL,
	"nomPays"	VARCHAR2(25) NOT NULL,
	"langue"	VARCHAR2(25),
	"population"	INTEGER,
	"superficie"	INTEGER,
	PRIMARY KEY("idPays")
);


CREATE TABLE IF NOT EXISTS "Auteur" (
	"idAuteur"	INTEGER NOT NULL,
	"idPays"	INTEGER NOT NULL,
	"nomAuteur"	VARCHAR2(25) NOT NULL,
	"dateNaissance"	DATE,
	PRIMARY KEY("idAuteur"),
	FOREIGN KEY("idPays") REFERENCES "Pays"("idPays")
);


CREATE TABLE IF NOT EXISTS "Lecteur" (
	"idLecteur"	INTEGER NOT NULL,
	"nomLecteur"	VARCHAR2(25) NOT NULL,
	"prenomLecteur"	VARCHAR2(25) NOT NULL,
	"adresse"	VARCHAR2(60) NOT NULL,
	"email"	VARCHAR2(60) NOT NULL,
	"telephone"	VARCHAR2(60) NOT NULL,
	PRIMARY KEY("idLecteur")
);
CREATE TABLE IF NOT EXISTS "Livre" (
	"idLivre"	INTEGER NOT NULL,
	"idAuteur"	INTEGER NOT NULL,
	"titre"	VARCHAR2(100) NOT NULL,
	"nbPages"	INTEGER,
	"type"	VARCHAR2(20) NOT NULL,
	FOREIGN KEY("idAuteur") REFERENCES "Auteur"("idAuteur"),
	PRIMARY KEY("idLivre")
);


CREATE TABLE IF NOT EXISTS "Emprunte" (
	"idEmprunte"	INTEGER NOT NULL,
	"idLivre"	INTEGER NOT NULL,
	"idLecteur"	INTEGER NOT NULL,
	"dateDebut"	DATE,
	"dateFin"	DATE,
	PRIMARY KEY("idEmprunte"),
	FOREIGN KEY("idLivre") REFERENCES "Livre"("idLivre"),
	FOREIGN KEY("idLecteur") REFERENCES "Lecteur"("idLecteur")
);


INSERT INTO "Pays" VALUES (1,'France','Français',67060000,632734);
INSERT INTO "Pays" VALUES (2,'Espagne','Espagnol',47000000,505911);
INSERT INTO "Pays" VALUES (3,'Portugal','Portugais',10302674,92090);
INSERT INTO "Pays" VALUES (4,'Allemagne','Allemand',83149300,357386);
INSERT INTO "Pays" VALUES (5,'Italie','Italien',60359546,301336);
INSERT INTO "Pays" VALUES (6,'USA','Anglais Américain',60359546,301336);


INSERT INTO "Auteur" VALUES (1,1,'Franck Thilliez',"1973-10-15");
INSERT INTO "Auteur" VALUES (2,1,'Jean d''Ormesson',"1925-06-16" );
INSERT INTO "Auteur" VALUES (3,1,'Hugues Royer',"1965-01-12");
INSERT INTO "Auteur" VALUES (4,6,'George R. R. Martin',"1948-09-20");


INSERT INTO "Lecteur" VALUES (1,'Barriere','Theo','Vannes 56','Barriere.Theo@ici.fr','0102030401');
INSERT INTO "Lecteur" VALUES (2,'Bertho','Julie','Séné 56','Bertho.Julie@ici.fr','0102030402');
INSERT INTO "Lecteur" VALUES (3,'Coent','Cindy','Redon 35','Coent.Cindy@ici.fr','0102030403');
INSERT INTO "Lecteur" VALUES (4,'Evanno','Dylan','Theix 56','Evanno.Dylan@ici.fr','0102030404');
INSERT INTO "Lecteur" VALUES (5,'Huet','Francois','Redon 35','Huet.Francois@ici.fr','0102030405');
INSERT INTO "Lecteur" VALUES (6,'Le Normand','Maxime','Vannes 56','Huet.Francois@ici.fr','0102030406');
INSERT INTO "Lecteur" VALUES (7,'Vincent','Sarah','Vannes 56','Vincent.Sarah@ici.fr','0102030407');
INSERT INTO "Livre" VALUES (1,1,'La mémoire fantôme',480,'thriller');
INSERT INTO "Livre" VALUES (2,1,'Vertige',318,'thriller');
INSERT INTO "Livre" VALUES (3,2,'Tous les hommes en sont fous',413,'roman');
INSERT INTO "Livre" VALUES (4,2,'Presque rien sur presque tout',416,'roman');
INSERT INTO "Livre" VALUES (5,3,'Est-ce que tu m''entends ?',271,'roman');
INSERT INTO "Livre" VALUES (6,3,'Vanessa Paradis, la vraie histoire',382,'biographie');
INSERT INTO "Livre" VALUES (7,3,'Mylene',355,'biographie');
INSERT INTO "Livre" VALUES (8,4,'Le trône de fer, tome 1',476,'fantasy');
INSERT INTO "Livre" VALUES (9,4,'Le trône de fer, tome 2',540,'fantasy');
INSERT INTO "Livre" VALUES (10,4,'Le trône de fer, tome 3',487,'fantasy');


INSERT INTO Emprunte VALUES(1,8,1,"2018-05-04","2018-05-24");
INSERT INTO Emprunte VALUES(2,3,2,"2018-12-01","2018-12-12");
INSERT INTO Emprunte VALUES(3,5,3,"2016-10-18","2016-10-28");
INSERT INTO Emprunte VALUES(4,8,4,"2018-05-26","2018-06-06");
INSERT INTO Emprunte VALUES(5,5,5,"2016-03-04","2016-04-21");
INSERT INTO Emprunte VALUES(6,8,6,"2017-12-13","2017-12-26");
INSERT INTO Emprunte VALUES(7,1,7,"2016-10-23","2016-10-27");
INSERT INTO Emprunte VALUES(8,2,7,"2017-04-04","2017-04-12");
INSERT INTO Emprunte VALUES(9,8,7,"2019-01-06","2019-02-08");
INSERT INTO Emprunte VALUES(10,9,7,"2019-02-08","2019-02-28");
INSERT INTO Emprunte VALUES(11,10,7,"2019-02-28","2019-03-15");
INSERT INTO Emprunte VALUES(12,4,7,"2018-04-04","2018-04-13");
INSERT INTO Emprunte VALUES(13,2,2,"2017-08-05","2017-08-31");
INSERT INTO Emprunte VALUES(14,8,2,"2017-07-17","2017-08-31");


COMMIT;
