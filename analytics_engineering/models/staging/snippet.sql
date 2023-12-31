{{config(
    materialize='view'
)}}

select
    publishedate,
    id,
    REPLACE(title, ' - Topic','') AS title,
    COALESCE(NULLIF(country, ''), 'aa') AS country

from {{source ('staging','channelsnippet')}}