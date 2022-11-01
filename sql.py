CREATE_TABLE_CODE = '''create table if not exists CODE (
   code varchar ,
   redeem boolean, 
   timestamp datetime,
   video varchar,
   primary key(code)
);'''

CREATE_TABLE_VIDEO = '''
create table if not exists VIDEO (
   name varchar,
   url varchar,
   timestamp datetime,
   primary key (url)
);
'''

INSERT_CODE = '''
insert  into CODE (code, redeem, timestamp, video) values  ({}, {}, {}, '{}');
'''

INSERT_VIDEO = '''
insert  into VIDEO (name, url, timestamp) values ('{}', '{}', {});
'''