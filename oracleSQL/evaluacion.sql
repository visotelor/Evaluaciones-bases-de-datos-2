DROP TABLE evaluacion CASCADE CONSTRAINTS
;
CREATE TABLE evaluacion
(
	id             NUMBER(8) NOT NULL,
	periodo        NUMBER(8) NOT NULL,
	fecha_final    DATE NOT NULL,
	fecha_inicial  DATE NOT NULL,
	tiempo_maximo  NUMBER(6) NOT NULL,
	plantilla_id   NUMBER(8)
)
;


ALTER TABLE evaluacion ADD CONSTRAINT PK_evaluacion 
	PRIMARY KEY (id)
;

