DROP TABLE tesis CASCADE CONSTRAINTS
;
CREATE TABLE tesis
(
	id           NUMBER(8) NOT NULL,
	nombre       VARCHAR2(100) NOT NULL,
	jurado_id    NUMBER(10),
	director_id  NUMBER(10)
)
;


ALTER TABLE tesis ADD CONSTRAINT PK_tesis 
	PRIMARY KEY (id)
;

ALTER TABLE tesis ADD CONSTRAINT FK_tesis_funcionarios 
	FOREIGN KEY (director_id) REFERENCES funcionarios (id)
;

ALTER TABLE tesis ADD CONSTRAINT FK_tesis_jurado 
	FOREIGN KEY (jurado_id) REFERENCES funcionarios (id)
;

