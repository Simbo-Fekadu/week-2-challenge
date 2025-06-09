-- Average rating per bank
select b.bank_name,
       round(
          avg(r.rating),
          2
       ) as avg_rating
  from banks b
  left join reviews r
on b.bank_id = r.bank_id
 group by b.bank_name;

-- Sentiment distribution
select b.bank_name,
       r.sentiment_label,
       count(*) as sentiment_count
  from banks b
  left join reviews r
on b.bank_id = r.bank_id
 where r.sentiment_label is not null
 group by b.bank_name,
          r.sentiment_label;

-- Top 5 themes
select identified_theme,
       count(*) as theme_count
  from reviews
 where identified_theme is not null
 group by identified_theme
 order by theme_count desc
 fetch first 5 rows only;

-- Reviews by month
select to_char(
   review_date,
   'YYYY-MM'
) as review_month,
       count(*) as review_count
  from reviews
 where review_date is not null
 group by to_char(
   review_date,
   'YYYY-MM'
)
 order by review_month;