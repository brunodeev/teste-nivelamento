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

SELECT
    Reg_Ans,
    SUM(VL_SALDO_FINAL) AS total_despesas
FROM 
    operadoras_ativas
WHERE 
    CD_CONTA_CONTABIL LIKE '4421190%'
    AND DATA >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY 
    Reg_Ans
HAVING 
    total_despesas < 0
ORDER BY 
    total_despesas ASC
LIMIT 10;

LOAD DATA INFILE '1T2023.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '2T2023.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '3T2023.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '4T2023.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '1T2024.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '2T2024.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '3T2024.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);

LOAD DATA INFILE '4T2024.csv' INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Data, Reg_Ans, Cd_Conta_Contabil, Descricao, VL_Saldo, VL_Saldo_Final, @dummy);