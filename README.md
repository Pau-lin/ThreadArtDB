# ThreadArtDB
This project is a graphical interface designed to manage a database of ThreadArt images, independent of the algorithm used.
It doesn't incorporate by default any thread art generation algorithm.

# Disclaimer
This project is also a way to experiment with Python features (PyQt) and does not claim to be a fully functional tool at the moment. 

# Database structure 
MySQL/MariaDB  :

CREATE TABLE source (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    infos TEXT,
    tags JSON NOT NULL,
    creation DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    path VARCHAR(255) NOT NULL,
    UNIQUE (path)
);

CREATE TABLE input (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status TEXT,
    description TEXT,
    infos TEXT,
    tags JSON,
    creation DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    path VARCHAR(255) NOT NULL,
    img_id INT,
    FOREIGN KEY (img_id) REFERENCES source(id) ON DELETE CASCADE,
    UNIQUE (path)
);

CREATE TABLE output (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note INT,
    infos TEXT,
    tags JSON,
    creation DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    num_pins INT,
    num_lines INT,
    program VARCHAR(50),
    config JSON,
    path VARCHAR(255),
    input_id INT,
    UNIQUE (path),
    FOREIGN KEY (input_id) REFERENCES input(id) ON DELETE CASCADE
);
