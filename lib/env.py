import os

import data

class Env(object):

    def __init__(self):
        self.data = data.getInstance()

    @property
    def base_dir(self):
        return os.path.dirname(self.data.config_filename)

    @property
    def base_url(self):
        '''Return base_url for programs'''
        if 'REQUEST_URI' not in os.environ:
            return None
        return os.path.dirname(os.environ['REQUEST_URI']).strip('/')

    @property
    def media_base_url(self):
        '''Return base_url of media suitable for anchor href attributes'''
        return self.data.media_base_url.strip('/')


if __name__ == '__main__':
    env = Env()
    print 'base_dir:', env.base_dir
    print 'base_url:', env.base_url
    print 'media_base_url:', env.media_base_url
