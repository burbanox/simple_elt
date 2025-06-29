{{config(
    materialized='table'
)}}

with actors as(
    SELECT *
    FROM {{source('dev','actors')}}
),

films as (
    SELECT *
    FROM {{source('dev','films')}}
),

film_actor as (
    SELECT *
    FROM {{source('dev','film_actors')}}
),

film_rating as (
    SELECT * 
    FROM {{ref('film_rating')}}
)


select *
from film_rating
left join film_actor using (film_id)
left join actors using (actor_id)