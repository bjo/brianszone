"""
App logic for maintaining blog entries
"""

from flask import render_template, Blueprint

bp = Blueprint('blog_pages', __name__, url_prefix='/blog_pages')

# register() is the view for /register
@bp.route('/built_in_modules')
def build_page(category='built_in_modules'):
    page_to_render = 'blog_pages/'+category+'.html'
    return render_template(page_to_render)
