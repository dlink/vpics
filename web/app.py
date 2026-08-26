#!/usr/bin/env python3

import os
from pathlib import Path
from urllib.parse import quote

from flask import abort, Flask, redirect, render_template, request, url_for
from markupsafe import Markup

import data
from pages import Page, PageError, Pages
from pics import Pic

app = Flask(__name__)

dataset = None
pages = None

def configure(config_filename=None, *, thumbnail_dir=None,
              page_columns=None):
    '''Configure this process to serve one vpics portfolio.'''
    global dataset, pages

    filename = config_filename or os.environ.get('VCONF')
    if not filename:
        raise data.DataError('No config and VCONF is not set')

    dataset = data.Data(filename).data
    pages = Pages(dataset)
    app.config['VPICS_DATA'] = dataset
    app.config['VPICS_CONFIG_FILENAME'] = str(filename)
    app.config['VPICS_THUMBNAIL_DIR'] = (
        thumbnail_dir or os.environ.get('VPICS_THUMBNAIL_DIR') or
        dataset.get('thumbnail_dir', '200px'))
    app.config['VPICS_DEFAULT_COLUMNS'] = int(
        dataset.get('num_columns', 3))
    app.config['VPICS_PAGE_COLUMNS'] = parse_page_columns(
        page_columns if page_columns is not None else
        os.environ.get('VPICS_PAGE_COLUMNS', ''))
    return app

def get_page(page_name=None):
    require_configuration()
    try:
        return Page(page_name, dataset) if page_name else pages.first_page
    except PageError:
        abort(404)

def page_context(page):
    columns = app.config['VPICS_PAGE_COLUMNS'].get(
        page.name,
        int(getattr(page, 'num_columns',
                    app.config['VPICS_DEFAULT_COLUMNS'])))
    return {
        'dataset': dataset,
        'pages': pages.list,
        'page': page,
        'columns': columns,
        'thumbnail_dir': app.config['VPICS_THUMBNAIL_DIR'],
        'page_html': Markup(read_page_html(page)),
        'media_path': media_path,
    }

def pic_context(pic_name):
    require_configuration()
    if pic_name not in dataset.pics:
        abort(404)

    picture = Pic(pic_name, dataset)
    page = Page(picture.page_name, dataset)
    page_pictures = page.pics
    position = next(
        index for index, item in enumerate(page_pictures)
        if item.name == picture.name)
    previous_picture = page_pictures[position - 1] if position else None
    next_picture = (
        page_pictures[position + 1]
        if position + 1 < len(page_pictures) else None)
    return {
        'dataset': dataset,
        'pages': pages.list,
        'page': page,
        'picture': picture,
        'previous_picture': previous_picture,
        'next_picture': next_picture,
        'media_path': media_path,
    }

@app.get('/')
def home():
    return redirect(url_for('page', page_name=get_page().name))

@app.get('/page/<page_name>')
def page(page_name):
    return render_template(
        'collection.html', **page_context(get_page(page_name)))

@app.get('/pic/<pic_name>')
def pic(pic_name):
    return render_template('oneup.html', **pic_context(pic_name))

@app.get('/collection.py')
def legacy_collection():
    page_name = request.args.get('id')
    if not page_name:
        page_name = get_page().name
    else:
        get_page(page_name)
    return redirect(url_for('page', page_name=page_name), code=301)

@app.get('/oneup.py')
def legacy_oneup():
    require_configuration()
    pic_name = request.args.get('id')
    if not pic_name or pic_name not in dataset.pics:
        abort(404)
    return redirect(url_for('pic', pic_name=pic_name), code=301)

def require_configuration():
    if dataset is None:
        raise data.DataError('vpics application has not been configured.')

def media_path(media_url, *parts):
    base = '/' + media_url.strip('/')
    encoded = '/'.join(quote(str(part), safe='') for part in parts)
    return '%s/%s' % (base, encoded)

def parse_page_columns(value):
    if not value:
        return {}
    if isinstance(value, dict):
        return {str(name): int(columns) for name, columns in value.items()}
    result = {}
    for setting in str(value).split(','):
        name, separator, columns = setting.partition(':')
        if not separator:
            raise ValueError(
                'VPICS_PAGE_COLUMNS entries must use page:columns')
        result[name.strip()] = int(columns)
    return result

def read_page_html(page):
    if not page.html:
        return ''
    page_dir = Path(dataset.config_filename).resolve().parent / page.name
    filename = (page_dir / page.html.filename).resolve()
    if not filename.is_relative_to(page_dir.resolve()):
        raise data.DataError('Page HTML must remain inside its media directory.')
    try:
        html = filename.read_text(encoding='utf-8')
    except OSError as error:
        raise data.DataError(
            'Unable to read page HTML %s: %s' % (filename, error)) from error
    page_media_url = media_path(dataset.media_url, page.name)
    return html.replace('##MEDIA_URL##', page_media_url)

if os.environ.get('VCONF'):
    configure()

if __name__ == '__main__':
    configure()
    app.run(host='0.0.0.0')
