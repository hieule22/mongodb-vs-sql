// Find the statistics of a collection
db.collection.stats();

// Enable profiler for all commands
db.setProfilingLevel(2);

// Get profiling data for most recent command
db.system.profile.find().limit(1).sort( { ts : -1 } ).pretty();
