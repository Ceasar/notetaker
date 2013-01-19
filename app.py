import os

from flask import Flask, render_template

"""
An instance of Flask will be our WSGI application.
The first argument is the name of the application's module.
If you are using a single module (as in this example),
you should use __name__ because depending on if it's started as
application or imported as module the name will be different
('__main__' versus the actual import name).
For more information, have a look at the Flask documentation.
"""
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    """
    Enable debug support. The server will reload itself on code changes,
    and it will also provide you with a helpful debugger if things go wrong.
    This makes it a major security risk and therefore it must never be used
    on production machines.
    """
    app.debug = True
    app.run(host='0.0.0.0', port=port)
