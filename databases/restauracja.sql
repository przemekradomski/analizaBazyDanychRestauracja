-- Tabela Klienci
CREATE TABLE Klienci (
  "Id klienta" INTEGER PRIMARY KEY,
  "Imie Klienta" TEXT,
  "Nazwisko klienta" TEXT
);

INSERT INTO Klienci ("Id klienta", "Imie Klienta", "Nazwisko klienta") VALUES
(1, 'Antoni', 'Anonim'),
(2, 'Janusz', 'Kulesza'),
(4, 'Marcel', 'Zbyszkowski'),
(5, 'Ireneusz', 'Zawadzki'),
(6, 'Krzysztof', 'Zawiejski'),
(7, 'Przemysław', 'Radomski'),
(8, 'Rafał', 'Trzaskowski'),
(9, 'Sebastian', 'Nowak'),
(10, 'Karol', 'Wojtyła'),
(11, 'Urszula', 'Wonderlajen'),
(12, 'Nikola', 'Jaczewska');

-- Tabela Menu
CREATE TABLE Menu (
  "id zamówienia" INTEGER PRIMARY KEY,
  "nazwa dania" TEXT,
  "Ilość" INTEGER
);

INSERT INTO Menu ("id zamówienia", "nazwa dania", "Ilość") VALUES
(1, 'Zupa pomidorowka', 10),
(2, 'Rosołek od babci', 20),
(3, 'Schabowy z ziemniakami', 20),
(4, 'Mielone', 20),
(5, 'Ogórkowa', 20);

-- Tabela Pracownicy
CREATE TABLE Pracownicy (
  "Id pracownika" INTEGER PRIMARY KEY,
  "Imię Pracownika" TEXT,
  "Nazwisko Pracownika" TEXT,
  "Data zatrudnienia" TEXT,
  "Staż pracy" INTEGER,
  "Na urlopie" TEXT,
  "Stawka za godzine" REAL
);

INSERT INTO Pracownicy ("Id pracownika", "Imię Pracownika", "Nazwisko Pracownika", "Data zatrudnienia", "Staż pracy", "Na urlopie", "Stawka za godzine") VALUES
(1, 'Jan', 'Kowalski', '2016-08-01', 9, 'Tak', 11),
(2, 'Joanna', 'Kwiatkowska', '2019-04-21', 6, 'Tak', 11),
(3, 'Zbigniew', 'Kucharski', '2017-03-01', 8, 'Tak', 6),
(4, 'Radoslaw', 'Lewandowski', '2020-08-03', 5, 'Nie', 8),
(5, 'Marlena', 'Ziółkowska', '2015-09-09', 10, 'Nie', 12),
(6, 'Karolina', 'Woźniak', '2024-08-09', 1, 'Nie', 13);