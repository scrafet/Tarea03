from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición de modelos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

# Crear las tablas
with app.app_context():
    db.create_all()

# Rutas
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id} for post in posts])

@app.route('/posts-by-user/<int:user_id>', methods=['GET'])
def get_posts_by_user(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@app.route('/posts-by-user/<int:user_id>', methods=['POST'])
def create_post(user_id):
    data = request.get_json()

    # Validar que las claves necesarias estén presentes en la solicitud
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Faltan los campos requeridos: title o content'}), 400

    new_post = Post(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post creado con éxito', 'post': {'id': new_post.id, 'title': new_post.title, 'content': new_post.content, 'user_id': new_post.user_id}}), 201

@app.route('/posts/<int:post_id>', methods=['PATCH'])
def edit_post(post_id):
    data = request.get_json()
    post = Post.query.get_or_404(post_id)
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Post actualizado con éxito', 'post': {'id': post.id, 'title': post.title, 'content': post.content}})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post eliminado con éxito'})

@app.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify([{'id': comment.id, 'content': comment.content, 'post_id': comment.post_id} for comment in comments])

@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()

    # Validar que las claves necesarias estén presentes en la solicitud
    if not data or 'content' not in data or 'post_id' not in data:
        return jsonify({'error': 'Faltan los campos requeridos: content o post_id'}), 400

    new_comment = Comment(content=data['content'], post_id=data['post_id'])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comentario creado con éxito', 'comment': {'id': new_comment.id, 'content': new_comment.content, 'post_id': new_comment.post_id}}), 201

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
