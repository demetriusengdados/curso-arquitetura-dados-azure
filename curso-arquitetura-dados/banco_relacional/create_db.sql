-- Criação do banco de dados curso_engenharia_dados
CREATE DATABASE curso_engenharia_dados
ON PRIMARY
(
    NAME = curso_engenharia_dados_data,
    FILENAME = 'C:\SQLServerData\curso_engenharia_dados.mdf', -- Caminho do arquivo de dados
    SIZE = 1000MB, -- Tamanho inicial do arquivo
    MAXSIZE = 10000MB, -- Tamanho máximo do arquivo
    FILEGROWTH = 100MB -- Incremento no crescimento do arquivo
)
LOG ON
(
    NAME = curso_engenharia_dados_log,
    FILENAME = 'C:\SQLServerData\curso_engenharia_dados_log.ldf', -- Caminho do arquivo de log
    SIZE = 5MB, -- Tamanho inicial do log
    MAXSIZE = 50MB, -- Tamanho máximo do log
    FILEGROWTH = 5MB -- Incremento no crescimento do log
);
GO

-- Selecionar o banco criado para execução de comandos
USE curso_engenharia_dados;
GO

-- Exibir a mensagem de sucesso
PRINT 'Banco de dados curso_engenharia_dados criado com sucesso!';
