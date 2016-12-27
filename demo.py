import web
import tempson
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        try:
            fragment = tempson.createDoc('./index.tpl')
            result = fragment.render({
                'myName': name,
                'sayHi': 'Hello, ' + name,
                'list': [{
                    'name': 'JavaScript'
                }, {
                    'name': 'C++'
                }, {
                    'name': 'Python'
                }]
            })
            return result
        except Exception as e:
            print e

if __name__ == "__main__":
    app.run()
