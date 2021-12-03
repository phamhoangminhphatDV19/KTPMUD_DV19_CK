-- a) Truy suất tổng điểm (grade) cho mỗi thành phố (city)
SELECT city, SUM(grade) AS "Tong diem"
FROM customer
GROUP BY city;

-- b) Truy suất tất cả khách hàng (customer) mà có người môi giới (sales_man) tương ứng có hoa hồng >0,12, sắp xếp theo customer_id
select * from customer c
join salesman s on c.salesman_id = s.salesman_id
where s.commission > 0.12
order by s.commission