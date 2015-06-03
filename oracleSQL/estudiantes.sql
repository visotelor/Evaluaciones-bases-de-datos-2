DROP TABLE estudiantes CASCADE CONSTRAINTS
;
CREATE TABLE estudiantes
(
	id             NUMBER(10) NOT NULL,
	codigo         NUMBER(10) NOT NULL,
	estructura_id  NUMBER(10) NOT NULL,
	tesis_id       NUMBER(8)
)
;


ALTER TABLE estudiantes ADD CONSTRAINT PK_estudiantes 
	PRIMARY KEY (id)
;

ALTER TABLE estudiantes ADD CONSTRAINT FK_estudiantes_estructuras 
	FOREIGN KEY (estructura_id) REFERENCES estructuras (id)
;

ALTER TABLE estudiantes ADD CONSTRAINT FK_estudiantes_usuarios 
	FOREIGN KEY (id) REFERENCES usuarios (id)
;

