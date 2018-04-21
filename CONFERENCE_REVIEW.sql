CREATE DATABASE CONFERENCE_REVIEW;

CREATE TABLE AUTHOR (
	EmailID   VARCHAR(320) NOT NULL,
	FirstName VARCHAR(15),
	LastName  VARCHAR(15),
	-- PRIMARY KEY (EmailID)
);

CREATE TABLE PAPER (
	ID                   INT NOT NULL,
	Title                VARCHAR(255),
	FileName             VARCHAR(255),
	Abstract             VARCHAR(255),
	Topic                VARCHAR(255) NOT NULL,
	ContactAuthorEmailID VARCHAR(320),
	ConferenceName       VARCHAR(255),
	-- PRIMARY KEY (ID),
	-- FOREIGN KEY (ContactAuthorEmailID) REFERENCES AUTHOR(EmailID),
	-- FOREIGN KEY (ConferenceName) REFERENCES CONFERENCE(Name)
);

CREATE TABLE AUTHORSHIP (
	AuthorEmailID VARCHAR(320) NOT NULL,
	PaperID       INT NOT NULL,
	-- PRIMARY KEY (AuthorEmailID, PaperID),
	-- FOREIGN KEY (AuthorEmailID) REFERENCES AUTHOR(EmailID),
	-- FOREIGN KEY (PaperID) REFERENCES PAPER(ID)
);