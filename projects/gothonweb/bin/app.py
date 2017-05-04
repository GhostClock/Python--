import web

urls = (
    '/','index'
)

app = web.application(urls,globals())

class index:
    def GET(self):
        greeting = "<h1>Hello World</h1>"
        return greeting

if __name__ == "__main__":
    app.run()