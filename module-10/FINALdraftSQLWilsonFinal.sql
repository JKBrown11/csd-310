--Written by Gabe, updated by Amanda 
CREATE DATABASE wilson_financial;
USE wilson_financial;

--creating clients table:--

CREATE TABLE clients (
  client_id INT NOT NULL AUTO_INCREMENT,
  f_name VARCHAR(45) NOT NULL,
  l_name VARCHAR(45) NOT NULL,
  date_added DATE NOT NULL,
  PRIMARY KEY (client_id));

--creating accounts table:--

CREATE TABLE accounts (
account_id INT NOT NULL AUTO_INCREMENT,
client_id INT NOT NULL,
account_type ENUM('low-risk', 'high-risk', 'retirement'),
PRIMARY KEY (account_id),
INDEX client_id_idx (client_id ASC),
CONSTRAINT client_id
  FOREIGN KEY (client_id)
  REFERENCES clients (client_id));

ALTER TABLE accounts AUTO_INCREMENT=100;

--creating transactions table:--

CREATE TABLE transactions (
  trans_id INT NOT NULL AUTO_INCREMENT,
  client_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  amount INT NOT NULL,
  account_id INT NOT NULL,
  PRIMARY KEY (trans_id),
  INDEX t_client_id_idx (client_id ASC),
  CONSTRAINT t_client_id
    FOREIGN KEY (client_id)
    REFERENCES clients (client_id),
  INDEX account_id (account_id ASC),
  CONSTRAINT account_id
    FOREIGN KEY (account_id)
    REFERENCES clients (client_id));

  ALTER TABLE transactions AUTO_INCREMENT=1000;

--populating clients table:--

INSERT INTO clients
(f_name, l_name, date_added)
VALUES 
('Bob', 'Sanchez', '2023-03-09'),
('Alice', 'Johnson', '2023-04-15'),
('Carlos', 'Diaz', '2023-05-22'),
('Emily', 'Brighton', '2023-06-05'),
('David', 'Smith', '2023-12-01'),
('Elena', 'Martinez', '2024-01-02');


--populating transactions table:--


  LOAD DATA INFILE "/transactionsUPDATED.csv"
  INTO TABLE transactions
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;


--populating accounts table. Two clients have two accounts, the rest have 1.--

INSERT INTO accounts
(client_id, account_type)
VALUES
(1, 'high-risk'),
(1, 'low-risk'),
(2, 'high-risk'),
(3, 'low-risk'),
(4, 'high-risk'),
(4, 'low-risk'),
(5, 'retirement'),
(6, 'retirement');