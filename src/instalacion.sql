CREATE TABLE dam1(
id INT PRIMARY KEY,
nombre VARCHAR(10),
apellidos TEXT,
asignaturas TEXT,
media INT,
aprobado BOOLEAN
);

INSERT INTO dam1 VALUES (1,'Sergio','Buendia Colao','PRO ED INGLES',5,TRUE)
,(2,'Miguel','Platon cano','PRO ED INGLES',4,FALSE),
(3,'Pablo','Paraiso','PRO BD XML FOL ED INGLES',7,TRUE),
(4,'Jorge','CASAS','PRO BD XML FOL ED INGLES',9,TRUE),
(5,'Jorge','Sancho','PRO ED INGLES',6,TRUE);
