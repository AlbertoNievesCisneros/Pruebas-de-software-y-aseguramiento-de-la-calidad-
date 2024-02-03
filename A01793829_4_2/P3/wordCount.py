#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from collections import Counter

def count_words(filepath):
    try:
        with open(filepath, 'r') as file:
            words = file.read().lower().split()
            word_count = Counter(words)
            total_count = sum(word_count.values())  # Total de palabras
            with open('WordCountResults.txt', 'w') as result_file:
                for word, count in word_count.items():
                    result_file.write(f"{word}: {count}\n")
                    print(f"{word}: {count}")
                # Escribe e imprime el total después de listar todas las palabras
                result_file.write(f"Total: {total_count}\n")
                print(f"Total: {total_count}")
    except FileNotFoundError:
        print(f"El archivo {filepath} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count_words(sys.argv[1])
    else:
        print("Por favor, proporciona el path del archivo como argumento.")

