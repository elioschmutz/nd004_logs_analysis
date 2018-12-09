#!/usr/bin/env python3

from analyser import Analyser
from printer import Printer
from question import Question
import queries

dsn = 'dbname=news'

analyser = Analyser(dsn, Printer(), 'Logs Analysis')

analyser.add_question(
    Question('What are the most popular three articles of all time?',
             queries.MOST_TREE_POPULAR_ARTICLES,
             lambda result: '{}: {} views'.format(result[0], result[1])))

analyser.add_question(
    Question('Who are the most popular article authors of all time?',
             queries.MOST_POPULAR_ARTICLE_AUTHORS,
             lambda result: '{}: {} views'.format(result[0], result[1])))

analyser.add_question(
    Question('On which days did more than 1% of requests lead to errors?',
             queries.ERROR_DAYS,
             lambda result: '{}: {}% errors'.format(result[0],
                                                    result[1])))
analyser.analyse()
