CREATE DATABASE IF NOT EXISTS dados_ans;

USE dados_ans;

CREATE TABLE cadop (
    Reg_Ans INT PRIMARY KEY,
    CNPJ TEXT,
    Razao_Social TEXT,
    Nome_Fantasia TEXT,
    Modalidade TEXT,
    Logradouro TEXT,
    Numero TEXT,
    Complemento TEXT,
    Bairro TEXT,
    Cidade TEXT,
    UF TEXT,
    CEP INT,
    DDD TEXT,
    Telefone TEXT,
    Fax TEXT,
    Email TEXT,
    Representante TEXT,
    Cargo_Rep TEXT,
    Regiao_de_Com TEXT,
    Data_Reg_Ans DATE
);

LOAD DATA INFILE 'Relatorio_cadop.csv' INTO TABLE cadop
FIELDS TERMINATED BY ';'
IGNORE 1 LINES
(Reg_Ans, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Email, Representante, Cargo_Rep, Regiao_de_Com, Data_Reg_Ans, @dummy);