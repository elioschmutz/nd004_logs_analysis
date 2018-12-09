from datetime import datetime


class Printer(object):
    """ The printer is responsible for printing the questions into the console.
    """
    def print_question(self, question, rows=[]):
        self._print_header(question)
        map(self._print_row, rows)

    def print_main_header(self, text):
        text = '{}: {}'.format(
            text, datetime.now().strftime('%A %d. %B %Y, %H:%M'))
        self._print_header(text, sign="#")

    def _print_header(self, text='', sign="-"):
        text_length = len(text)
        self._print_nl()
        print(text)
        self._print_line(sign=sign, times=text_length)

    def _print_row(self, text=''):
        print('- {}'.format(text))

    def _print_line(self, sign="-", times=50):
        print(sign * times)

    def _print_nl(self):
        print('\n')
