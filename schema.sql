CREATE TABLE genders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender VARCHAR(255) NOT NULL
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    fk_GENDERid INTEGER REFERENCES genders(id)
    ON DELETE CASCADE
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    approximate_duration INTEGER NOT NULL,
    overview TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE lectures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    fk_COURSEid INTEGER REFERENCES courses(id)
    ON DELETE CASCADE
);

CREATE TABLE user_lectures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    is_completed BOOLEAN NOT NULL,
    is_starred BOOLEAN NOT NULL,
    start_date DATE NOT NULL,
    fk_LECTUREid INTEGER REFERENCES lectures(id),
    fk_USERid INTEGER REFERENCES users(id)
);