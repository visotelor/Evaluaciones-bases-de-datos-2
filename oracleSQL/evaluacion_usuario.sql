DROP TABLE evaluacion_usuario CASCADE CONSTRAINTS
;
CREATE TABLE evaluacion_usuario
(
	evaluado_id    NUMBER(10) NOT NULL,
	evaluacion_id  NUMBER(8) NOT NULL,
	evaluador_id   NUMBER(10)
)
;


ALTER TABLE evaluacion_usuario ADD CONSTRAINT PK_evaluados 
	PRIMARY KEY (evaluado_id, evaluacion_id)
;

ALTER TABLE evaluacion_usuario ADD CONSTRAINT FK_evaluacion_usuario_usuarios 
	FOREIGN KEY (evaluador_id) REFERENCES usuarios (id)
;

ALTER TABLE evaluacion_usuario ADD CONSTRAINT FK_evaluados_evaluacion 
	FOREIGN KEY (evaluacion_id) REFERENCES evaluaciones (id)
;

ALTER TABLE evaluacion_usuario ADD CONSTRAINT FK_evaluados_usuarios 
	FOREIGN KEY (evaluacion_id) REFERENCES usuarios (id)
;

