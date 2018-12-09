MOST_TREE_POPULAR_ARTICLES = """
    SELECT title, count(title) as views FROM log
    JOIN articles on log.path = CONCAT('/article/', articles.slug)
    GROUP BY title
    ORDER BY views desc
    LIMIT 3;
    """

MOST_POPULAR_ARTICLE_AUTHORS = """
    SELECT authors.name, count(authors.name) as views FROM log
    JOIN articles on log.path = CONCAT('/article/', articles.slug)
    JOIN authors ON articles.author = authors.id
    GROUP BY authors.name
    """


_REQUESTS_PER_DAY = """
    SELECT date(time) as day, count(*) as total FROM log
    GROUP BY date(time)
    """

_ERROR_REQUESTS_PER_DAY = """
    SELECT date(time) as day, count(*) as total FROM log
    WHERE status != '200 OK'
    GROUP BY date(time)
    """

_DAYS_WITH_ERROR_RATIO = """
    SELECT all_requests.day,
           CAST(error_requests.total as FLOAT) / all_requests.total as ratio
    FROM ({requests_per_day}) as all_requests
    LEFT JOIN ({error_requests_per_day}) as error_requests
    ON all_requests.day = error_requests.day
    """.format(requests_per_day=_REQUESTS_PER_DAY,
               error_requests_per_day=_ERROR_REQUESTS_PER_DAY)

ERROR_DAYS = """
    SELECT TO_CHAR(day, 'Mon DD, YYYY'), ROUND((ratio * 100)::NUMERIC, 2)
    FROM ({days_with_error_ratio}) as ratio_errors
    WHERE ratio > 0.01
    """.format(days_with_error_ratio=_DAYS_WITH_ERROR_RATIO)
