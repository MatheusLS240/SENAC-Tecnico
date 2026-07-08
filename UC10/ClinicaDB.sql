CREATE DATABASE clinica;
USE clinica;

CREATE TABLE paciente (
	idPaciente INT AUTO_INCREMENT PRIMARY KEY,
    nomePaciente VARCHAR(50) NOT NULL,
    cpfPaciente VARCHAR(13) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(15) NOT NULL, 
    dataNascinento DATE NOT NULL
);

CREATE TABLE medico (
	idMedico INT AUTO_INCREMENT PRIMARY KEY,
    nomeMedico VARCHAR(50) NOT NULL,
    crm VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    especialista ENUM("Pediatria", "Oftalmologia", "Cardiologia", "Dermatologia") NOT NULL DEFAULT "Dermatologia",
    dataCadastro DATE DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE agendamento (
	idAgendamento INT AUTO_INCREMENT PRIMARY KEY,
	idPaciente INT NOT NULL,
    idMedico INT NOT NULL,
    dataConsulta DATE NOT NULL,
    horaConsulta TIME NOT NULL,
    dataHoraAgendamento DATETIME DEFAULT CURRENT_TIMESTAMP() NOT NULL
);

ALTER TABLE agendamento
ADD CONSTRAINT fk_agendamento_pk_paciente
FOREIGN KEY agendamento(idPaciente)
REFERENCES paciente(idPaciente);

ALTER TABLE agendamento
DROP FOREIGN KEY fk_agendamento_paciente;

ALTER TABLE agendamento
ADD CONSTRAINT fk_agendamento_pk_medico
FOREIGN KEY agendamento(idMedico)
REFERENCES medico(idMedico);

ALTER TABLE agendamento
DROP FOREIGN KEY fk_agendamento_medico;

SELECT * FROM paciente;

INSERT INTO paciente(nomePaciente, cpfPaciente, email, telefone, dataNascinento)
VALUES ("Julia", "110987654331", "vidaMiinha@gmail.com", "22982004", "2010-03-05"); 

UPDATE paciente SET telefone = "8291641" WHERE idPaciente = 5;
DELETE FROM paciente WHERE idPaciente = 5;

INSERT INTO paciente (nomePaciente, cpfPaciente, email, telefone, dataNascinento)
VALUES
("Julia Souza", "11098765433", "julia@gmail.com", "22982004", "2010-03-05"),
("Carlos Silva", "12345678901", "carlos@gmail.com", "11987654321", "1995-08-15");

INSERT INTO medico (nomeMedico, crm, email, especialista)
VALUES
("Fernanda Lima", "CRM12345", "fernanda@clinica.com", "Cardiologia"),
("Ricardo Alves", "CRM67890", "ricardo@clinica.com", "Dermatologia");

INSERT INTO agendamento (idPaciente, idMedico, dataConsulta, horaConsulta)
VALUES
(1, 1, "2026-07-10", "09:00:00"),
(2, 2, "2026-07-11", "14:30:00");

INSERT INTO agendamento(idPaciente, idMedico, dataConsulta, horaConsulta)
VALUES (1, 1, "2026-05-10", "10:30");

UPDATE agendamento SET horaConsulta = "08:00" WHERE idAgendamento = 3;

DELETE FROM agendamento WHERE idAgendamento = 2;

SELECT * FROM agendamento;