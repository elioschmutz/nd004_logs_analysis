# Logs Analysis

This is an example analysis tool to demonstrate the use of the Python DB-API using
`psycopg2` and a `PostgreSQL` database.

It provides an example `news` database to run queries against it.

This analyser ouptups the result of different questions asked about the database in a human readable format.

<!-- MarkdownTOC levels="1" autolink=true autoanchor=false bracket="round" -->

- [Installation](#installation)
- [Alternatvie installation using a VM](#alternatvie-installation-using-a-vm)
    - [Sidenotes about the VM](#sidenotes-about-the-vm)
- [Usage](#usage)
    - [Example output](#example-output)
- [How it works](#how-it-works)
- [ERD](#erd)
- [Class diagramm](#class-diagramm)
- [Compatibility](#compatibility)

<!-- /MarkdownTOC -->

## Installation

This analyser requires a [PostgreSQL](https://www.postgresql.org/) server.
Just follow the [PostgreSQL](https://www.postgresql.org/) installation guide and run the server on the default-port `5432`.

Next, you need to clone the analyser module and change the directory to the cloned repo:

```sh
git clone git@github.com:elioschmutz/nd004_logs_analysis.git
cd nd004_logs_analysis
```

Then download, unpack and import the example-database:

```sh
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
psql -d news -f newsdata.sql.
```

and install the dependencies:

```sh
pip -r requirements.txt
```

Your environment is now set up.

## Alternatvie installation using a VM

If you don't want to set-up a local PostgreSQL with manual configuration, you can use a preset virtual machine using [vagrant](https://www.vagrantup.com/).

[Install vagrant](https://www.vagrantup.com/intro/getting-started/install.html) and clone the VM-configuration. Change the directory to the `vagrant`-folder within your cloned repo and run the VM:

```sh
git clone git@github.com:udacity/fullstack-nanodegree-vm.git
cd fullstack-nanodegree-vm/vagrant
vagrant up
```

Log into the VM with:

```sh
vagrant ssh
```

and clone the analyser module and change the directory to the cloned repo:

```sh
git clone git@github.com:elioschmutz/nd004_logs_analysis.git
cd nd004_logs_analysis
```

This VM already comes with a running PostgreSQL and a preinstalled python with all required dependencies.
The only thing you have to do is to download, unpack and import the example-database:

```sh
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
psql -d news -f newsdata.sql.
```

Your environment is now set up for the analyser-script.

### Sidenotes about the VM

The VM provides a shared directory on `/vagrant`. This is the same directory as the directory from where you startet your VM with `vagrant up`.

So if you do changes within this directory on your local computer, this changes will be available in your VM, too.

## Usage

```sh
python nd004_logs_analysis
```

or if you are already within the module, just run:

```sh
python ./
```

The analyser will output all questions and answers. Here is an example-output:

### Example output

```
Logs Analysis: Friday 01. March 1820, 09:20
##############################################


What are the most popular three articles of all time?
-----------------------------------------------------
- Candidate is jerk, alleges rival: 338647 views
- Bears love berries, alleges bear: 253801 views
- Bad things gone, say good people: 170098 views


Who are the most popular article authors of all time?
-----------------------------------------------------
- Markoff Chaney: 84557 views
- Anonymous Contributor: 170098 views
- Rudolf von Treppenwitz: 423457 views
- Ursula La Multa: 507594 views


On which days did more than 1% of requests lead to errors?
----------------------------------------------------------
- 2016-07-17: 2.26% errors
```

## How it works

The main class is the `Analyser` class. You can append `Question` objects
on it and then run the `analyse` method to start the analysing process.

## ERD

![ERD](./docs/assets/erd.png)

## Class diagramm

![CD](./docs/assets/cd.png)

## Compatibility

- Requires python3
