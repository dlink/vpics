Picture Viewer App

Developed to make Artist Websites easy using only image files.

It consists of Pages and Pics.   Uses Yaml to define metadata for each Page and Pic.

Live sites:
* http://davidlinkart.com
* http://hermanroggeman.com
* http://rickrogersart.com


=======
Given subdirectories of pictures, generate a Website Picture Viewer.

No Database required.

Uses a single yaml config file, called vpics.yaml in the root subdirectory

The Config file can be generated from the given files.

All configuration takes place in the config file

Relies on Unix Know-How.

>>>>>>> yaml_source2

Requirements
------------

- vlib - Python base libraries, [https://github.com/dlink/vlib](https://github.com/dlink/vlib)

- vweb - Python website libraries, - [https://github.com/dlink/vweb](https://github.com/dlink/vweb)

- GraphicsMagick - to create thumbnails.

Install
-------

Assuming base directory is /apps

Assuming images directory is /data/vpics-images

#### Code
The code base is in github.

    $ git clone git@github.com:dlink/vpics.git

###Images

Create a directory to house images.  And make it available via apache

    $ mkdir /data/vpics-images
    $ ln -s /data/vpics-images /www

In it add a subdirectory of images for each 'page' of images you wish to display.

For each subdirectory create a 200px subdirectory and make a copy of each image resized to 200px.  You can do that using graphicsmatick

    $ gm mogrify -resize 200 Place_Setting.jpg

### Apache2

Create two apache configurations.

One for the code base,

Only give visibilty to the web subdirectory.  Eq.:
    $ ln -s /data/apps/vpics/web /data/www/vpics

Apache config requires setting these two environment variables:

    SetEnv PYTHONPATH /apps/vpics/lib
    SetEnv VCONF /data/vpics-images/vpics.yaml

Here are steps using template file:

    # cd /etc/apache/sites-available
    # cp ~<USERNAME>/vpics/conf/apache/vpics.conf .
    # emacs vpics.conf # or vim vpics.conf
    # cd ../sites-enabled
    # ln -s ../sites-available/vpics.conf .
    # /etc/init.d/apache2 restart

You then also need to give apache access to the media directory.  Eq.:

    $ ln -s /data/vpics-images /data/www/

### Configuration

run vpics.py, to create the vpics.yaml file:

    $ /data/apps/vpics/lib/vpics.py update /data/vpics-images

You must then set the media_url attribute:

    $ emacs /data/vpics-images/vpics.yaml



