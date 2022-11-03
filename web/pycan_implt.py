import cantools
from pprint import pprint

db=cantools.database.load_file('static/CSS-Electronics-SAE-J1939-2018-08_v1.2.dbc')
print(db.messages[1])

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


# class PhotoForm(FlaskForm):
#     photo = FileField(validators=[FileRequired()])
#
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     form = PhotoForm()
#
#     if form.validate_on_submit():
#         f = form.photo.data
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(
#             app.instance_path, 'static', filename
#         ))
#         return redirect(url_for('index'))
#
#     return render_template('upload.html', form=form)
