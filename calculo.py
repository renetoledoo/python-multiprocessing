import math
import datetime
from concurrent.futures.process import ProcessPoolExecutor as Executor
import multiprocessing

def main():
    inicio = datetime.datetime.now()
    qtd_cores = multiprocessing.cpu_count()
    total = 50_000_000
    with Executor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            ini =  total * (n - 1) / qtd_cores
            fim = total * n / qtd_cores
            executor.submit(computar, inicio = ini, fim = fim)
            


    tempo = datetime.datetime.now() - inicio
    print(f"Terminou em {tempo.total_seconds():.2f} segundos")



def computar(fim, inicio = 1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

    
if __name__ == "__main__":
    main()
