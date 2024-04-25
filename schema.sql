CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  country VARCHAR(255),
  gender VARCHAR(255)
);

CREATE TABLE courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL,
  approximate_duration INT,
  overview TEXT,
  price DECIMAL(10,2)
);

CREATE TABLE lectures (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(255) NOT NULL,
  fk_Courseid INT,
  FOREIGN KEY (fk_Courseid) REFERENCES courses(id)
);

CREATE TABLE user_lectures (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  is_completed BOOLEAN,
  is_starred BOOLEAN,
  fk_LECTUREid INT,
  fk_USERid INT,
  FOREIGN KEY (fk_LECTUREid) REFERENCES lectures(id),
  FOREIGN KEY (fk_USERid) REFERENCES users(id)
);
