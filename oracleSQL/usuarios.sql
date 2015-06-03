DROP TABLE usuarios CASCADE CONSTRAINTS
;
CREATE TABLE usuarios
(
	id          NUMBER(10) NOT NULL,
	email       VARCHAR(50),
	contrasena  VARCHAR(50),
	nombre      VARCHAR2(100) NOT NULL,
	habilitado  CHAR(1) NOT NULL,
	username    VARCHAR(50) NOT NULL
)
;


ALTER TABLE usuarios
	ADD CONSTRAINT UQ_usuarios_email UNIQUE (email)
;

ALTER TABLE usuarios
	ADD CONSTRAINT UQ_usuarios_habilitado UNIQUE (habilitado)
;

ALTER TABLE usuarios
	ADD CONSTRAINT UQ_usuarios_username UNIQUE (username)
;

ALTER TABLE usuarios ADD CONSTRAINT PK_usuarios 
	PRIMARY KEY (id)
;

