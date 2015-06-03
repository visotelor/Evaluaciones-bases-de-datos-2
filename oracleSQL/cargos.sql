DROP TABLE cargos CASCADE CONSTRAINTS
;
CREATE TABLE cargos
(
	id      NUMBER(4) NOT NULL,
	nombre  VARCHAR(50)
)
;


ALTER TABLE cargos ADD CONSTRAINT PK_cargo 
	PRIMARY KEY (id)
;

