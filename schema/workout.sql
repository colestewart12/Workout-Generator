create table if not exists workout (
    title text primary key,
    descrip text null,
    type text not null,
    bodypart text not null,
    equipment text not null,
    level text not null
)