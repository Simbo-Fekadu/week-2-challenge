-- Create Banks Table
create table banks (
   bank_id   number
      generated always as identity
   primary key,
   bank_name varchar2(100) not null unique
);

-- Create Reviews Table
create table reviews (
   review_id        number
      generated always as identity
   primary key,
   bank_id          number not null,
   review_text      varchar2(1000) not null,
   rating           number check ( rating between 1 and 5 ),
   review_date      date,
   source           varchar2(50),
   sentiment_label  varchar2(20),
   sentiment_score  number,
   identified_theme varchar2(100),
   foreign key ( bank_id )
      references banks ( bank_id )
);

-- Insert initial bank data
insert into banks ( bank_name ) values ( 'CBE' );
insert into banks ( bank_name ) values ( 'BOA' );
insert into banks ( bank_name ) values ( 'Dashen' );