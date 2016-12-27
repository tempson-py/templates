import web
import tempson
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        fragment = tempson.createDoc('./index.tpl')
        result = fragment.render({
            'sayHi': 'Hello, ' + name
        })
        return result

if __name__ == "__main__":
    app.run()
