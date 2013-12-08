-- drop table pics;

set foreign_key_checks = 0;

create table page_pics (
  page_pic_id integer unsigned     not null auto_increment primary key,
  page_id     integer unsigned     not null,
  pic_id      integer unsigned     not null,
  seq_num     integer unsigned     ,

  last_updated timestamp           not null 
        default current_timestamp on update current_timestamp,
  created datetime         default null,

  unique key page_id_pic_id (page_id, pic_id)
) engine InnoDB;

show warnings;

set foreign_key_checks = 1;

select * from page_pics;

