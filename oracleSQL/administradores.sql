DROP TABLE administradores CASCADE CONSTRAINTS
;
CREATE TABLE administradores
(
	id  NUMBER(10) NOT NULL
)
;


ALTER TABLE administradores ADD CONSTRAINT PK_administrador 
	PRIMARY KEY (id)
;

ALTER TABLE administradores ADD CONSTRAINT FK_administrador_usuarios 
	FOREIGN KEY (id) REFERENCES usuarios (id)
;

