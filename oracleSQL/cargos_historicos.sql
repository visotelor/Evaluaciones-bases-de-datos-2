DROP TABLE cargos_historicos CASCADE CONSTRAINTS
;
CREATE TABLE cargos_historicos
(
	fecha_inicio    DATE NOT NULL,
	fecha_fin       DATE,
	funcionario_id  NUMBER(10) NOT NULL,
	cargo_id        NUMBER(4) NOT NULL
)
;


ALTER TABLE cargos_historicos ADD CONSTRAINT FK_cargos_historicos_cargos 
	FOREIGN KEY (cargo_id) REFERENCES cargos (id)
;

ALTER TABLE cargos_historicos ADD CONSTRAINT FK_cargos_historicos_funcionar 
	FOREIGN KEY (funcionario_id) REFERENCES funcionarios (id)
;

