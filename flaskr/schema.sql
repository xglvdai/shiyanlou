drop table if exists enteries;
create table entries(
    id integer primary key autoincrement,
    title string not null,
    text string not null
);
