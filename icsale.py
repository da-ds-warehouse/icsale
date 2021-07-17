import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        number1_1 = ''
        result_1 = ''
        self.render('index.html', number1_1 = '', result_1 = '')
                     
    def post(self):
           
        number1_1 = self.get_argument('number1_1')
        #if number1_1.isdigit() and number1_2.isdigit():
        try:
            number1_1 = float(number1_1)
            a = -379066.6134822497
            b = 16431.591543677703
            result_1 = str(a+(b*number1_1))
        except (ValueError, ZeroDivisionError) as error:
            number1_1 = ''
            result_1 = ''
        
        self.render('index.html', number1_1 = number1_1, result_1 = result_1)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()