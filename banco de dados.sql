CREATE DATABASE estoque;
USE estoque;

CREATE TABLE blusas (
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_tamanho INT,
    id_tecido INT,
    id_cor INT,
    FOREIGN KEY (id_tamanho) REFERENCES tamanhos (id),
    FOREIGN KEY (id_tecido) REFERENCES tecidos (id),
    FOREIGN KEY (id_cor) REFERENCES cores (id)
    );
    
CREATE TABLE tamanhos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    tamanho VARCHAR(5),
    quantidade INT
    ); 
    
CREATE TABLE tecidos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(45)
    );

    
CREATE TABLE cores (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR (45)
    );
   

select * from blusas;

select * from tamanhos;

select * from tecidos;

select * from cores;


SELECT * FROM tamanhos left join blusas  on id_tamanho=tamanhos.id;
SELECT * FROM tecidos left join blusas on id_tecido=tecidos.id;
SELECT * FROM cores left join blusas on id_cor=cores.id;

