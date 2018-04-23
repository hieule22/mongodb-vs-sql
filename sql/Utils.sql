-- Find the size of all tables in a given database
SELECT TABLE_NAME, TABLE_ROWS, DATA_LENGTH, INDEX_LENGTH,
       (DATA_LENGTH + INDEX_LENGTH) "Size in bytes"
  FROM INFORMATION_SCHEMA.TABLES
 WHERE TABLE_SCHEMA = 'CONFERENCE_REVIEW';

-- Enable the profiler
SET PROFILING=1;

-- Display profiling data for all queries
SHOW PROFILES;

-- Display profiling data for a specific query
SHOW PROFILE FOR QUERY 41;
