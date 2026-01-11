insert into rooms(name, price, capacity)
select * from (select 'Standard', 200000, 2) as tmp
where not exists (select name from rooms where name = 'Standard' limit 1);

insert into rooms(name, price, capacity)
select * from (select 'Hoàng Tử', 500000, 5) as tmp
where not exists (select name from rooms where name = 'Hoàng Tử' limit 1);

insert into rooms(name, price, capacity)
select * from (select 'Công Chúa', 550000, 5) as tmp
where not exists (select name from rooms where name = 'Công Chúa' limit 1);

insert into rooms(name, price, capacity)
select * from (select 'Nhà Vua', 2000000, 10) as tmp
where not exists (select name from rooms where name = 'Nhà Vua' limit 1);

