from flask import Blueprint, render_template, flash, redirect, url_for, request, abort, current_app
from flask_login import current_user, login_required
from ..forms import ProfileForm
from .. import db
from ..models import User, Profile

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if request.method == 'GET' and current_user.profile:
        form.bio.data = current_user.profile.bio
        form.location.data = current_user.profile.location
        form.website.data = current_user.profile.website
    if form.validate_on_submit():
        # Update user fields
        current_user.username = form.username.data
        current_user.email = form.email.data
        # Update or create profile
        if not current_user.profile:
            profile = Profile(user_id=current_user.id)
            db.session.add(profile)
        else:
            profile = current_user.profile
        profile.bio = form.bio.data
        profile.location = form.location.data
        profile.website = form.website.data
        # Handle avatar upload if provided
        if form.avatar.data:
            avatar_file = form.avatar.data
            filename = f"avatar_{current_user.id}_{avatar_file.filename}"
            avatar_path = f"{current_app.config['UPLOAD_FOLDER']}/{filename}"
            avatar_file.save(avatar_path)
            profile.avatar_filename = filename
        db.session.commit()
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('user.profile'))
    return render_template('user/profile.html', form=form)
