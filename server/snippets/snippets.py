from flask import Blueprint, jsonify, request, send_from_directory
from models.models import Snippets, SnippetsCategories, SnippetsHashtags
from sqlalchemy import event
from urllib.parse import urljoin
from datetime import datetime
import os
import time
from werkzeug.utils import secure_filename
import json #

UPLOAD_FOLDER = 'snippets/images'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


snippets_api = Blueprint('snippets_api', __name__)
snippet_create_api = Blueprint('snippets_create_api', __name__)
snippets_detail_api = Blueprint('snippets_detail_api', __name__)
snippet_delete_api = Blueprint('snippets_delete_api', __name__)
snippets_update_api = Blueprint('snippets_update_api', __name__)
snippet_images_api = Blueprint('snippets_image_api', __name__)


def allowed_file(filename):
    print('filename', filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@snippet_create_api.route('/api/create/snippets', methods=['POST'])
def create_snippets():
    from main import authKey, Session
    data = request.form
    print('data', data)
    
    if not data:
        return jsonify({'message': 'Invalid data'}), 400
    
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    session = Session()
    
    file = request.files['file']
    print('file', file)
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    snippet = session.query(Snippets).order_by(Snippets.id.desc()).first()
    last_id = snippet.id if snippet else 0
    new_id = last_id + 1
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = f'{str(new_id)}_{filename}'
        print('file', file)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        
    session = Session()
    new_snippet = Snippets(title=data['title'], subject=data['subject'], image=filename, reading_time=data['reading_time'], content=data['content'])
    
    for sc in data['category'].split(','):
        snippets_category = SnippetsCategories(category=sc)
        new_snippet.snippets_category.append(snippets_category)
        
    for sh in data['hashtags'].split(','):
        snippet_hashtag = SnippetsHashtags(hashtag=sh)
        new_snippet.snippets_hashtags.append(snippet_hashtag)


    session.add(new_snippet)
    session.commit()    
    
    return jsonify({'message': 'Snippet created successfully', 'info': True}), 201


@snippet_images_api.route('/api/images/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 7

@snippets_api.route('/api/snippets', methods=['GET'])
def get_snipepts():
    from main import authKey, session
    search = request.args.get('search', type=str)
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401
    
    if search:
        print(search)
        snippets = session.query(Snippets).filter(Snippets.title.like(f'%{search}%')).all()
        if not snippets:
            return jsonify({'message': 'No Content'}), 204
        
        snippets_list = []
        for snippet in snippets:
            snippet_dict = {
                'id': snippet.id,
                'title': snippet.title,
                'subject': snippet.subject,
                'image': snippet.image,
                'reading_time': snippet.reading_time,
                'content': snippet.content,
                'create_at': snippet.create_at.strftime('%B %d, %Y'),
                'update_at': snippet.update_at
            }
            categories = [sc.category for sc in snippet.snippets_category]
            hashtags = [sh.hashtag for sh in snippet.snippets_hashtags]
            snippet_dict['categories'] = categories
            snippet_dict['hashtags'] = hashtags
            snippets_list.append(snippet_dict)
        
        return jsonify(snippets_list), 200
    
    page = request.args.get('page', DEFAULT_PAGE, type=int)
    per_page = request.args.get('per_page', DEFAULT_PER_PAGE, type=int)
    
    total_posts = session.query(Snippets).count()
    total_pages = (total_posts - 1) // per_page + 1
    
    offset = (page - 1) * per_page
    snippets = session.query(Snippets).order_by(Snippets.create_at.desc()).offset(offset).limit(per_page).all()
    
    snippets_list = []
    for snippet in snippets:
        snippet_dict = {
            'id': snippet.id,
            'title': snippet.title,
            'subject': snippet.subject,
            'image': 'http://localhost:5000/api/images/' + snippet.image,
            'reading_time': snippet.reading_time,
            'content': snippet.content,
            'create_at': snippet.create_at.strftime('%B %d, %Y'),
            'update_at': snippet.update_at
        }
        print('image', snippet.image)
        categories = session.query(SnippetsCategories).filter_by(snippet_id=snippet.id).all()
        hashtags = session.query(SnippetsHashtags).filter_by(snippet_id=snippet.id).all()

        snippet_dict['categories'] = [category.category for category in categories]
        snippet_dict['hashtags'] = [hashtag.hashtag for hashtag in hashtags]
        
        snippets_list.append(snippet_dict)
        
    base_url = request.base_url
    
    response = {
        'snippets': snippets_list,
        'total': total_posts,
        'pages': total_pages,
        'prev_url': urljoin(base_url, f'api/snippets?page={page-1}&per_page={per_page}') if page > 1 else None,
        'next_url': urljoin(base_url, f'api/snippets?page={page+1}&per_page={per_page}') if page < total_pages else None
    }
    
    return jsonify(response), 200

@snippets_detail_api.route('/api/snippets/<int:id>', methods=['GET'])
def get_snippet_detail(id):
    from main import authKey, session
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized request'}), 401 
    
    snippet = session.query(Snippets).filter_by(id=id).first()
    if not snippet:
        return jsonify({'message': 'No Content'}), 204
    
    response = {
        'id': snippet.id,
        'title': snippet.title,
        'subject': snippet.subject,
        'image': snippet.image,
        'reading_time': snippet.reading_time,
        'content': snippet.content, 
        'create_at': snippet.create_at.strftime('%B %d, %Y'),
        'update_at': snippet.update_at
    }
    
    category = [pc.category for pc in snippet.snippets_category]
    hashtags = [ph.hashtag for ph in snippet.snippets_hashtags]
    print(hashtags)
    response['category'] = category
    response['hashtags'] = hashtags
    
    return jsonify(response), 200


@snippets_update_api.route('/api/update/snippets/<int:id>', methods=['PUT'])
def update_snippet(id):
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
    
    snippet = session.query(Snippets).filter_by(id=id).first()
    if not snippet:
        return jsonify({'message': 'No content'}), 204
    print('snippet', snippet)
    
    with open('snippets/config.json') as config_file:
        config = json.load(config_file)
        
    image_directory = config['image_directory']
    
    file_path = os.path.join(image_directory, snippet.image)
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
    
    snippet.title = data['title']
    snippet.image = filename
    snippet.reading_time = data['reading_time']
    snippet.subject = data['subject']
    snippet.content = data['content']
    
    for sc in snippet.snippets_category:
        session.delete(sc)
        
    for sh in snippet.snippets_category:
        session.delete(sh)
    
    for sc in snippet.snippets_category:
        session.delete(sc)
        
    for sh in snippet.snippets_hashtags:
        session.delete(sh)

    for sc in data['category'].split(','):
        snippets_category = SnippetsCategories(category=sc)
        snippet.snippets_category.append(snippets_category)
        
    for sh in data['hashtags'].split(','):
        snippets_hashtag = SnippetsHashtags(hashtag=sh)
        snippet.snippets_hashtags.append(snippets_hashtag)
            
    session.commit()
    
    return jsonify({'message': 'Snippet updated successfully', 'info': True}), 200


@snippet_delete_api.route('/api/delete/snippets/<int:id>', methods=['DELETE'])
def delete_snippet(id):
    from main import authKey, session

    print('id', id)
    
    # content_type = request.headers.get('Authorization')
    # if content_type != authKey[0]:
    #     return jsonify({'message': 'Unauthorized Request'}), 401
    
    delete_snippet = session.query(Snippets).filter_by(id=id).first()
    if not delete_snippet:
        return jsonify({'message': 'Snippet not found'}), 404
    print('delete_snippet', delete_snippet.image)
    
    with open('snippets/config.json') as config_file:
        config = json.load(config_file)
    
    image_directory = config['image_directory']
    
    file_path = os.path.join(image_directory, delete_snippet.image)
    print('file_path', file_path)
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print('The file has been deleted')
        else:
            print('The file does not exist')
    except FileNotFoundError as e:
        print(e)
    
    session.query(SnippetsHashtags).filter_by(snippet_id=id).delete()
    session.commit()
    
    session.query(SnippetsCategories).filter_by(snippet_id=id).delete()
    session.commit()
    
    session.delete(delete_snippet)
    session.commit()

    return jsonify({'message': 'Snippet deleted successfully', 'info': True}), 200