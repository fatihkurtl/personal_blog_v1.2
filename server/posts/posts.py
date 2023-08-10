from flask import Blueprint, jsonify, request, send_from_directory
from models.models import Posts, PostsCategories, PostsHashtags
from sqlalchemy import event
from urllib.parse import urljoin
from datetime import datetime
import os
import time
from werkzeug.utils import secure_filename
import json

UPLOAD_FOLDER = 'posts/images'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


post_api = Blueprint('post_api', __name__)
post_create_api = Blueprint('post_create_api', __name__)
posts_detail_api = Blueprint('posts_detail_api', __name__)
post_delete_api = Blueprint('post_delete_api', __name__)
posts_update_api = Blueprint('posts_update_api', __name__)
post_search_api = Blueprint('post_search_api', __name__)
post_images_api = Blueprint('post_image_api', __name__)
post_hashtags_api = Blueprint('post_hashtags_api', __name__)


def allowed_file(filename):
    print('filename', filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@post_create_api.route('/api/create/posts', methods=['POST'])
def create_posts():
    from main import authKey, Session
    data = request.form
    print('data', data)
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401
    
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    session = Session()  
    
    if not data:
        return jsonify({'message': 'Invalid data'}), 400
  
    post = session.query(Posts).order_by(Posts.id.desc()).first()
    last_id = post.id if post else 0
    new_id = last_id + 1
    
    file = request.files['file']
    print('file', file.filename)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = f'{str(new_id)}_{filename}'
        print('file', file)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        
    new_post = Posts(title=data['title'], image=filename, reading_time=data['reading_time'], subject=data['subject'], content=data['content'])
    
    for pc in data['category'].split(','):
        posts_category = PostsCategories(category=pc)
        new_post.posts_category.append(posts_category)
    
    for ph in data['hashtags'].split(','):
        posts_hashtag = PostsHashtags(hashtag=ph)
        new_post.posts_hashtags.append(posts_hashtag)
    
    session.add(new_post)
    session.commit()
    
    return jsonify({'message': 'Post created successfully', 'info': True}), 201


@post_images_api.route('/api/post/images/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 7

@post_api.route('/api/posts', methods=['GET'])
def get_posts():
    from main import authKey, session
    search = request.args.get('search', type=str)
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401
    
    if search:
        print(search)
        posts = session.query(Posts).filter(Posts.title.like(f'%{search}%')).all()
        if not posts:
            return jsonify({'message': 'No Content'}), 204
        
        posts_list = []
        for post in posts:
            post_dict = {
                'id': post.id,
                'title': post.title,
                'subject': post.subject,
                'image':post.image,
                'reading_time': post.reading_time,
                'content': post.content,
                'create_at': post.create_at.strftime('%B %d, %Y'),
                'update_at': post.update_at
            }
            category = [pc.category for pc in post.posts_category]
            hashtags = [ph.hashtag for ph in post.posts_hashtags]
            post_dict["category"] = category
            post_dict["hashtags"] = hashtags
            posts_list.append(post_dict)
        
        return jsonify(posts_list), 200
    
    page = request.args.get('page', DEFAULT_PAGE, type=int)
    per_page = request.args.get('per_page', DEFAULT_PER_PAGE, type=int)
    
    total_posts = session.query(Posts).count()
    total_pages = (total_posts - 1) // per_page + 1
    
    offset = (page - 1) * per_page
    posts = session.query(Posts).order_by(Posts.create_at.desc()).offset(offset).limit(per_page).all()
    
    posts_list = []
    for post in posts:
        post_dict = {
            'id': post.id,
            'title': post.title,
            'subject': post.subject,
            'image': post.image,
            'reading_time': post.reading_time,
            'content': post.content,
            'create_at': post.create_at.strftime('%B %d, %Y'),
            'update_at': post.update_at
        }
        
        categories = session.query(PostsCategories).filter_by(post_id=post.id).all()
        hashtags = session.query(PostsHashtags).filter_by(post_id=post.id).all()
        
        post_dict['categories'] = [category.category for category in categories]
        post_dict['hashtags'] = [hashtag.hashtag for hashtag in hashtags]
        
        posts_list.append(post_dict)
        
    base_url = request.base_url
    
    response = {
        'posts': posts_list,
        'total': total_posts,
        'pages': total_pages,
        'prev_url': urljoin(base_url, f'api/posts?page={page-1}&per_page={per_page}') if page > 1 else None,
        'next_url': urljoin(base_url, f'api/posts?page={page+1}&per_page={per_page}') if page < total_pages else None
    }
    
    return jsonify(response), 200

@posts_detail_api.route('/api/posts/<int:id>', methods=['GET'])
def get_post_detail(id):
    from main import authKey, session
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401
    
    print('id', id)
    
    post = session.query(Posts).filter_by(id=id).first()
    if post is None:
        return {"message": "No Content"}, 204
    print(post)
        
    response = {
        "id": post.id,
        "title": post.title,
        "subject": post.subject,
        "image": post.image,
        "reading_time": post.reading_time,
        "content": post.content,
        "create_at": post.create_at.strftime('%B %d, %Y'),
        "update_at": post.update_at
    }

    categories = [pc.category for pc in post.posts_category]
    print('categories', categories)
    hashtags = [ph.hashtag for ph in post.posts_hashtags]
    print('hashtags', hashtags)
    
    response["category"] = categories
    response["hashtags"] = hashtags

    return jsonify(response), 200


@posts_update_api.route('/api/update/posts/<int:id>', methods=['PUT']) # hatalı 
def update_post(id):
    from main import authKey, session
    data = request.form
    file = request.files['file']
    print('data', data)
    print('file', file)
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized Request'}), 401
    
    if not data:
        return jsonify({'message': 'Invalid data'}), 400
    
    post = session.query(Posts).filter_by(id=id).first()
    if not post:
        return ({'message': 'No content'}), 204
    
    print('post', post)
    
    with open('posts/config.json') as config_file:
        config = json.load(config_file)
        
    image_directory = config['image_directory']
    
    file_path = os.path.join(image_directory, post.image)
    print('file_path', file_path)
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print('The file has been deleted')
        else:
            print('The file does not exist')
    except FileNotFoundError as e:
        print(e)
        
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = str(id) + '_' + filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        
    post.title = data['title']
    post.image = filename
    post.subject = data['subject']
    post.reading_time = data['reading_time']
    post.content = data['content']
    
    for pc in post.posts_category:
        session.delete(pc)
        
    for ph in post.posts_hashtags:
        session.delete(ph)
    
    for pc in data['category'].split(','):
        posts_category = PostsCategories(category=pc)
        post.posts_category.append(posts_category)
    
    for ph in data['hashtags'].split(','):
        posts_hashtag = PostsHashtags(hashtag=ph)
        post.posts_hashtags.append(posts_hashtag)
    
    session.commit()
    
    return jsonify({'message': 'Post updated successfully', 'info': True}), 200


@post_delete_api.route('/api/delete/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    from main import authKey, session

    print('id', id)
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized Request'}), 401
    
    post = session.query(Posts).filter_by(id=id).first()
    if not post:
        return ({'message': 'No content'}), 204
    
    print('post', post)
    
    with open('posts/config.json') as config_file:
        config = json.load(config_file)
        
    image_directory = config['image_directory']
    
    file_path = os.path.join(image_directory, post.image)
    print('file_path', file_path, post.image)
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print('The file has been deleted')
        else:
            print('The file does not exist')
    except FileNotFoundError as e:
        print(e)
    
    session.query(PostsHashtags).filter_by(post_id=id).delete()
    session.commit()
    
    
    session.query(PostsCategories).filter_by(post_id=id).delete()
    session.commit()
    
    session.delete(post)
    session.commit()
    
    return jsonify({'message': 'Post deleted successfully', 'info': True}), 200


@post_search_api.route('/api/search/posts', methods=['GET'])
def search_post():
    from main import authKey, session
    search = request.args.get('search', type=str)
    
    print(search)
 
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401
 
    posts = session.query(Posts).filter(Posts.title.like(f'%{search}%')).all()
    if not posts:
        return jsonify({'message': 'No Content'}), 204

    posts_list = []
    for post in posts:
        post_dict = {
            'id': post.id,
            'title': post.title,
            'subject': post.subject,
            'image': post.image,
            'reading_time': post.reading_time,
            'content': post.content,
            'create_at': post.create_at,
            'update_at': post.update_at
        }
     
    categories = [pc.category for pc in post.posts_category]
    hashtags = [ph.hashtag for ph in post.posts_hashtags]
     
    post_dict["categories"] = categories
    post_dict["hashtags"] = hashtags
     
    posts_list.append(post_dict)
 
    return jsonify(posts_list), 200


##### NOT WORKING #####
@post_hashtags_api.route('/api/getHashtags/posts', methods=['GET'])
def find_post():
    from main import authKey, session
    hashtags = request.args.get('hashtag', type=str)
    
    print('sasa', hashtags)
 
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401
 
    # posts = session.query(Posts).join(PostsHashtags).filter(PostsHashtags.hashtag.like(f"%{hashtags}%")).all()
    posts = session.query(Posts).filter(PostsHashtags.hashtag.like(f'%{hashtags}%')).all()
    print(posts)
    if not posts:
        return jsonify({'message': 'No Content'}), 204

    posts_list = []
    for post in posts:
        post_dict = {
            'id': post.id,
            'title': post.title,
            'subject': post.subject,
            'image': post.image,
            'reading_time': post.reading_time,
            'content': post.content,
            'create_at': post.create_at,
            'update_at': post.update_at
        }
     
    categories = [pc.category for pc in post.posts_category]
    hashtags = [ph.hashtag for ph in post.posts_hashtags]
     
    post_dict["categories"] = categories
    post_dict["hashtags"] = hashtags
     
    posts_list.append(post_dict)
 
    return jsonify(posts_list), 200