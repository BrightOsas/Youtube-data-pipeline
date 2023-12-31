{{ config(
    materialize = 'view'
)}}

SELECT 
    id,
    CAST(viewcounts as numeric) as views,
    cast(subscribercounts as numeric) as subscribers,
    CAST(videocounts as numeric) as videos

FROM {{source ('staging','channelstat')}}