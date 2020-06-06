CREATE TABLE like_test (
string1 CHAR(2),
string2 CHAR(2)
) DEFAULT CHARSET=latin1 DEFAULT COLLATE=latin1_german2_ci;

INSERT INTO like_test (string1, string2) VALUES('ae','ä');

