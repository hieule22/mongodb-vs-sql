db.author.explain("executionStats").aggregate([
	{
		$unwind: "$paperIDs"
	},
	{
		$lookup:
		{
			from: "paper",
			localField: "paperIDs",
			foreignField: "ID",
			as: "papers"
		}
	},
	{
		$unwind: "$papers"
	},
	{
		$match:
		{
			"firstName": { $gte: "Susan", $lte: "Susanne" },
			"papers.topic": "Machine learning"
		}
	},
	{
		$project:
		{
			firstName: 1,
			lastName: 1,
			"papers.ID": 1
		}
	}]);

db.author.aggregate([
	{
		$unwind: "$paperIDs"
	},
	{
		$lookup:
		{
			from: "paper",
			localField: "paperIDs",
			foreignField: "ID",
			as: "papers"
		}
	},
	{
		$unwind: "$papers"
	},
	{
		$match:
		{
			"firstName": { $gte: "Susan", $lte: "Susanne" },
			"papers.topic": "Machine learning"
		}
	},
	{
		$project:
		{
			firstName: 1,
			lastName: 1,
			"papers.ID": 1
		}
	}]);