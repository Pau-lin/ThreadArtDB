# ThreadArtDB
This project is a graphical interface designed to manage a database of ThreadArt images, regardless the algorithm used.

It doesn't incorporate by default any thread art generation algorithm.


# Disclaimer
This project is also a way for me to experiment with Python features (PyQt) and does not claim to be a fully functional tool at the moment. 

# Database structure 

This program is intended to work with MySQL/MariaDB with this structure :

CREATE TABLE img (
    id INT AUTO\_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    infos TEXT,
    tags JSON NOT NULL,
    creation DATETIME NOT NULL DEFAULT NOW(),
    path VARCHAR(255) NOT NULL,
    UNIQUE (path)
);

CREATE TABLE input (
    id INT AUTO\_INCREMENT PRIMARY KEY,
    status TEXT,
    description TEXT,
    infos TEXT,
    tags JSON,
    creation DATETIME NOT NULL DEFAULT NOW(),
	path VARCHAR(255) NOT NULL,
    img\_id INT,
    FOREIGN KEY (img\_id) REFERENCES img(id) ON DELETE CASCADE,
    UNIQUE (path)
);

CREATE TABLE output (
    id INT AUTO\_INCREMENT PRIMARY KEY,
    description TEXT,
    note INT,
    infos TEXT,
    num\_pins INT,
    num\_lines INT,
    program VARCHAR(50),
    config JSON,
    input\_version\_id INT,
    path VARCHAR(255),  -- Ajout de la colonne 'path'
    UNIQUE (path),
    FOREIGN KEY (input\_version\_id) REFERENCES input(id) ON DELETE CASCADE
);
