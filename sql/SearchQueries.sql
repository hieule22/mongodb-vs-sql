-- List all papers on the topic of Machine Learning which are written by an
-- author whose first name starts with an S.

SELECT DISTINCT PAPER.ID, PAPER.FileName, PAPER.Topic
  FROM PAPER
       INNER JOIN AUTHORSHIP
       ON PAPER.ID = AUTHORSHIP.PaperID

       INNER JOIN AUTHOR
       ON AUTHORSHIP.AuthorEmailID = AUTHOR.EmailID
WHERE PAPER.TOPIC = 'Machine Learning' AND AUTHOR.FirstName LIKE 'S%';

-- List all papers with a filename starting with 'C' and a contact author
-- whose first name starts with 'A' and last name starts with 'H'.

SELECT PAPER.ID, PAPER.FileName,
       AUTHOR.EmailID, AUTHOR.FirstName, AUTHOR.LastName
  FROM PAPER
       INNER JOIN AUTHOR
       ON PAPER.ContactAuthorEmailID = AUTHOR.EmailID
WHERE PAPER.FileName LIKE 'C%' AND AUTHOR.FirstName LIKE 'A%' AND
      AUTHOR.LastName LIKE 'H%';
      
