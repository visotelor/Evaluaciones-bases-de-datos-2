DROP TABLE plantillas CASCADE CONSTRAINTS
;
CREATE TABLE plantillas
(
	id           NUMBER(8) NOT NULL,
	nombre       VARCHAR2(50),
	modificable  CHAR(1),
	eliminada    CHAR(1)
)
;


ALTER TABLE plantillas ADD CONSTRAINT PK_plantilla 
	PRIMARY KEY (id)
;

