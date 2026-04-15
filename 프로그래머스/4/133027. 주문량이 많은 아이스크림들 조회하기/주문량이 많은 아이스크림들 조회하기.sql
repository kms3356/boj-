-- 코드를 입력하세요
select flavor from (
    select f.flavor, RANK() over(order by (f.total_order+m.합계) desc) as rnk from first_half f join (
        SELECT flavor, sum(total_order) as 합계 from july group by flavor) m on f.flavor = m.flavor) where rnk in (1,2,3)