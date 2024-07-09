--Miguel Madueño Sanz

--1

CREATE TABLE Temporada(
idserie int not null,
numTemporada int not null,
fechaEstreno date not null,
fechaRegistro date not null,
disponible int not null,
PRIMARY KEY (idserie, numTemporada),
CHECK (disponible in (0,1)),
CHECK (fechaRegistro > fechaEstreno),
FOREIGN KEY (idserie) REFERENCES series(idSerie)
);

--2
ALTER TABLE profesiones ADD descripcion char null;
--3
CREATE INDEX idx_titu ON series (titulo,anyoFin);
--4
select s.idserie, s.titulo, s.tituloOriginal, s.sinopsis from series s
order by s.titulo desc;
--5
select u.* from usuarios u
where u.pais in ('Francia','Noruega');
--6
select a.*, s.* from actores a
    join reparto r on a.idActor = r.idActor
    join series s on s.idSerie = r.idSerie
--7
select u.* from usuarios u
where u.idUsuario not in (select v.idUsuario from valoraciones v);
--8
select u.*,p.* from usuarios u 
right join profesiones p on u.idProfesion = p.idProfesion;
--9
select s.* from series s 
where s.idIdioma in (select i.idIdioma from idiomas i where i.idioma = 'Español') 
    and  (s.titulo like ('E%') or s.titulo like ('G%')) ;
--10
select s.idSerie, s.titulo, s.sinopsis, MAX(v.puntuacion) maxPuntuacion, MIN(v.puntuacion) minPuntuacion, AVG(v.puntuacion) avgPuntuacion
from series s
join valoraciones v on s.idSerie = v.idSerie
group by s.idSerie, s.titulo, s.sinopsis;
--11
update series set sinopsis = 'Sin sinopsis'
    where sinopsis is null and idIdioma in (select i.idIdioma from idiomas i where i.idioma = 'Inglés');
--12
select v.*, u.nombre ||' '||u.apellido1 ||' '|| ifnull(u.apellido2,'') as NombreCompleto, AVG(v.puntuacion)  OVER
(PARTITION BY v.idUsuario) as PuntuacionMedia 
from valoraciones v
join usuarios u on u.idUsuario = v.idUsuario;

