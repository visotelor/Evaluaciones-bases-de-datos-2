DROP TABLE resultados_preguntas CASCADE CONSTRAINTS
;
CREATE TABLE resultados_preguntas
(
	resultado_id  NUMBER(8) NOT NULL,
	pregunta_id   NUMBER(4) NOT NULL,
	nota          NUMBER(2) NOT NULL
)
;


ALTER TABLE resultados_preguntas ADD CONSTRAINT FK_resultados_pr_resultados_ev 
	FOREIGN KEY (resultado_id) REFERENCES resultados_evaluaciones (id)
;

