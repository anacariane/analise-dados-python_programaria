import sys

preco_cenoura = 4.5
preco_oleo = 10
preco_fermento = 8
preco_leite = 5
preco_acucar = 6
preco_ovos = 15

def soma_ingredientes(tem_cenoura, tem_acucar, tem_ovos, tem_oleo, tem_fermento, tem_leite):
    total_compra = 0
    if tem_cenoura:
        total_compra = total_compra + preco_cenoura

    if tem_acucar:
        total_compra = total_compra + preco_acucar

    if tem_fermento:
        total_compra = total_compra + preco_fermento

    if tem_leite:
        total_compra = total_compra + preco_leite

    if tem_oleo:
        total_compra = total_compra + preco_oleo

    if tem_ovos:
        total_compra = total_compra + preco_ovos

    return total_compra

total = soma_ingredientes(True, True, True, True, True, True)

print(total)


terminal_tem_cenoura = True
terminal_tem_acucar = True
terminal_tem_fermento = True
terminal_tem_leite = True
terminal_tem_oleo = True
terminal_tem_ovos = True

total = soma_ingredientes(terminal_tem_cenoura, terminal_tem_acucar, terminal_tem_fermento, terminal_tem_leite, terminal_tem_oleo, terminal_tem_ovos)

print("Total dos Ingredientes: ", total)