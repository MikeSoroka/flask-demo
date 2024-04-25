INSERT INTO users (name, surname, country, gender) VALUES
  ("Alice", "Smith", "USA", "Female"),
  ("Bob", "Johnson", "UK", "Male"),
  ("Charlie", "Brown", "Canada", "Male"),
  ("Olivia", "Garcia", "Mexico", "Female"),
  ("William", "Miller", "Australia", "Male"),
  ("Emily", "Davis", "Germany", "Female"),
  ("Benjamin", "Clark", "France", "Male"),
  ("Sophia", "Taylor", "India", "Female"),
  ("James", "Wilson", "Brazil", "Male"),
  ("Isabella", "Moore", "Japan", "Female"),
  ("Noah", "Lee", "South Korea", "Male"),
  ("Ava", "Lewis", "Argentina", "Female"),
  ("Liam", "Robinson", "South Africa", "Male"),
  ("Mia", "Walker", "Nigeria", "Female"),
  ("Ethan", "Scott", "Egypt", "Male"),
  ("Charlotte", "Turner", "Indonesia", "Female"),
  ("Michael", "Thompson", "Pakistan", "Male"),
  ("Abigail", "Garcia", "Colombia", "Female"),
  ("Daniel", "Martin", "Thailand", "Male"),
  ("Evelyn", "Hernandez", "Philippines", "Female");

INSERT INTO courses (name, approximate_duration, overview, price) VALUES
  ("Introduction to Programming", 12, "Learn the basics of programming concepts and languages.", 29.99),
  ("Data Science Fundamentals", 18, "Master the essential tools and techniques for data analysis.", 49.99),
  ("Creative Writing Techniques", 8, "Develop your storytelling skills and explore writing styles.", 19.99),
  ("Web Development Bootcamp", 24, "Learn the skills to build modern and interactive websites.", 79.99),
  ("Digital Marketing Strategies", 16, "Master the art of attracting and engaging customers online.", 39.99),
  ("Project Management Fundamentals", 10, "Learn how to plan, execute, and deliver projects effectively.", 24.99),
  ("Public Speaking for Professionals", 8, "Develop your confidence and captivate your audience.", 19.99),
  ("Time Management and Productivity", 6, "Learn strategies to maximize your time and achieve your goals.", 14.99),
  ("Financial Literacy Basics", 10, "Gain a strong foundation in personal finance and investing.", 29.99),
  ("Negotiation Skills for Success", 8, "Learn how to negotiate effectively in business and life.", 19.99),
  ("Stress Management Techniques", 6, "Discover strategies to manage stress and improve your wellbeing.", 14.99),
  ("Effective Communication Skills", 8, "Develop your communication skills for clarity and connection.", 19.99),
  ("Leadership Development for Managers", 12, "Learn how to build high-performing teams and inspire others.", 39.99),
  ("Agile Project Management", 10, "Master the agile methodology for effective project delivery.", 29.99),
  ("Social Media Marketing Strategies", 14, "Learn how to leverage social media to reach your target audience.", 34.99),
  ("Content Marketing Essentials", 12, "Discover how to create high-quality content that attracts and engages customers.", 29.99),
  ("Search Engine Optimization (SEO) Training", 16, "Learn how to optimize your website for better search engine visibility.", 39.99),
  ("Data Visualization for Beginners", 8, "Learn how to create compelling data visualizations for communication.", 19.99),
  ("Machine Learning Fundamentals", 18, "Gain an introduction to machine learning concepts and applications.", 49.99);

-- Assuming you have these IDs (replace with actual user and lecture IDs from your data)
-- User 1: Alice, User 2: Bob, User 3: Charlie, ... and so on for other users
-- Lecture 1: Introduction to Programming - Variables and Data Types
-- Lecture 2: Introduction to Programming - Control Flow Statements
-- Lecture 3: Introduction to Programming - Functions and Procedures
-- ... and so on for other lectures

INSERT INTO user_lectures (is_completed, is_starred, fk_LECTUREid, fk_USERid) VALUES
  (FALSE, FALSE, 1, 1),  -- Lecture 1 for User 1 (Alice)
  (TRUE, TRUE, 2, 2),    -- Lecture 2 for User 2 (Bob)
  (FALSE, FALSE, 3, 3),  -- Lecture 3 for User 3 (Charlie)
  -- Link more users and lectures, vary completion and starred status
  (FALSE, TRUE, 4, 4),   -- Replace IDs with your data (Lecture 4 for User 4)
  (TRUE, FALSE, 5, 5),  -- Replace IDs with your data (Lecture 5 for User 5)
  (FALSE, FALSE, 6, 6),   -- Replace IDs with your data (Lecture 6 for User 6)
  (TRUE, TRUE, 7, 7),  -- Replace IDs with your data (Lecture 7 for User 7)
  (FALSE, FALSE, 8, 8),   -- Replace IDs with your data (Lecture 8 for User 8)
  (FALSE, TRUE, 9, 9),    -- Replace IDs with your data (Lecture 9 for User 9)
  (TRUE, FALSE, 10, 10), -- Replace IDs with your data (Lecture 10 for User 10)

  -- Repeat pattern for 10 more entries, linking different users and lectures
  (FALSE, FALSE, 11, 11),  -- Replace IDs with your data (Lecture 11 for User 11)
  (TRUE, TRUE, 12, 12),   -- Replace IDs with your data (Lecture 12 for User 12)
  (FALSE, FALSE, 13, 13),  -- Replace IDs with your data (Lecture 13 for User 13)
  (TRUE, TRUE, 14, 14),   -- Replace IDs with your data (Lecture 14 for User 14)
  (FALSE, FALSE, 15, 15),  -- Replace IDs with your data (Lecture 15 for User 15)
  (TRUE, FALSE, 16, 16),   -- Replace IDs with your data (Lecture 16 for User 16)
  (FALSE, TRUE, 17, 17),    -- Replace IDs with your data (Lecture 17 for User 17)
  (TRUE, FALSE, 18, 18),   -- Replace IDs with your data (Lecture 18 for User 18)
  (FALSE, FALSE, 19, 19),  -- Replace IDs with your data (Lecture 19 for User 19)
  (TRUE, TRUE, 20, 20)   -- Replace IDs with your data (Lecture 20 for User 20)
;

-- Assuming you have these Course IDs (replace with actual IDs from your data)
-- Course 1: Introduction to Programming (ID: 1)
-- Course 2: Data Science Fundamentals (ID: 2)
-- Course 3: Creative Writing Techniques (ID: 3)
-- ... and so on for other courses with their corresponding IDs

INSERT INTO lectures (title, fk_Courseid) VALUES
  ("Introduction to Programming - Variables and Data Types", 1),  -- Lecture for Course 1 (ID: 1)
  ("Introduction to Programming - Control Flow Statements", 1),  -- Lecture for Course 1 (ID: 1)
  ("Introduction to Programming - Functions and Procedures", 1),  -- Lecture for Course 1 (ID: 1)
  ("Data Analysis with Python - Introduction to Libraries", 2),    -- Lecture for Course 2 (ID: 2)
  ("Data Analysis with Python - Data Cleaning and Manipulation", 2),  -- Lecture for Course 2 (ID: 2)
  ("Data Analysis with Python - Exploratory Data Analysis", 2),    -- Lecture for Course 2 (ID: 2)
  ("Creative Writing Techniques - Character Development", 3),       -- Lecture for Course 3 (ID: 3)
  ("Creative Writing Techniques - Crafting Dialogue and Point of View", 3),  -- Variation in title (Course 3)
  ("Creative Writing Techniques - Building a Compelling Plot", 3),     -- Variation in title (Course 3)
  ("Web Development Fundamentals - HTML and CSS Basics", 4),        -- Replace 4 with actual Course ID
  ("Web Development Fundamentals - Introduction to JavaScript", 4),   -- Replace 4 with actual Course ID
  ("Web Development Fundamentals - Building Interactive Web Applications", 4),  -- Variation in title (replace 4 with actual Course ID)
  ("Digital Marketing Strategies - Content Marketing Essentials", 5),  -- Replace 5 with actual Course ID
  ("Digital Marketing Strategies - Social Media Marketing for Beginners", 5),   -- Replace 5 with actual Course ID
  ("Digital Marketing Strategies - Email Marketing Techniques", 5),     -- Variation in title (replace 5 with actual Course ID)
  ("Project Management Fundamentals - Introduction to Project Planning", 6),  -- Replace 6 with actual Course ID
  ("Project Management Fundamentals - Task Management and Delegation", 6),    -- Replace 6 with actual Course ID
  ("Project Management Fundamentals - Effective Communication for Projects", 6),  -- Variation in title (replace 6 with actual Course ID)
  ("Public Speaking for Professionals - Overcoming Stage Fright", 7),     -- Replace 7 with actual Course ID
  ("Public Speaking for Professionals - Crafting a Captivating Presentation", 7)  -- Replace 7 with actual Course ID
;


