create table supplier(
    SNO text primary key,
    SNAME text,
    status integer,
    city text
);

insert into supplier (SNO,status, SNAME,CITY) VALUES
('S1','Smith',20,'London'),
('S2','John',30,'Paris'),
('S3','Lora',2,'Paris'),
('S4','Peter',18,'London'),
('S5','Jake',25,'london');

SELECT * FROM supplier;