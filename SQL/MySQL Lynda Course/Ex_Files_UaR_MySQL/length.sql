CREATE TABLE length_test (string VARCHAR(10)) DEFAULT CHARSET utf8;
SHOW CREATE TABLE length_test\G
INSERT INTO length_test (string) VALUES('hi'),('€');
SELECT string, LENGTH(string),CHAR_LENGTH(string) FROM length_test;
