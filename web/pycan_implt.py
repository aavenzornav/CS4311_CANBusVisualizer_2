import cantools
from pprint import pprint
import time

import can

bus = can.Bus(channel='vcan0', interface='socketcan')


for i in range(10):
    msg = can.Message(arbitration_id=0xc0ffee, data=[id, i, 0, 1, 3, 1, 4, 1], is_extended_id=False)
    bus.send(msg.data)

time.sleep(1)


message = bus.recv(0.0)  # Timeout in seconds.
if message is None:
    print('Timeout occurred, no message.')
#db=cantools.database.load_file('static/CSS-Electronics-SAE-J1939-2018-08_v1.2.dbc')
print(message)
#print(db.messages)
#print(db.shape)

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
