DROP TABLE preguntas CASCADE CONSTRAINTS
;
CREATE TABLE preguntas
(
	id        NUMBER(4) NOT NULL,
	pregunta  VARCHAR(2000) NOT NULL
)
;


ALTER TABLE preguntas ADD CONSTRAINT PK_preguntas 
	PRIMARY KEY (id)
;

