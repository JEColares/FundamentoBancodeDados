-- ==========================================
-- 1. CONFIGURAÇÃO DO USUÁRIO ADMINISTRADOR
-- ==========================================

-- Cria o usuário admin_user com uma senha segura
CREATE USER admin_user WITH PASSWORD 'admin123';

-- Concede permissão de uso no esquema public
GRANT USAGE ON SCHEMA public TO admin_user;

-- Concede TODOS os privilégios (SELECT, INSERT, UPDATE, DELETE) em todas as tabelas
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin_user;

-- Concede privilégios em sequências (necessário para os campos SERIAL como id_user, id_produto, etc.)
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO admin_user;


-- ==========================================
-- 2. CONFIGURAÇÃO DO USUÁRIO SOMENTE LEITURA
-- ==========================================
    
-- Cria o usuário auditor_user com uma senha segura
CREATE USER auditor_user WITH PASSWORD 'auditor123';

-- Concede permissão de uso no esquema public
GRANT USAGE ON SCHEMA public TO auditor_user;

-- Concede APENAS a permissão de consulta (SELECT) em todas as tabelas
GRANT SELECT ON ALL TABLES IN SCHEMA public TO auditor_user;

-- Garante explicitamente que este usuário NÃO pode fazer alterações por motivos de segurança
REVOKE INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM auditor_user;