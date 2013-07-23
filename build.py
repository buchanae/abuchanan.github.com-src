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


class Page(object):

    def __init__(self, name):
        self.name = name
        self.content_path = os.path.join('content', name + '.md')

        with open(self.content_path) as fh:
            self.raw_content = fh.read()

        self.content = markdowner.convert(self.raw_content)
        self.metadata = self.content.metadata

        self.web_path = self.metadata.get('path', name + '.html').lstrip('/')


def build():

    # Ensure build output directory exists
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)


    # Build pages
    pages = [
        'happy-bday-to-you',
        '3d-tree-v0.1',
        'ready-fire-aim'
    ]
    pages = [Page(name) for name in pages]

    for page in pages:

        template = page.metadata.get('template', 'default-article') + '.html'
        template = env.get_template(template)

        out = template.render({
            'meta': page.metadata,
            'content': str(page.content),
        })

        # TODO detect output path that conflicts with another page

        build_path = os.path.join(BUILD_DIR, page.web_path)

        with open(build_path, 'w') as out_fh:
            out_fh.write(out)


    # Copy first page to index.html
    build_path = os.path.join(BUILD_DIR, pages[0].web_path)
    index_path = os.path.join(BUILD_DIR, 'index.html')
    shutil.copyfile(build_path, index_path)


    # Copy static assests
    for p in ['img', 'css', 'js']:
        dir_util.copy_tree(p, os.path.join(BUILD_DIR, p))


    # Compile and write scss
    with open('css/main.css.scss') as fh:
        css = scss_.compile(fh.read())

        with open('built/css/main.css', 'w') as fh:
            fh.write(css)


if __name__ == '__main__':

    build()
    print 'built'
