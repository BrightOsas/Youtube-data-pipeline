{{ config(
    materialized = 'table'
)}}

with snippetdata as (
    select * from {{ ref('snippet')}}
),

statsata as (
    select * from {{ref('stats')}}
),

dimcountry as (
    select * from {{ ref ('country')}}
)

select
    sp.id,
    sp.title,
    sp.publishedate,
    st.views,
    st.subscribers,
    st.videos,
    value as country

from snippetdata sp
full join statsata st on sp.id = st.id

left join dimcountry dm
on sp.country = dm.id