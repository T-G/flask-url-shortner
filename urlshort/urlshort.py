from flask import render_template, request,abort, redirect, url_for, flash, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

urlshort_bp = Blueprint('urlshort', __name__)


@urlshort_bp.route('/')
def index_view():
    return render_template('index.html', codes = session.keys())

@urlshort_bp.route('/your_url', methods=['POST', 'GET'])
def your_url_view():
    if request.method == 'POST':
        # Create an empty object
        urls = {}

        # Check if the url.json alerady exist
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        # if exists then return to index
        if request.form['code'] in urls.keys():
            flash('That short name has already been taken , please choose another name!')
            return redirect(url_for('urlshort.index_view'))

        # check if the user choose the url or file field
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_file_name = f"{request.form['code']}_{secure_filename(f.filename)}"
            f.save('/home/theo/workspace/url-shortner/urlshort/static/user_files/' + full_file_name)
            urls[request.form['code']] = { 'file' : full_file_name }

        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
            # Saving Session Variable
            session[request.form['code']] = True
                        
        return render_template('your_url.html', code=request.form['code'])
    
    else:
        return redirect(url_for('urlshort.index_view'))

# search for any sort of string and put it in a variable name code
@urlshort_bp.route('/<string:code>')
def redirect_to_url(code):
    # check if the file exists : urls.json
    if os.path.exists('urls.json'):
        with open('urls.json', 'r') as urls_file:
            urls = json.load(urls_file)
            # check if the code that was entered by user matches in the file
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('urlshort/static', filename='user_files/' + urls[code]['file'])  ) 

    return abort(404)

@urlshort_bp.errorhandler(404)
def page_not_found_view(error):
    return render_template('page_not_found.html'), 404



@urlshort_bp.route('/about')
def about_view():
    return render_template('about.html')


@urlshort_bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))


if __name__ == '__main__':
    urlshort_bp.run(debug=True)