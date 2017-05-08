import web

urls = (
    '/', 'foo'
)

app = web.application(urls, globals())

render = web.template.render('templates/')


# class index(object):
#     def GET(self):
#         greeting = "Hello World"
#         return render.index(greeting=greeting)

class foo(object):
    def GET(self):
        foo = "foo"
        return render.foo(foo = foo)

if __name__ == "__main__":
    app.run()
