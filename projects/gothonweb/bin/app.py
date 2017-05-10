import web

urls = (
    # '/', "index"
    '/hello','Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/',base="layout")

class Index(object):
    def GET(self):
        # form = web.input(name = None,age = None) 
        # if form.age and form.name:
        #     greeting = "name = %s  age = %s" % (form.name,form.age)
        # else:
        #    return "ERROR: name and age is required"

        # return render.index(greeting = greeting)
        return render.hello_form()
    
    def POST(self):
        form = web.input(name=None,age=None)
        greeting = "%s %s" % (form.name,form.age)
        return render.index(greeting = greeting)



# class index(object):
#     def GET(self):
#         greeting = "Hello World"
#         return render.index(greeting=greeting)

# class foo(object):
#     def GET(self):
#         foo = "foo"
#         return render.foo(foo = foo)

if __name__ == "__main__":
    app.run()
