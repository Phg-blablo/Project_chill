use booking_system;
create table if not exists rooms(
	id int auto_increment primary key,
    name varchar(50) not null,
    price decimal(10, 2) not null,
    capacity int not null
);

create table if not exists bookings(
	id int auto_increment primary key,
    customer_name varchar(100) not null,
    room_id int,
    nights int,
    total_guest int,
    total_price int,
    created_at datetime,
    foreign key (room_id) references rooms(id)
);
