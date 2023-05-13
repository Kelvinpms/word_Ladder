# Importa a biblioteca string, que fornece uma coleção de constantes para lidar com strings em Python.
import string
# Definimos uma função read_file que recebe um nome de arquivo e retorna um conjunto com todas as palavras contidas nele. O with garante que o arquivo seja fechado após a leitura. word.strip().lower() remove espaços em branco e converte a palavra em minúsculas.
def read_file(filename):
    with open(filename, "r") as file:
        return set(word.strip().lower() for word in file)
# Definimos uma função generate_graph que recebe um conjunto de palavras e retorna um dicionário que representa um grafo. Inicializamos o grafo como um dicionário vazio e criamos uma string alphabet que contém todas as letras minúsculas do alfabeto.
def generate_graph(words):
    graph = {}
    alphabet = string.ascii_lowercase

    for word in words:
        graph[word] = []
        # Para cada letra na palavra, geramos uma nova palavra com uma letra trocada
        for i in range(len(word)):
            for letter in alphabet:
                neighbor = word[:i] + letter + word[i+1:]
                if neighbor in words and neighbor != word:
                    graph[word].append(neighbor)
    return graph
# Para cada palavra no conjunto words, inicializamos uma lista vazia no grafo correspondente. Para cada letra na palavra, geramos uma nova palavra com uma letra trocada por uma das letras do alfabeto. Se essa nova palavra existir no conjunto words e for diferente da palavra original, adicionamos ela na lista correspondente no grafo. Por fim, retornamos o grafo completo.
def bfs(graph, start_word, end_word):
    visited = {start_word}
    queue = [(start_word, [start_word])]
# Definimos uma função bfs que recebe um grafo, uma palavra inicial e uma palavra final. Inicializamos um conjunto visited com a palavra inicial e uma fila queue com a palavra inicial e uma lista que contém apenas a palavra inicial.
    while queue:
        word, path = queue.pop(0)
        for neighbor in graph[word]:
            if neighbor == end_word:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []
# Enquanto a fila não estiver vazia, removemos o primeiro elemento da fila e o atribuímos a word e path. Em seguida, percorremos a lista de vizinhos (palavras que diferem em apenas uma letra) da palavra word. Se o vizinho for a palavra final, retornamos o caminho até ele. Se o vizinho ainda não foi visitado, adicionamos ele ao conjunto de visitados e o colocamos na fila com o caminho até ele. Se não houver caminho, retornamos uma lista vazia.
if __name__ == '__main__':
    filename = input("Digite o nome do arquivo de dicionário: ")
    start_word = input("Digite a palavra de início: ").lower()
    end_word = input("Digite a palavra de fim: ").lower()

    words = read_file(filename)
    graph = generate_graph(words)

    ladder = bfs(graph, start_word, end_word)

    if ladder:
        print(f"Caminho: {' -> '.join(ladder)}")
    else:
        print("Não é possível conectar as duas palavras.")
