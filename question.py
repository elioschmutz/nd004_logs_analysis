class Question(object):
    def __init__(self, title, query, format_func=lambda result: result):
        self.title = title
        self.query = query
        self.format_func = format_func

    def results(self, curs):
        curs.execute(self.query)
        return curs.fetchall()

    def readable_results(self, curs):
        results = self.results(curs)
        for result in results:
            yield self.format_func(result)
