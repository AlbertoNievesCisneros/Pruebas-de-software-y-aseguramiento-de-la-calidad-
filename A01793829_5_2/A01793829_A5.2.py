#!/usr/bin/env python
# coding: utf-8

# In[18]:


import json
import sys
import time


def load_json_file(filename):
    """
    cargar el archivo JSON  y manejar excepciones.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:
                raise ValueError("El archivo no contiene una lista de diccionarios")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: el archivo '{filename}' no es un JSON válido.")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []


def calculate_total_cost(price_catalogue, sales_record):
    """
    Calcular el costo toal de als ventas.
    """
    total_cost = 0
    for sale in sales_record:
        try:
            product = sale.get('Product')
            quantity = sale.get('Quantity')
            if product is None or quantity is None:
                raise KeyError
            for item in price_catalogue:
                if item['title'] == product:
                    total_cost += item['price'] * quantity
                    break
            else:
                print(f"Warning: el producto '{product}' no se encontró en el catálogo de precio.")
        except KeyError:
            print("Error: Formato de datos inválido en los registros de ventas.")
    return total_cost


# In[19]:



def main():
    """
    Main.
    """
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        return

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    # Cargar los archivos JSON 
    price_catalogue = load_json_file(price_catalogue_file)
    sales_record = load_json_file(sales_record_file)

    # Calcular el costo total "calculate_total_cost"
    total_cost = calculate_total_cost(price_catalogue, sales_record)

    # imprimir el costo total 
    print(f"Total cost of all sales: ${total_cost:.2f}")

    # escribir los resultados a un archivo
    with open("SalesResults.txt", 'w') as results_file:
        results_file.write(f"Total cost of all sales: ${total_cost:.2f}\n")
        elapsed_time = time.time() - start_time
        results_file.write(f"Elapsed time: {elapsed_time:.2f} seconds\n")

    # imprimir el tiempo transcurrido
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()


# In[21]:


TC1ProductList = load_json_file("TC1.ProductList.json")


# In[22]:


TC1ProductList


# In[23]:


TC1Sales = load_json_file("TC1.Sales.json")


# In[24]:


calculate_total_cost(TC1ProductList, TC1Sales)


# In[25]:


calculate_total_cost(TC1ProductList, TC1Sales)


# In[26]:


TC2Sales = load_json_file("TC2.Sales.json")


# In[27]:


TC2Sales


# In[28]:


calculate_total_cost(TC1ProductList, TC2Sales)


# In[29]:


TC3Sales = load_json_file("TC3.Sales.json")


# In[30]:


TC3Sales


# In[31]:


calculate_total_cost(TC1ProductList, TC3Sales)


# In[ ]:




