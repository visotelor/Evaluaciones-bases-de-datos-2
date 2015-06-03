DROP TABLE funcionarios CASCADE CONSTRAINTS
;
CREATE TABLE funcionarios
(
	id      NUMBER(10) NOT NULL,
	codigo  NUMBER(10) NOT NULL
)
;


ALTER TABLE funcionarios ADD CONSTRAINT PK_funcionarios 
	PRIMARY KEY (id)
;

ALTER TABLE funcionarios ADD CONSTRAINT FK_funcionarios_usuarios 
	FOREIGN KEY (id) REFERENCES usuarios (id)
;

