{{ config(
    materialized='table',
    unique_key='actor_id'
)}}

SELECT *
FROM {{source('dev','actors')}}