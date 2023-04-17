create table if not exists Medecin (
    "idMedecin"     number primary key,
    "nom"           varchar2(25) not null,
    "specialite"    varchar2(40)
);

create table if not exists Personne (
    "idPersonne"    number primary key,
    "nom"           varchar2(25) not null,
    "age"           number not null,
    "ville"         varchar2(40)
);

create table if not exists Maladie (
    "idMaladie"     number primary key,
    "nom"           varchar2(25) not null,
    "symptomes"     varchar2(100)
);

create table if not exists Soin (
    "idSoin"       number primary key,
    "idMedecin"     number not null,
    "idPersonne"    number not null,
    "idMaladie"     number not null,
    "date"          date,
    "prix"          number,
    foreign key ("idMedecin") references Medecin("idMedecin"),
    foreign key ("idPersonne") references Personne("idPersonne"),
    foreign key ("idMaladie") references Maladie("idMaladie")
);
