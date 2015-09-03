Picture Viewer App

Developed to make Artist Websites easy using only image files.

It consists of Pages and Pics.   Uses Yaml to define metadata for each Page and Pic.

Live sites:
* http://davidlinkart.com
* http://hermanroggeman.com

Requirements
------------

- MySQL-python

- vlib - Python base libraries, [https://github.com/dlink/vlib](https://github.com/dlink/vlib)

- vweb - Python website libraries, - [https://github.com/dlink/vweb](https://github.com/dlink/vweb)

Optional:

- GraphicsMagick

Install
-------

Assuming base directory is $HOME.

Assuming images directory is /data/vpics-images

#### Code
The code base is in github.

    $ git clone git@github.com:dlink/vpics.git

### Database
Use Mysql.  Create a database and a database base user called _vpics_.  Create tables:

    $ mysql
    mysql> create database vpics;
    mysql> grant all on vpics.* to vpics@localhost identified by 'bojangles123';
    mysql> exit
    $ cd $HOME/vpics/sql
    $ cat create_all.sql | mysql -uvpics -pbojangles123 vpics

###Images

Create a directory to house images.  Symlink that into the web/ directory:

    $ mkdir /data/vpics-images
    $ cd $HOME/vpics/web
    $ ln -s /data/vpics-images images

### Apache 2
As the root user, copy apache2 config template and edit it:

    # cd /etc/apache/sites-available
    # cp ~<USERNAME>/vpics/conf/apache/vpics.conf .
	# emacs vpics.conf # or vim vpics.conf
    # cd ../sites-enabled
    # ln -s ../sites-available/vpics.conf .
    # /etc/init.d/apache2 restart

### Configuration
See vpics/conf/dev.yml


