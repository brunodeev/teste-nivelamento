CREATE DATABASE IF NOT EXISTS dados_ans;

USE dados_ans;

CREATE TABLE operadoras_ativas (
	Data DATE,
    Reg_Ans INT,
    Cd_Conta_Contabil INT,
    Descricao TEXT,
    VL_Saldo INT,
    VL_Saldo_Final FLOAT
);