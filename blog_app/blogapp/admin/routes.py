# admin/routes.py
from flask import Blueprint, render_template, flash, redirect, url_for, abort
from functools import wraps
from flask_login import login_required, current_user
from blogapp import db
from blogapp.models import Blog, User
from blogapp.forms import BlogForm

admin_bp = Blueprint('admin', __name__)

def admin_required(func):
    """Decorator to ensure the current user is admin."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return func(*args, **kwargs)
    return wrapper

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    users = User.query.all()
    return render_template('admin/dashboard.html', blogs=blogs, users=users)

@admin_bp.route('/blog/<int:blog_id>/toggle')
@admin_required
def toggle_publish(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    blog.is_published = not blog.is_published
    db.session.commit()
    flash('Publish status toggled.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/user/<int:user_id>/toggle_admin')
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = not user.is_admin
    db.session.commit()
    flash('Admin status toggled.', 'success')
    return redirect(url_for('admin.dashboard'))
