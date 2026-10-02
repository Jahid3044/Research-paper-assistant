create extension if not exists vector;

create table users (
    id uuid primary key,
    email text unique not null,
    password_hash text not null,
    created_at timestamptz default now()
);

create table papers (
    id uuid primary key,
    user_id uuid references users(id) on delete cascade,
    filename text not null,
    title text,
    authors text,
    abstract text,
    full_text text,
    summary text,
    research_gaps text,
    created_at timestamptz default now()
);

create table paper_chunks (
    id bigserial primary key,
    paper_id uuid references papers(id) on delete cascade,
    page_number integer,
    chunk_index integer,
    content text,
    embedding vector(1536)
);

create table notes (
    id uuid primary key,
    user_id uuid references users(id) on delete cascade,
    paper_id uuid references papers(id) on delete cascade,
    title text,
    content text,
    created_at timestamptz default now()
);