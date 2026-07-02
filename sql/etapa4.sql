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

/*View 1: vw_biblioteca_usuario
Consolida os jogos e DLCs que cada usuário possui, juntando Usuario, Biblioteca, 
Armazena e Produto, já trazendo tempo jogado e progresso.*/
 
CREATE VIEW vw_biblioteca_usuario AS
SELECT
    u.id_user,
    u.nickname,
    p.id_produto,
    p.Nome AS nome_produto,
    p.tipo_produto,
    a.tempo_jogado,
    a.data_aqs,
    a.ultima_sessao,
    a.status_progresso
FROM Usuario u
JOIN Biblioteca b ON b.id_user = u.id_user
JOIN Armazena a ON a.id_biblioteca = b.id_biblioteca
JOIN Produto p  ON p.id_produto = a.id_produto;


/*View 2: vw_receita_desenvolvedora 
Consolida, por desenvolvedora, quantos produtos publicou, receita bruta,
cópias vendidas e nota média (juntando Desenvolvedora, Produto, itens_pedidos, 
Pedidos e Review, considerando só pedidos com status = true).*/

CREATE VIEW vw_receita_desenvolvedora AS
SELECT
    d.id_desenvolvedora,
    d.razao_social AS desenvolvedora,
    COUNT(DISTINCT p.id_produto)  AS qtd_produtos_publicados,
    SUM(ip.preco_momento * ip.quantidade) AS receita_total_bruta,
    SUM(ip.quantidade) AS copias_vendidas,
    ROUND(AVG(r.nota), 2) AS qualidade_media_portfolio
FROM Desenvolvedora d
JOIN Produto p ON d.id_desenvolvedora = p.id_desenvolvedora
JOIN itens_pedidos ip ON p.id_produto = ip.id_produto
JOIN Pedidos ped ON ip.id_pedido = ped.id_pedido
LEFT JOIN Review r ON p.id_produto = r.id_produto
WHERE ped.status = true
GROUP BY d.id_desenvolvedora, d.razao_social;



/* TESTE PARA A VIEW 1*/
SELECT * FROM vw_biblioteca_usuario LIMIT 10;

/* TESTE PARA A VIEW 2*/
SELECT * FROM vw_receita_desenvolvedora LIMIT 10;
