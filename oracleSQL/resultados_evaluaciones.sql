DROP TABLE resultados_evaluaciones CASCADE CONSTRAINTS
;
CREATE TABLE resultados_evaluaciones
(
	id             NUMBER(8) NOT NULL,
	evaluador_id   NUMBER(10) NOT NULL,
	evaluado_id    NUMBER(10) NOT NULL,
	fecha          DATE NOT NULL,
	promedio       NUMBER(5,2) NOT NULL,
	evaluacion_id  NUMBER(8) NOT NULL,
	estado         VARCHAR(50)
)
;


ALTER TABLE resultados_evaluaciones ADD CONSTRAINT PK_resultados_evaluaciones 
	PRIMARY KEY (id)
;

ALTER TABLE resultados_evaluaciones ADD CONSTRAINT FK_resultados_evaluaciones_us1 
	FOREIGN KEY (evaluado_id) REFERENCES usuarios (id)
;

ALTER TABLE resultados_evaluaciones ADD CONSTRAINT FK_resultados_evaluaciones_usu 
	FOREIGN KEY (evaluador_id) REFERENCES usuarios (id)
;

