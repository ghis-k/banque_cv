-- Création de la table Etudiant
CREATE TABLE Etudiant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    contact VARCHAR(20),
    age INTEGER,
    photo VARCHAR(100),
    nationalite VARCHAR(50),
    situation_matrimoniale VARCHAR(50) CHECK(situation_matrimoniale IN ('Celibataire', 'Marie', 'Divorcé', 'Veuve/Veuf')) DEFAULT 'Celibataire',
    mobile VARCHAR(20),
    mot_de_passe VARCHAR(128) NOT NULL
);

-- Création de la table CV
CREATE TABLE CV (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    etudiant_id INTEGER NOT NULL,
    titre VARCHAR(255) NOT NULL,
    description TEXT,
    date_creation DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (etudiant_id) REFERENCES Etudiant(id) ON DELETE CASCADE
);

-- Création de la table Formation
CREATE TABLE Formation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cv_id INTEGER,
    diplomes VARCHAR(255) NOT NULL,
    etablissement VARCHAR(255) NOT NULL,
    date_debut DATE DEFAULT '2000-01-01',
    date_fin DATE DEFAULT '2000-12-31',
    localite VARCHAR(100),
    FOREIGN KEY (cv_id) REFERENCES CV(id) ON DELETE CASCADE
);

-- Création de la table Experience
CREATE TABLE Experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cv_id INTEGER,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    titre VARCHAR(255) NOT NULL,
    entreprise VARCHAR(255) NOT NULL,
    localite_entreprise VARCHAR(100),
    taches TEXT NOT NULL,
    FOREIGN KEY (cv_id) REFERENCES CV(id) ON DELETE CASCADE
);

-- Création de la table Competence
CREATE TABLE Competence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cv_id INTEGER,
    titre VARCHAR(100) NOT NULL,
    niveau INTEGER CHECK(niveau BETWEEN 0 AND 100) DEFAULT 50,
    FOREIGN KEY (cv_id) REFERENCES CV(id) ON DELETE CASCADE
);

-- Création de la table Langue
CREATE TABLE Langue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cv_id INTEGER,
    nom VARCHAR(100) DEFAULT 'Inconnu',
    niveau VARCHAR(50) CHECK(niveau IN ('Débutant', 'Intermédiaire', 'Avancé', 'Bilingue')) DEFAULT 'Débutant',
    FOREIGN KEY (cv_id) REFERENCES CV(id) ON DELETE CASCADE
);

-- Création de la table Loisir
CREATE TABLE Loisir (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cv_id INTEGER,
    libelle VARCHAR(50) NOT NULL,
    FOREIGN KEY (cv_id) REFERENCES CV(id) ON DELETE CASCADE
);

-- Création de la table Projet
CREATE TABLE Projet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cv_id INTEGER,
    titre VARCHAR(255) NOT NULL,
    date_debut DATE DEFAULT '2000-01-01',
    date_fin DATE NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (cv_id) REFERENCES CV(id) ON DELETE CASCADE
);
