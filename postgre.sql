create table users(
    ci int primary key,
    name varchar(100) not null,
    lastName varchar(100),
    email varchar(100) not null unique,
    password varchar(255) not null,
    jwi varchar(32) default null
);

create table tareas(
    id serial primary key ,
    title varchar not null,
    description text not null,
    userCi int not null,
    isDeleted bool not null default false,
    foreign key (userCi) references users(ci)
);

insert into users (ci, name, lastName, email, password) values
    (11111111, 'Martin', 'Mujica', 'martin@example.com', '1234');

insert into tareas (title, description, userCi) values
    ('Prueba', 'Esto es alta prueba muy pruebosa', 11111111);

select tareas.id, tareas.title, tareas.description, users.email from tareas
    join users on tareas.userCi = users.ci
        where users.ci = 11111111 and tareas.isDeleted = false;