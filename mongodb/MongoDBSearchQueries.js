// List all papers on the topic of Machine Learning which are written by an
// author whose first name starts with an S.

db.author.aggregate([
	{
		$unwind: "$paperIDs"
	},
	{
		$lookup:
		{
			from: "paper",
			localField: "paperIDs",
			foreignField: "_id",
			as: "papers"
		}
	},
	{
		$unwind: "$papers"
	},
	{
		$match:
		{
		    "firstName": { $regex: /^S/ },
			"papers.topic": "Machine learning"
		}
	},
	{
		$project:
		{
			"papers._id": 1,
			"papers.fileName": 1,
			"papers.topic": 1
		}
	}]);

// List all papers with a filename starting with 'C' and a contact author
// whose first name starts with 'A' and last name starts with 'H'.

db.paper.aggregate([
	{
		$lookup:
		{
			from: "author",
			localField: "contactAuthorEmailID",
			foreignField: "_id",
			as: "contactAuthor"
		}
	},
	{
		$unwind: "$contactAuthor"
	},
	{
		$match:
		{
			"fileName": { $regex: /^C/ },
			"contactAuthor.firstName": { $regex: /^A/ },
			"contactAuthor.lastName": { $regex: /^H/ }
		}
	},
	{
		$project:
		{
			"_id": 1,
			"fileName": 1,
			"contactAuthor._id": 1,
			"contactAuthor.firstName": 1,
			"contactAuthor.lastName": 1
		}
	}]);
