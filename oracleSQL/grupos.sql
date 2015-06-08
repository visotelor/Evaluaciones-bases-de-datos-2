DROP TABLE grupos CASCADE CONSTRAINTS
;
CREATE TABLE grupos
(
	id             NUMBER(10) NOT NULL,
	asignatura_id  NUMBER(6) NOT NULL,
	docente_id     NUMBER(10) NOT NULL,
	periodo        NUMBER(8)
)
;


ALTER TABLE grupos ADD CONSTRAINT PK_grupo 
	PRIMARY KEY (id)
;

ALTER TABLE grupos ADD CONSTRAINT FK_grupo_asignaturas 
	FOREIGN KEY (asignatura_id) REFERENCES asignaturas (id)
;

ALTER TABLE grupos ADD CONSTRAINT FK_grupos_funcionarios 
	FOREIGN KEY (docente_id) REFERENCES funcionarios (id)
;

