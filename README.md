Picture Viewer App

Install
=======

Assuming base directory is $HOME.
Assuming images directory is /data/vpics-images

Code
----
 $ git clone git@github.com:dlink/vpics.git

Database
--------
Create a database and a database base user called vpics:

 $ mysql
 mysql> create database vpics;
 mysql> grant all on vpics.* to vpics@localhost identified by 'bogangles123';
 mysql> exit

 $ cd $HOME/vpics/sql
 $ cat create_all.sql | mysql -uvpics -pbogangles123 vpics

Images
------
Create a directory to house images.  Symlink that into the web/ directory:

 $ mkdir /data/vpics-images
 $ cd $HOME/vpics/web
 $ ln -s /data/vpics-images images

Apache 2
--------
 # cd /etc/apache/sites-available
 # cp ~<USERNAME>/vpics/conf/apache/vpics.conf .

Edit  vpics.conf

 # cd ../sites-enabled
 # ln -s ../sites-available/vpics.conf .
 # /etc/init.d/apache2 restart

Config
------
See vpics/conf/dev.yml


