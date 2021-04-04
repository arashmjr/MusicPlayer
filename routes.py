from flask import Blueprint
from SoundManager import SoundManager


play_blueprint = Blueprint('play', __name__)

@play_blueprint.route('/play', methods=['POST'])
def play():
    SoundManager.get_instance().play_songs()
    return 'Success'


next_blueprint = Blueprint('next', __name__)

@next_blueprint.route('/next', methods=['GET'])
def next():
    SoundManager.get_instance().next_song()
    return 'Success'


previous_blueprint = Blueprint('/previous', __name__)

@previous_blueprint.route('/previous', methods=['GET'])
def previous():
    SoundManager.get_instance().previous_song()
    return 'Success'


pause_blueprint = Blueprint('/pause', __name__)

@pause_blueprint.route('/pause', methods=['GET'])
def pause():
    SoundManager.get_instance().pause_song()
    return 'Success'


resume_blueprint = Blueprint('/resume', __name__)

@resume_blueprint.route('/resume', methods=['GET'])
def resume():
    SoundManager.get_instance().resume_song()
    return 'Success'