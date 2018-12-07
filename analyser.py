import psycopg2


class Analyser(object):
    questions = []

    def __init__(self, dsn, printer, title):
        self.printer = printer
        self.title = title
        self.dsn = dsn

    def add_question(self, question):
        self.questions.append(question)

    def analyse(self):
        self.printer.print_main_header(self.title)

        with psycopg2.connect(self.dsn) as conn:
            with conn.cursor() as curs:
                self._print_questions(curs)

    def _print_questions(self, curs):
        for question in self.questions:
            self.printer.print_question(
                question.title, question.readable_results(curs))
