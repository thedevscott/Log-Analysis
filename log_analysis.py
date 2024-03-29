#!/usr/bin/python3

import psycopg2

DBNAME = "news"


def execute_query(query):
    """
    Executes the given query against the given database name
    :param query: SQL query to execute
    :return: Result of the database query
    """
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except Exception as e:
        print("Failed to execute query:\n {}Error: {}\n".
              format(query, e))


def get_popular_articles():
    """What are the most popular three articles of all time?"""

    GET_QUERY = """SELECT articles.title, clean_articles.views
    FROM (SELECT REPLACE(SUBSTRING(log.path, 10),'-', ' ')
    AS article, count(log.path) AS views
    FROM log WHERE log.status = '200 OK' AND log.path LIKE '%article%'
    GROUP BY log.path
    ORDER BY views DESC
    LIMIT 3) as clean_articles, articles
    WHERE articles.title ~* clean_articles.article
    ORDER BY clean_articles.views DESC;
  """

    return execute_query(GET_QUERY)


def get_popular_authors():
    """Who are the most popular (top 5) article authors of all time?"""

    GET_QUERY = """ SELECT authors.name, COUNT(log.path) AS total_views
    FROM authors, log, articles
    WHERE log.status = '200 OK' AND articles.author = authors.id
    AND SUBSTRING(log.path, 10) = articles.slug
    GROUP BY authors.name
    ORDER BY total_views DESC;
    """

    return execute_query(GET_QUERY)


def get_error_day():
    """On which days did more than 1% of requests lead to errors?"""

    GET_QUERY = """SELECT TO_CHAR(error.day::DATE,'Mon dd, yyyy') AS date,
    TRUNC(error.prc::NUMERIC, 2)
    FROM (SELECT error.day as day, 100*(error.num::float/req.num::float) AS prc
    FROM (SELECT DATE(time) as day, count(*) as num
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP by day
    ORDER BY num DESC) as error,
    (SELECT date(time) as day, count(*) as num
    FROM log
    GROUP by day
    ORDER BY num DESC) as req
    WHERE error.day = req.day AND 100*(error.num::float/req.num::float) > 1
    ORDER BY error.day) AS error;
    """

    return execute_query(GET_QUERY)


if __name__ == '__main__':

    print("The top 3 articles are:")
    for article in get_popular_articles():
        print("{} -- {} views".format(article[0], article[1]))

    print("\nThe top authors are:")
    for top in get_popular_authors():
        print("{} -- {} views".format(top[0], top[1]))

    print("\nThe day(s) request errors greater than 1%:")
    for error_day in get_error_day():
        print("{} -- {}% errors".format(error_day[0], error_day[1]))
