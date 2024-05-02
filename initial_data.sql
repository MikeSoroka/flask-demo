-- Insert genders
INSERT INTO genders (gender) VALUES
    ('Male'),
    ('Female'),
    ('Non-binary'),
    ('Prefer not to say');

-- Insert users
INSERT INTO users (name, surname, country, fk_GENDERid) VALUES
    ('John', 'Doe', 'USA', 1),
    ('Alice', 'Smith', 'UK', 2),
    ('Mohammed', 'Ali', 'Egypt', 1),
    ('Emma', 'Johnson', 'Canada', 2),
    ('Chen', 'Wei', 'China', 1),
    ('Maria', 'Garcia', 'Spain', 2),
    ('Ahmed', 'Khan', 'Pakistan', 1),
    ('Lena', 'Müller', 'Germany', 2),
    ('Yusuf', 'Abdul', 'Nigeria', 1),
    ('Sophia', 'Kim', 'South Korea', 2),
    ('Diego', 'Lopez', 'Mexico', 1),
    ('Aya', 'Sato', 'Japan', 2),
    ('Anna', 'Novak', 'Russia', 2),
    ('Ethan', 'Brown', 'Australia', 1),
    ('Fatima', 'Mohamed', 'Saudi Arabia', 2),
    ('Luca', 'Ricci', 'Italy', 1),
    ('Leila', 'Silva', 'Brazil', 2),
    ('Muhammad', 'Choi', 'Indonesia', 1),
    ('Olivia', 'Lee', 'New Zealand', 2),
    ('Omar', 'Gonzalez', 'Argentina', 1);

-- Insert courses
INSERT INTO courses (name, approximate_duration, overview, price) VALUES
    ('Introduction to Programming', 30, 'Learn the basics of programming', 49.99),
    ('Web Development Fundamentals', 45, 'Build your first website', 59.99),
    ('Data Science Essentials', 60, 'Discover the power of data analysis', 69.99),
    ('Graphic Design Basics', 40, 'Create stunning visuals', 54.99),
    ('Language Learning: Spanish', 50, 'Master the Spanish language', 64.99),
    ('Finance for Beginners', 35, 'Understand the basics of finance', 44.99),
    ('Photography 101', 55, 'Capture beautiful moments', 74.99),
    ('Fitness and Nutrition', 40, 'Get in shape and eat healthy', 59.99),
    ('Introduction to Psychology', 50, 'Explore the human mind', 69.99),
    ('Music Theory Fundamentals', 45, 'Learn the basics of music theory', 54.99);

-- Insert lectures
INSERT INTO lectures (title, fk_COURSEid) VALUES
    ('Variables and Data Types', 1),
    ('HTML Basics', 2),
    ('Introduction to Data Science', 3),
    ('Introduction to Graphic Design', 4),
    ('Greetings and Introductions', 5),
    ('Understanding Interest Rates', 6),
    ('Camera Settings', 7),
    ('Nutrition Basics', 8),
    ('The Mind and Behavior', 9),
    ('Notes and Scales', 10);

-- Insert user_lectures
INSERT INTO user_lectures (is_completed, is_starred, fk_LECTUREid, fk_USERid) VALUES
    (TRUE, TRUE, 1, 1),
    (TRUE, FALSE, 2, 1),
    (TRUE, TRUE, 3, 1),
    (TRUE, FALSE, 1, 2),
    (TRUE, TRUE, 4, 2),
    (TRUE, FALSE, 5, 2),
    (TRUE, TRUE, 1, 3),
    (TRUE, FALSE, 2, 3),
    (TRUE, TRUE, 3, 3),
    (TRUE, FALSE, 4, 3),
    (TRUE, TRUE, 1, 4),
    (TRUE, FALSE, 2, 4),
    (TRUE, TRUE, 3, 4),
    (TRUE, FALSE, 4, 4),
    (TRUE, TRUE, 1, 5),
    (TRUE, FALSE, 2, 5),
    (TRUE, TRUE, 3, 5),
    (TRUE, FALSE, 4, 5),
    (TRUE, TRUE, 1, 6),
    (TRUE, FALSE, 2, 6);
-- Add more records as needed
