# Cryptocurrency Data Science Project
## _Ahmed Elhadidy - 202101774_

[https://github.com/Hadidy7/CryptocurrencyDataHadoop]

- Docker is a set of the platform as a service products that use OS-level virtualization to deliver software in packages called containers.
- Hive is an SQL Based tool that builds over Hadoop to process the data.

The project consists of a setup to a production environment using Docker to control Hive. The purpose of this is to manipulate the data included in the cryptocurrency dataset scraped using Twint. 

## Files

The following files are included in this project:

- [docker-compose.yml] - A docker tool to define and run the container, inside is the configuration required to power up Hive services.
- [hadoop-hive.env] - A configuration file to setup variables for the working environment.
- [CryptoTweets.csv] - A raw .csv file that consists of the scraped data from Twitter.
- [CryptoTweets_table.hql] - A HQL file that sets up a Hive database and table and filters specific columns from the .csv file.

## Installation

Install the latest version of [Docker](https://docs.docker.com/desktop/windows/install/).

Add the project files to your local and navigate to the project directory.
```sh
> cd [HIVE FILE LOCATION]
```

Open terminal and run the following docker command to create and start the services.
```sh
> docker-compose up
```

After setup is complete, log into the Hive server and create a database and hive table using this command 
```sh
> docker exec -it hive-server /bin/bash
```

Navigate to the CryptoTweets directory
```sh
root@0712a6a1ba04:/opt# ls
hadoop-2.7.4  hive
root@0712a6a1ba04:/opt# cd
root@0712a6a1ba04:~# ls
root@0712a6a1ba04:~# cd /CryptoTweets
```

Execute CryptoTweets_table.sql to create a new database that has a table in Hive
```sh
root@0712a6a1ba04:/CryptoTweets# hive -f CryptoTweets_table.hql
```

Add the data from CryptoTweets.csv file to the Hive table in the new database
```sh
root@0712a6a1ba04:/CryptoTweets# hadoop fs -put CryptoTweets.csv hdfs://namenode:8020/user/hive/warehouse/testdb.db/CryptoTweets
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



