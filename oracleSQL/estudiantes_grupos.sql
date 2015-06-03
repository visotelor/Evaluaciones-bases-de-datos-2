DROP TABLE estudiantes_grupos CASCADE CONSTRAINTS
;
CREATE TABLE estudiantes_grupos
(
	estudiante_id  NUMBER(10) NOT NULL,
	grupo_id       NUMBER(10) NOT NULL
)
;


ALTER TABLE estudiantes_grupos ADD CONSTRAINT FK_estudiantes_grupos_estudian 
	FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id)
;

ALTER TABLE estudiantes_grupos ADD CONSTRAINT FK_estudiantes_grupos_grupos 
	FOREIGN KEY (grupo_id) REFERENCES grupos (id)
;

