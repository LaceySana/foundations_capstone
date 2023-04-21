CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone INTEGER,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    date_created DATE NOT NULL,
    hire_date DATE NOT NULL,
    user_type DEFAULT "user",
    active DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_name TEXT,
    date_added DATE,
    active DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_name TEXT,
    date_added DATE,
    active DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    assessment_id INTEGER,
    score INTEGER NOT NULL,
    date_added DATE,
    manager INTEGER,
    active DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id)
);