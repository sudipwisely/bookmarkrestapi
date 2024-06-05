from flask import Blueprint

bookmarks = Blueprint('boolmarks', __name__, url_prefix="/api/v2/bookmark")


@bookmarks.get('/all')
def get_all_bookmarks():
    return {"bookmarks": "all"}
