DROP TABLE estructuras CASCADE CONSTRAINTS
;
CREATE TABLE estructuras
(
	id              NUMBER(10) NOT NULL,
	dependencia_id  NUMBER(10),
	director_id     NUMBER(4)
)
;


ALTER TABLE estructuras ADD CONSTRAINT PK_estructuras 
	PRIMARY KEY (id)
;

ALTER TABLE estructuras ADD CONSTRAINT FK_estructuras_cargos 
	FOREIGN KEY (director_id) REFERENCES cargos (id)
;

ALTER TABLE estructuras ADD CONSTRAINT FK_estructuras_estructuras 
	FOREIGN KEY (dependencia_id) REFERENCES estructuras (id)
;

ALTER TABLE estructuras ADD CONSTRAINT FK_estructuras_usuarios 
	FOREIGN KEY (id) REFERENCES usuarios (id)
;

