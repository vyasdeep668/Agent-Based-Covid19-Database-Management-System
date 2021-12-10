drop database AlbertaCovid19;
create database AlbertaCovid19;
use AlbertaCovid19;
drop Table PatientData;
drop Table EditVaccineData;
create Table PatientData (
HCNo int NOT NULL UNIQUE,
PatientName varchar(50) NOT NULL,
DOB varchar(50) NOT NULL,
Address varchar(50) NOT NULL,
Contact  varchar(50),
  PRIMARY KEY (HCNo)
);

ALTER TABLE PatientData ADD PRIMARY KEY (PatientID);

create Table EditVaccineData (
VaccineID int AUTO_INCREMENT NOT NULL,
Name varchar(50) NOT NULL,
HCNo int NOT NULL UNIQUE,
Dose1Type varchar(50) NOT NULL,
Dose1Date varchar(50) NOT NULL,
Dose1Address varchar(50) NOT NULL,
Dose2Type varchar(50) NOT NULL,
Dose2Date varchar(50) NOT NULL,
Dose2Address varchar(50) NOT NULL,
  PRIMARY KEY (VaccineID)
  
);

ALTER TABLE EditVaccineData
ADD CONSTRAINT FK_PatientDataEditVaccineData
FOREIGN KEY (HCNo) REFERENCES PatientData(HCNo)
ON UPDATE CASCADE ON DELETE CASCADE;

drop table EditVaccineData;

drop table PatientData;

INSERT INTO PatientData (PatientName, HCNo, DOB, Address, Contact) VALUES('Sudarsini Tekkam', 344225, '1987-06-04', '3/1 New No.8, 2nd loop st, R. A. Puram, Chennai-28', '8253650387');
INSERT INTO PatientData (PatientName, HCNo, DOB, Address, Contact) VALUES('Gnanasekar Damodaram', 879000, '1987-06-04', '3/1 New No.8, 2nd loop st, R. A. Puram, Chennai-28', '9445328619');
INSERT INTO PatientData (PatientName, HCNo, DOB, Address, Contact) VALUES('Premakumari Gnanasekar', 568999, '1987-06-04', '3/1 New No.8, 2nd loop st, R. A. Puram, Chennai-28',  '9445328619');
INSERT INTO PatientData (PatientName, HCNo, DOB, Address, Contact) VALUES('Indravathi Swamy', 765889, '1987-06-04', '3/1 New No.8, 2nd loop st, R. A. Puram, Chennai-28',  '2493437190');
INSERT INTO PatientData (PatientName, HCNo, DOB, Address, Contact) VALUES('Noor Abid', 9802002, '1987-06-04', '3/1 New No.8, 2nd loop st, R. A. Puram, Chennai-28',  '8253679009');
INSERT INTO PatientData (PatientName, HCNo, DOB, Address, Contact) VALUES('Deep Vyas', 8999000, '1983-07-31', '3/1 New No.8, 2nd loop st, R. A. Puram, Chennai-28', '8799879098');

INSERT INTO EditVaccineData (Name, HCNo, Dose1Type, Dose1Date, Dose1Address, Dose2Type, Dose2Date, Dose2Address) VALUES('Name3', 3, 'D1T3', 'D1D3', 'D1L3', 'D2T3', 'D2D3', 'D2L3');
INSERT INTO EditVaccineData (Name, HCNo, Dose1Type, Dose1Date, Dose1Address, Dose2Type, Dose2Date, Dose2Address ) VALUES('Bela Vyas', (SELECT HCNo FROM PatientData WHERE PatientName ='Bela Vyas'), 'Pfizer', '1945-07-15', 'No.3/1, 2nd loop st, R.A. Puram, Chennai-600028', 'Pfizer', '1945-07-15', 'No.3/1, 2nd loop st, R.A. Puram, Chennai-600028');


select * from patientdata;
select * from EditVaccineData;

Update PatientData set PatientName='Deep1 Vyas', DOB= '1987-05-06' WHERE HCNo=49;
Update EditVaccineData set Name='Deep1 Vyas' WHERE HCNo=49;


DELETE FROM EditVaccineData WHERE Name='Name1' AND HCNo=1;
DELETE FROM EditVaccineData WHERE Name='Name2' AND HCNo=2;
DELETE FROM EditVaccineData WHERE Name='Name2' AND HCNo=2;
DELETE FROM EditVaccineData WHERE Name='Name2' AND HCNo=2;


DELETE FROM PatientData WHERE PatientName='Bela Vyas' AND HCNo=123456;

SELECT * FROM PatientData WHERE PatientName="Bela Vyas" AND HCNo=8999000;
drop table login;
create Table Login(
LoginID int NOT NULL,
UserName varchar(50) NOT NULL unique,
primary key(UserName),
Password varchar(50) NOT NULL
);
Drop table Admin;
create Table Admin(
AdminID int NOT NULL,
Name varchar(50) NOT NULL,
HCNo int NOT NULL,
FOREIGN KEY (HCNo) REFERENCES PatientData(HCNo)
ON UPDATE CASCADE ON DELETE CASCADE,
PRIMARY KEY (AdminID)
);

select * from login;

insert into login (loginID, UserName, Password) values (1, 'sudatekkam', 'Lifeisbeautiful@1');
insert into login (loginID, UserName, Password) values (2, 'prema.gnana', 'Lifeisbeautiful@1');
insert into login (loginID, UserName, Password) values (3, 'gnana.tekkam', 'Lifeisbeautiful@1');


use albertacovid19;

Update PatientData set PatientName='Deep1 Vyas', DOB= '1987-05-06' WHERE HCNo=568999;
delete FROM PatientData WHERE PatientName='Sudarsini Tekkam' AND HCNo=344225;
select * from PatientData;
use AlbertaCovid19;
select * from EditVaccineData;

select * from PatientData;
DELETE FROM EditVaccineData WHERE HCNo=344225;
select * from editvaccinedata;


                    
SELECT HCNo FROM PatientData WHERE PatientName ='Sudarsini Tekkam';
use albertacovid19;
select * from editvaccinedata;
DROP TABLE PatientData;
SELECT * FROM PatientData;
