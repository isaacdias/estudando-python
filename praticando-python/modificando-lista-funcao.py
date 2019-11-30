
# coding: UTF-8

#
# Função que simula a impressão de um design 
#

def print_models(unprinted_designs, completed_models):
    """Simula a impressão de cada design, até que não haja mais nenhum.
    transfere cada design para completed_models após a impressão"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

#
# Função que exibe quais modelos estão prontos
#

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'phone charger', ]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
