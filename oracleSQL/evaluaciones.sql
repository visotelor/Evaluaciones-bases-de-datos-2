DROP TABLE evaluaciones CASCADE CONSTRAINTS
;
CREATE TABLE evaluaciones
(
	id             NUMBER(8) NOT NULL,
	periodo        NUMBER(8) NOT NULL,
	fecha_final    DATE NOT NULL,
	fecha_inicial  DATE NOT NULL,
	tiempo_maximo  NUMBER(6) NOT NULL,
	plantilla_id   NUMBER(8)
)
;


ALTER TABLE evaluaciones ADD CONSTRAINT PK_evaluacion 
	PRIMARY KEY (id)
;

ALTER TABLE evaluaciones ADD CONSTRAINT FK_evaluaciones_plantillas 
	FOREIGN KEY (plantilla_id) REFERENCES plantillas (id)
;

