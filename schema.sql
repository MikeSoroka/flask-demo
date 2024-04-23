--
-- Database: `online_courses`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
  `name` varchar(255) NOT NULL,
  `approximate_duration` int(11) NOT NULL,
  `overview` varchar(255) NOT NULL,
  `price` int(11) NOT NULL
);

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`name`, `approximate_duration`, `overview`, `price`) VALUES
('Introduction to SQL', 10, 'Learn SQL basics', 50),
('Advanced SQL Queries', 15, 'Master advanced SQL queries', 75),
('Python for Beginners', 12, 'Get started with Python programming', 60),
('Machine Learning Fundamentals', 20, 'Introduction to machine learning concepts', 100),
('Web Development Bootcamp', 25, 'Learn full-stack web development', 120),
('Data Structures and Algorithms', 18, 'Master fundamental data structures and algorithms', 90),
('Digital Marketing Essentials', 10, 'Learn basics of digital marketing', 50),
('Graphic Design Fundamentals', 12, 'Introduction to graphic design principles', 60),
('iOS App Development', 20, 'Learn to develop iOS apps with Swift', 100),
('Android App Development', 20, 'Build Android apps with Java/Kotlin', 100),
('Financial Planning 101', 8, 'Basic principles of financial planning', 40),
('Photography Masterclass', 15, 'Master the art of photography', 75),
('Artificial Intelligence Basics', 12, 'Introduction to AI concepts and applications', 60),
('Blockchain Fundamentals', 10, 'Learn about blockchain technology', 50),
('UI/UX Design Fundamentals', 12, 'Introduction to UI/UX design principles', 60),
('Project Management Essentials', 10, 'Basic principles of project management', 50),
('Cybersecurity Fundamentals', 15, 'Introduction to cybersecurity concepts', 75),
('English Language Basics', 8, 'Learn English grammar and vocabulary', 40),
('Spanish for Beginners', 10, 'Introduction to Spanish language', 50),
('Japanese Language Basics', 12, 'Learn basic Japanese language skills', 60);
-- --------------------------------------------------------

--
-- Table structure for table `payment_methods`
--

CREATE TABLE `payment_methods` (
  `card_number` int(11) NOT NULL,
  `cvv_code` int(3) NOT NULL,
  `holder_name` varchar(255) NOT NULL,
  `card_name` varchar(255) NOT NULL,
  `paying_system` varchar(255) NOT NULL,
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `fk_Userid` int(11) NOT NULL
);

--
-- Dumping data for table `payment_methods`
--

INSERT INTO `payment_methods` (`card_number`, `cvv_code`, `holder_name`, `card_name`, `paying_system`, `fk_Userid`) VALUES
(2147483648, 123, 'John Doe', 'Visa', 'Visa Checkout', 1),
(2147483649, 456, 'Jane Smith', 'Mastercard', 'Mastercard SecureCode', 2),
(2147483650, 789, 'Michael Johnson', 'American Express', 'Amex Express Checkout', 3),
(2147483651, 321, 'Emily Brown', 'Discover', 'Discover Card', 4),
(2147483652, 654, 'Daniel Martinez', 'Visa', 'Visa Checkout', 5),
(2147483653, 987, 'Sophia Garcia', 'Mastercard', 'Mastercard SecureCode', 6),
(2147483654, 234, 'Matthew Lopez', 'Visa', 'Visa Checkout', 7),
(2147483655, 567, 'Olivia Perez', 'Mastercard', 'Mastercard SecureCode', 8),
(2147483656, 890, 'William Gonzalez', 'American Express', 'Amex Express Checkout', 9),
(2147483657, 123, 'Isabella Rodriguez', 'Discover', 'Discover Card', 10),
(2147483658, 456, 'Ethan Hernandez', 'Visa', 'Visa Checkout', 11),
(2147483659, 789, 'Ava Nguyen', 'Mastercard', 'Mastercard SecureCode', 12),
(2147483660, 321, 'James Kim', 'American Express', 'Amex Express Checkout', 13),
(2147483661, 654, 'Mia Lee', 'Discover', 'Discover Card', 14),
(2147483662, 987, 'Alexander Singh', 'Visa', 'Visa Checkout', 15),
(2147483663, 234, 'Charlotte Kumar', 'Mastercard', 'Mastercard SecureCode', 16),
(2147483664, 567, 'Benjamin Mohamed', 'American Express', 'Amex Express Checkout', 17);
-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT ,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL
);

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`name`, `surname`, `country`, `gender`) VALUES
('John', 'Doe', 'USA', 'Male'),
('Jane', 'Smith', 'Canada', 'Female'),
('Michael', 'Johnson', 'UK', 'Male'),
('Emily', 'Brown', 'Australia', 'Female'),
('Daniel', 'Martinez', 'Spain', 'Male'),
('Sophia', 'Garcia', 'Mexico', 'Female'),
('Matthew', 'Lopez', 'Germany', 'Male'),
('Olivia', 'Perez', 'France', 'Female'),
('William', 'Gonzalez', 'Italy', 'Male'),
('Isabella', 'Rodriguez', 'Brazil', 'Female'),
('Ethan', 'Hernandez', 'Japan', 'Male'),
('Ava', 'Nguyen', 'China', 'Female'),
('James', 'Kim', 'South Korea', 'Male'),
('Mia', 'Lee', 'India', 'Female'),
('Alexander', 'Singh', 'Russia', 'Male'),
('Charlotte', 'Kumar', 'Nigeria', 'Female'),
('Benjamin', 'Mohamed', 'South Africa', 'Male'),
('Amelia', 'Ali', 'Egypt', 'Female'),
('Lucas', 'Chen', 'Argentina', 'Male'),
('Harper', 'Liu', 'Canada', 'Female');

-- --------------------------------------------------------

--
-- Table structure for table `user_courses`
--

CREATE TABLE `user_courses` (
  `is_completed` tinyint(1) NOT NULL,
  `fk_COURSEid` int(11) NOT NULL,
  `fk_Userid` int(11) NOT NULL,
  `id` INTEGER PRIMARY KEY AUTOINCREMENT
);

--
-- Dumping data for table `user_courses`
--

INSERT INTO `user_courses` (`is_completed`, `fk_COURSEid`, `fk_Userid`) VALUES
(1, 1, 1),
(1, 2, 2),
(0, 3, 3),
(1, 4, 4),
(1, 5, 5),
(0, 6, 6),
(1, 7, 7),
(1, 8, 8),
(0, 9, 9),
(1, 10, 10),
(1, 11, 11),
(0, 12, 12),
(1, 13, 13),
(1, 14, 14),
(0, 15, 15),
(1, 16, 16),
(1, 17, 17),
(0, 18, 18),
(1, 19, 19),
(1, 20, 20);

-- --------------------------------------------------------