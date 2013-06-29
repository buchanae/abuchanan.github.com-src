from distutils import dir_util
import logging
import os
import shutil

import jinja2
import markdown2
import scss


logger = logging.getLogger('scss')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

loader = jinja2.FileSystemLoader('templates')
env = jinja2.Environment(loader=loader)

markdowner = markdown2.Markdown(extras=['metadata'])

BUILD_DIR = 'built'

scss_ = scss.Scss(search_paths=[
    'third-party/compass/frameworks/compass/stylesheets/',
    'third-party/compass/frameworks/blueprint/stylesheets/',
], scss_opts={
    'compress': False,
})


def build():
    template = env.get_template('default.html')

    with open('content/index.md') as fh:
        raw = fh.read()

    content = markdowner.convert(raw)
    out = template.render({
        'meta': content.metadata,
        'content': str(content),
    })

    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    path = content.metadata['path']
    path = path.lstrip('/')
    path = os.path.join(BUILD_DIR, path)

    for p in ['img', 'css', 'js']:
        dir_util.copy_tree(p, os.path.join(BUILD_DIR, p))

    with open(path, 'w') as out_fh:
        out_fh.write(out)

    with open('css/main.css.scss') as fh:
        css = scss_.compile(fh.read())

        with open('built/css/main.css', 'w') as fh:
            fh.write(css)


if __name__ == '__main__':

    build()
