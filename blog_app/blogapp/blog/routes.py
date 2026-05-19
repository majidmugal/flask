from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import current_user, login_required
from blogapp import db
from blogapp.models import Blog
from blogapp.forms import BlogForm

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
    """Home page showing all published blogs."""
    blogs = Blog.query.filter_by(is_published=True).order_by(Blog.created_at.desc()).all()
    return render_template('blog/index.html', blogs=blogs)

@blog.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if not blog.is_published and not (current_user.is_authenticated and (current_user.is_admin or blog.author == current_user)):
        abort(404)
    return render_template('blog/detail.html', blog=blog)

@blog.route('/blog/create', methods=['GET', 'POST'])
@login_required
def create_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(new_blog)
        db.session.commit()
        flash('Blog post created!', 'success')
        return redirect(url_for('blog.blog_detail', blog_id=new_blog.id))
    return render_template('blog/create.html', form=form)

@blog.route('/blog/<int:blog_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.author != current_user and not current_user.is_admin:
        abort(403)
    form = BlogForm(obj=blog)
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash('Blog updated.', 'success')
        return redirect(url_for('blog.blog_detail', blog_id=blog.id))
    return render_template('blog/edit.html', form=form, blog=blog)

@blog.route('/blog/<int:blog_id>/delete', methods=['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.author != current_user and not current_user.is_admin:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash('Blog deleted.', 'info')
    return redirect(url_for('blog.index'))
