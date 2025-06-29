{% macro generate_ratings() %}

case
    when user_rating >=4.5 then 'EXCELENT'
    when user_rating >=4.0 then 'GOOD'
    when user_rating >=3.0 then 'AVERAGE'
    ELSE 'POOR'
end as rating_category

{% endmacro %}