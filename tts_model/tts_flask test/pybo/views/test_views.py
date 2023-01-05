from flask import Blueprint, render_template, request

from pybo.models import Question

bp = Blueprint('tt', __name__, url_prefix='/qu')


@bp.route('/list/', methods=['GET', 'POST'])
def _list():
    return render_template('question/test.html')

@bp.route('/list/text', methods=['GET', 'POST'])
def _list2():
    if request.method == 'POST' :
        print(request.form['textarea'])
        from ..ai_model.TTS import tts_test
        

        return render_template('question/test.html')
    else :
        return render_template('question/test.html')


# if request.method == 'POST':
#         date = request.form['date']
#         title = request.form['blog_title']
#         post = request.form['blog_main']
#         post_entry = models.BlogPost(date = date, title = title, post = post)
#         db.session.add(post_entry)
#         db.session.commit()
#         return redirect(url_for('database'))
#     else:
#         return render_template('entry.html')