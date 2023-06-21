create database Tickets;
use Tickets;

create table Area(id_area int not null auto_increment primary key, nombre varchar(100) not null, 
email varchar(100), telefono varchar(100));

create table Prioridad(id_prioridad int not null auto_increment primary key, nombre varchar(100) not null);

create table Estado(id_estado int not null auto_increment primary key, nombre varchar(100) not null);

create table Estado_pedido(id_estado_pedido int not null auto_increment primary key, nombre varchar(100) not null);

create table Articulo(id_articulo int not null auto_increment primary key, nombre varchar(100) not null);

create table Tipo_usuario(id_tipo_usuario int not null auto_increment primary key, nombre varchar(100) not null);

create table Tipo_problema(id_tipo_problema int not null auto_increment primary key, nombre varchar(100) not null);

create table Usuario(id_usuario int not null auto_increment primary key, 
id_tipo_usuario int, foreign key(id_tipo_usuario) references Tipo_usuario(id_tipo_usuario),
 nombre varchar(100) not null, apellido varchar(100) not null, legajo varchar(100) not null,
 email varchar(100) not null, activo boolean not null, 
 nombre_usuario varchar(100) not null, contraseña varchar(100) not null);
 
create table Ticket(id_ticket int not null auto_increment primary key, 
id_usuario int not null, foreign key(id_usuario) references Usuario(id_usuario),
id_area int not null, foreign key(id_area) references Area(id_area),
id_estado int not null, foreign key(id_estado) references Estado(id_estado),
id_prioridad int not null, foreign key(id_prioridad) references Prioridad(id_prioridad),
id_tecnico int, foreign key(id_tecnico) references Usuario(id_usuario),
id_tipo_problema int not null, foreign key(id_tipo_problema) references Tipo_problema(id_tipo_problema),
asunto varchar(100) not null, fecha_inicio date not null, fecha_cierre date not null, descripcion text not null, 
codigo_hardware varchar(100) not null, hora_inicio time not null, hora_cierre time not null);

create table Respuesta(id_respuesta int not null auto_increment primary key, 
id_ticket int not null, foreign key(id_ticket) references Ticket(id_ticket),
id_usuario int not null, foreign key(id_usuario) references Usuario(id_usuario),
fecha date not null, hora time not null, descripcion text not null);

create table Pedido(id_pedido int not null auto_increment primary key,
id_ticket int not null, foreign key(id_ticket) references Ticket(id_ticket),
id_estado_pedido int not null, foreign key(id_estado_pedido) references Estado_pedido(id_estado_pedido),
codigo_pedido varchar(100) not null, fecha_inicio date not null, fecha_cierre date not null,
hora_inicio time not null, hora_cierre time not null);

create table Detalle_pedido(id_detalle_pedido int not null auto_increment primary key, 
id_pedido int not null, foreign key(id_pedido) references Pedido(id_pedido),
id_articulo int not null, foreign key(id_articulo) references Articulo(id_articulo),
id_estado_detalle int not null, foreign key(id_estado_detalle) references Estado_pedido(id_estado_pedido),
descripcion text, modelo_componente varchar(100) not null, cantidad int not null);

insert into Prioridad(nombre) values ('Baja'), ('Media'), ('Alta'), ('Urgente');

insert into Estado(nombre) values ('En espera'), ('En espera componente'), ('Finalizado'), ('Entregado'), ('Archivado');

insert into Estado_pedido(nombre) values ('Pendiente'), ('Parcial'), ('Completado');

insert into Tipo_usuario(nombre) values ('Administrador'), ('Técnico'), ('Normal');

alter table Usuario alter column id_tipo_usuario set default (3);
alter table Usuario alter column activo set default (True);