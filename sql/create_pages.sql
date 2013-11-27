-- drop table pages;

set foreign_key_checks = 0;

create table pages (
  page_id integer unsigned     not null auto_increment primary key,
  name varchar(30)        not null,
  last_updated timestamp       not null 
        default current_timestamp on update current_timestamp,
  created datetime         default null,

  unique key name (name)
) engine InnoDB;

show warnings;

set foreign_key_checks = 1;

select * from pages;

