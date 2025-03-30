CREATE DATABASE IF NOT EXISTS dados_ans;

USE dados_ans;

CREATE TABLE operadoras_ativas (
	Data DATE,
    Reg_Ans INT,
    Cd_Conta_Contabil INT,
    Descricao TEXT,
    VL_Saldo FLOAT,
    VL_Saldo_Final FLOAT
);

SELECT * FROM operadoras_ativas
WHERE Descricao LIKE 'OUTROS DÉBITOS DE OPERAÇÕES COM PLANOS DE ASSISTÊNCIA MÉDICO HOSPITALAR'
OR Descricao LIKE 'Despesas Financeiras com Operações de Assistência Médico-Hospitalar'
OR Descricao LIKE 'DESPESAS FINANCEIRAS COM OPERAÇÕES DE ASSISTÊNCIA MÉDICO-HOSPITALAR';

LOAD DATA INFILE '1T2023_formatado.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);