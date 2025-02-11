-- init_database.sql

INSERT INTO types (id, name) VALUES
  (1, 'Criador'),
  (2, 'Admin'),
  (3, 'Regular');

INSERT INTO statuses (id, name) VALUES
  (1, 'Completo'),
  (2, 'Em andamento'),
  (3, 'A ser iniciado'),
  (4, 'Fechado');

INSERT INTO priorities (id, name) VALUES
  (1, 'Urgente'),
  (2, 'Alta'),
  (3, 'Média'),
  (4, 'Baixa');

INSERT INTO difficulties (id, name) VALUES
  (1, 'Difícil'),
  (2, 'Médio'),
  (3, 'Fácil');

INSERT INTO task_types (id, name) VALUES
  (1, 'Bugfix'),
  (2, 'Refatoração'),
  (3, 'Documentação'),
  (4, 'Organização'),
  (5, 'Desenvolvimento');

INSERT INTO scholarships (id, name) VALUES
  (1, 'Voluntário'),
  (2, 'Remunerado');
