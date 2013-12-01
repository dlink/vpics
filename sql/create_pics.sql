-- drop table pics;

set foreign_key_checks = 0;

create table pics (
  pic_id       integer unsigned     not null auto_increment primary key,
  name         varchar(30)          not null,
  filename     varchar(256)         not null,
  caption      varchar(512)         ,
  description  varchar(1024)        ,

  last_updated timestamp         not null 
        default current_timestamp on update current_timestamp,
  created datetime         default null,

  unique key name (name)
) engine InnoDB;

show warnings;

set foreign_key_checks = 1;

select * from pics;

