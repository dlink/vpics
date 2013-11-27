-- As of Mysql 5.something, you must specify --local-infile=1

delete from page_pics;
delete from pics;
delete from pages;

load data local infile 'data/pages.csv' into table pages
fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

load data local infile 'data/pics.csv' into table pics
   fields terminated by ',' optionally enclosed by '"' ignore 1 lines; 

load data local infile 'data/page_pics.csv' into table page_pics
   fields terminated by ',' optionally enclosed by '"' ignore 1 lines;
