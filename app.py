from flask import Flask
from AudioAPI import AudioApi
from routes import play_blueprint, next_blueprint, previous_blueprint, pause_blueprint, resume_blueprint

def create_app():
    app = Flask(__name__)
    AudioApi.register(app, route_base='/')
    app.register_blueprint(play_blueprint)
    app.register_blueprint(next_blueprint)
    app.register_blueprint(previous_blueprint)
    app.register_blueprint(pause_blueprint)
    app.register_blueprint(resume_blueprint)

    return app

# AudioApi.register(app, route_base='/')

if __name__ == '__main__':
    create_app().run()
