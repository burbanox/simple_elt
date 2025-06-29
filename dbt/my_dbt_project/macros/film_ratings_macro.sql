{% macro generate_film_rating() %}

{{ config(
    materialized='table',
    unique_key='film_id'
)}}

with source as (
    select *
    from {{source('dev','films')}}
)

select film_id,
title,
release_date,
price,
rating,
user_rating,
{{ generate_ratings() }}
from source


{% endmacro %}