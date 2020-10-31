import sys, os
import functools
from time import time
from brute_force import brute_force
from algos import factorize_v1, factorize_v2

def test_decompistion(n, primes):
    mult = functools.reduce(lambda a,b : a*b,primes)
    return n == mult

def factorize(numbers):
    """
        A Faire:
        - Ecrire une fonction qui prend en paramètre une liste de nombres et qui retourne leurs decompositions en facteurs premiers
        - cette fonction doit retourner un dictionnaire Python où :
            -- la clé est un nombre n parmi la liste de nombres en entrée
            -- la valeur est la liste des facteurs premiers de n (clé). Leur produit correpond à n (clé).  
            
        - Attention :
            -- 1 n'est pas un nombre premier
            -- un facteur premier doit être répété autant de fois que nécessaire. Chaque nombre est égale au produit de ses facteurs premiers. 
            -- une solution partielle est rejetée lors de la soumission. Tous les nombres en entrée doivent être traités. 
            -- Ne changez pas le nom de cette fonction, vous pouvez ajouter d'autres fonctions appelées depuis celle-ci.
            -- Ne laissez pas trainer du code hors fonctions car ce module sera importé et du coup un tel code sera exécuté et cela vous pénalisera en temps.
    """
    # return {n: brute_force(n) for n in numbers} # ceci n'est pas une bonne réponse

    start = time()
    rep = {}
    for n in numbers:
        start_n = time()
        primes = factorize_v2(n, ini_facto=True)
        if test_decompistion(n, primes):
            # print(f"Correct decomposition for {n}")
            rep[n] = primes
        else:
            print(f"Wrong decomposition for {n} with {primes}")
        # print(f"Took {time() - start_n}\n")

    print(f"Took {time() - start} s\n\n")
    return rep


#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__=="__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    
    # un repertoire des fichiers en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
	    print(input_dir, "doesn't exist")
	    exit()

    # un repertoire pour enregistrer les résultats doit être passé en parametre 2
    if not os.path.isdir(output_dir):
	    print(input_dir, "doesn't exist")
	    exit()       

     # Pour chacun des fichiers en entrée 
    for idx, data_filename in enumerate(sorted(os.listdir(input_dir))):
        # if idx != 6:
        #     continue
        # importer la liste des nombres
        data_file = open(os.path.join(input_dir, data_filename), "r")
        numbers = [int(line) for line in data_file.readlines()]        
        
        # decomposition en facteurs premiers
        D = factorize(numbers)

        # fichier des reponses depose dans le output_dir
        output_filename = 'answer_{}'.format(data_filename)             
        output_file = open(os.path.join(output_dir, output_filename), 'w')
        
        # ecriture des resultats
        for (n, primes) in D.items():
            output_file.write('{} {}\n'.format(n, primes))
        
        output_file.close()

    
