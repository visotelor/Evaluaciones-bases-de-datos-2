DROP TABLE plantillas_preguntas CASCADE CONSTRAINTS
;
CREATE TABLE plantillas_preguntas
(
	plantilla_id  NUMBER(8) NOT NULL,
	pregunta_id   NUMBER(4) NOT NULL
)
;


ALTER TABLE plantillas_preguntas ADD CONSTRAINT FK_plantilla_preguntas_plantil 
	FOREIGN KEY (plantilla_id) REFERENCES plantillas (id)
;

ALTER TABLE plantillas_preguntas ADD CONSTRAINT FK_plantillas_preguntas_pregun 
	FOREIGN KEY (pregunta_id) REFERENCES preguntas (id)
;

