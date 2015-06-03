DROP TABLE asignaturas CASCADE CONSTRAINTS
;
CREATE TABLE asignaturas
(
	id      NUMBER(6) NOT NULL,
	nombre  VARCHAR(50) NOT NULL
)
;


ALTER TABLE asignaturas
	ADD CONSTRAINT UQ_asignaturas_id UNIQUE (id)
;

ALTER TABLE asignaturas ADD CONSTRAINT PK_asignaturas 
	PRIMARY KEY (id)
;

