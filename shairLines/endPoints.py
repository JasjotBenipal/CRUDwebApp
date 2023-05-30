from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .dbStructs import Note
from . import db
import json

endPoints = Blueprint('endPoints', __name__)


@endPoints.route('/', methods=['GET', 'POST'])
@login_required
def shairLines():
    if request.method == 'POST': 
        note = request.form.get('note')
        patient = request.form.get('patient')

        if len(note) < 1 or len(patient) < 1:
            flash('Note/Name is too short!', category='error') 
        else:
            new_note = Note(data=note, patient=patient, userId=current_user.id)  
            db.session.add(new_note) 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("shairLines.html", user=current_user)

@endPoints.route('/aboutPage', methods=['GET', 'POST'])
@login_required
def aboutPage():
    return render_template("aboutPage.html", user=current_user)

@endPoints.route('/contactPage', methods=['GET', 'POST'])
@login_required
def contactPage():
    return render_template("contactPage.html", user=current_user)

@endPoints.route('/dealsPage', methods=['GET', 'POST'])
@login_required
def dealsPage():
    return render_template("dealsPage.html", user=current_user)

@endPoints.route('/reservationsPage', methods=['GET', 'POST'])
@login_required
def reservationsPage():
    return render_template("reservationsPage.html", user=current_user)

@endPoints.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.userId == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
  