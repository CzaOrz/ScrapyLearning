from .blog.blog_api import *
from .blog.blog_dom import *

from tools.handler import get


@get('/')
async def index(): return {'__template__': 'index.html'}
