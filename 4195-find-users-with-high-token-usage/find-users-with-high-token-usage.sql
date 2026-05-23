# Write your MySQL query statement below
select  user_id , count(prompt) as prompt_count,ROUND(AVG(tokens), 2) AS avg_tokens  from prompts
group by user_id 
having prompt_count>=3 and 
max(tokens)>avg(tokens)
order by avg_tokens desc, user_id;