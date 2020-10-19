# Otimização Estocástica.



## Método Hill Clibing

### funcionamento do método

![ilustra](./ha_ilustra_00.png)

### Objetivo almejado

![ilustra](./hc_ilustra_01.jpg)

### Limitações do método

![ilustra](./hc_ilustra_02.jpg)

_______________________________________


## Mínimos e máximos locais e Globais

![máximos e mínimus](https://upload.wikimedia.org/wikipedia/commons/6/68/Extrema_example_original.svg)

###### fonte: https://upload.wikimedia.org/wikipedia/commons/6/68/Extrema_example_original.svg

## Problemas multivariáveis

![multi var](https://upload.wikimedia.org/wikipedia/commons/5/5c/ConstrTestFunc02.png)

[fonte](https://en.wikipedia.org/wiki/Test_functions_for_optimization#Test_functions_for_constrained_optimization)


## [Algoritmos Evolucionários](https://en.wikipedia.org/wiki/Evolutionary_algorithm)


### Algoritmos Genéticos

1. #### Função de aptidão (Fitness function)
1. #### Genes
1. #### População (population)
1. #### Geração (generation)
1. #### Reprodução (inbreading)
1. #### Mutação (mutation)

#### Galapagos Solver



[arquivo 3dm](./OTIMIZAÇÃO_EXEMPLO.3dm)

[arquivo gh](./galapagos_lb.gh)



O componente Galapagos fica na aba **Params**, seção **uitl**. 

![galapagos_01](./galapagos_01.jpg)

A maneira mais prática de indicar os parâmetros de otimização para o algoritmo é:
primeiro selecione todos os **sliders** que pretende otimizar.

![galapagos_01](./galapagos_02.jpg)

Em seguida, clique com o botão direito na entrada **genome** do componente **Galapagos** e escolha a opção **Selected Sliders**

![galapagos_01](./galapagos_03.jpg)

Para indicar o valor a ser usado como função de aptidão, é preciso arrastar a conexão da entrada do componente Galápagos para a saída que apresenta o valor a ser otimizado.

![galapagos_01](./galapagos_04.jpg)

#### Rodando a simulação.

![galapagos](./galapagos_05.jpg)


![galapagos](./galapagos_06.jpg)


![galapagos](./galapagos_07.jpg)


![galapagos](./galapagos_08.jpg)


![galapagos](./galapagos_09.jpg)


![galapagos](./galapagos_10.jpg)


![galapagos](./galapagos_11.jpg)


![galapagos](./galapagos_12.jpg)  


[registro da otimização](./RECORD.TXT)













