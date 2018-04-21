SELECT AUTHOR.FirstName, AUTHOR.LastName, PAPER.ID
  FROM PAPER
       INNER JOIN AUTHORSHIP
       ON PAPER.ID = AUTHORSHIP.PaperID

       INNER JOIN AUTHOR
       ON AUTHORSHIP.AuthorEmailID = AUTHOR.EmailID
WHERE PAPER.TOPIC = 'Machine Learning'
      AND AUTHOR.FirstName >= 'Susan' AND AUTHOR.FirstName <= 'Susanne';
