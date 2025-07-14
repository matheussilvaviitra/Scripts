import os

def ler_tabelas_para_set(caminho_arquivo: str) -> set:
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return {linha.strip() for linha in f if linha.strip()}
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return set()

def comparar_listas_de_tabelas(arquivo_antigo: str, arquivo_novo: str, arquivo_saida: str):
    tabelas_antigas = ler_tabelas_para_set(arquivo_antigo)
    tabelas_novas = ler_tabelas_para_set(arquivo_novo)

    if not tabelas_antigas and not tabelas_novas:
        print("Não foi possível ler os arquivos de entrada. A operação foi cancelada.")
        return

    tabelas_removidas = sorted(list(tabelas_antigas - tabelas_novas))
    tabelas_adicionadas = sorted(list(tabelas_novas - tabelas_antigas))

    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write("Tabelas REMOVIDAS (presentes na versão ANTIGA, mas não na NOVA):\n")
            f.write("===================================================================\n")
            if tabelas_removidas:
                for tabela in tabelas_removidas:
                    f.write(f"{tabela}\n")
            else:
                f.write("Nenhuma.\n")
            
            f.write("\n\n----------------------\n\n")

            f.write("Tabelas ADICIONADAS (presentes na versão NOVA, mas não na ANTIGA):\n")
            f.write("=================================================================\n")
            if tabelas_adicionadas:
                for tabela in tabelas_adicionadas:
                    f.write(f"{tabela}\n")
            else:
                f.write("Nenhuma.\n")

        print(f"Relatório de comparação gerado com sucesso em '{arquivo_saida}'")

    except Exception as e:
        print(f"Ocorreu um erro ao escrever o arquivo de saída: {e}")


comparar_listas_de_tabelas('list_full_tables_old.txt', 'list_full_tables_current.txt', 'tables_diff.txt')
