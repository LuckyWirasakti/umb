from flaskwebgui import FlaskUI
from umb.wsgi import application

ui = FlaskUI(
    application,
    maximized=True,
    start_server='django'
)
ui.run()