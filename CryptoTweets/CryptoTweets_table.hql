create database if not exists testdb;
use testdb;
create external table if not exists CryptoTweets (

  id string,
  tweet string,
  replies_count int,
  retweets_count int,
  likes_count int,
  hashtags string
)

row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/testdb.db/CryptoTweets';