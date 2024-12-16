import subprocess
from kitano import puts 
# Lista de arquivos para execução
arquivos = [
    "send_dev.py",
    "send_fofoca.py",
    "send_geek.py",
    "send_news.py",
    "send_philo.py"
]

for arquivo in arquivos:
    try:
        # Executa o arquivo pelo shell
        puts(f"Executando {arquivo}...")
        subprocess.run(["python3", arquivo], check=True)
    except subprocess.CalledProcessError as e:
        puts(f"Erro ao executar {arquivo}: {e}")
    except FileNotFoundError:
        puts(f"Arquivo {arquivo} não encontrado.")

