# Otimização Estocástica.
________________________________________________

## Entendendo o problema


[exemplo teórico 3dm](./galapagos_exemplo_teorico.3dm)

[exemplo teórico gh](./galapagos_exemplo_teorico.gh)

_________________________________________
### Método HILL CLIMBING

#### Funcionamento do método
![ilustra](./ha_ilustra_00.png)

#### Objetivo almejado

![ilustra](./hc_ilustra_01.jpg)

#### Limitações do método

![ilustra](./hc_ilustra_02.jpg)

_______________________________________


### Mínimos e máximos locais e Globais

![máximos e mínimus](https://upload.wikimedia.org/wikipedia/commons/6/68/Extrema_example_original.svg)

###### fonte: https://upload.wikimedia.org/wikipedia/commons/6/68/Extrema_example_original.svg

### Problemas multivariáveis

![multi var](https://upload.wikimedia.org/wikipedia/commons/5/5c/ConstrTestFunc02.png)

[fonte](https://en.wikipedia.org/wiki/Test_functions_for_optimization#Test_functions_for_constrained_optimization)

_________________________________________________________

## [Algoritmos Evolucionários](https://en.wikipedia.org/wiki/Evolutionary_algorithm)


### Algoritmos Genéticos

1. #### Função de aptidão (Fitness function)
1. #### Genes
1. #### População (population)
1. #### Geração (generation)
1. #### Reprodução (inbreading)
1. #### Mutação (mutation)

#### Galapagos Solver

[arquivo 3dm](./OTIMIZA_EXEMPLO.3dm)

[arquivo gh](./galapagosLadyBug.gh)

O componente Galapagos fica na aba **Params**, seção **uitl**. 

![galapagos_01](./galapagos_01.jpg)

A maneira mais prática de indicar os parâmetros de otimização para o algoritmo é:
primeiro selecione todos os **sliders** que pretende otimizar.

![galapagos_01](./galapagos_02.jpg)

Em seguida, clique com o botão direito na entrada **genome** do componente **Galapagos** e escolha a opção **Selected Sliders**

![galapagos_01](./galapagos_03.jpg)

Para indicar o valor a ser usado como função de aptidão, é preciso arrastar a conexão da entrada do componente Galápagos para a saída que apresenta o valor a ser otimizado.

![galapagos_01](./galapagos_04.jpg)

Clique duas vezes no ícone do componente **Galapagos** para abrir o editor do *solver*.

#### Rodando a simulação.

O *Galapagos Editor* possui 3 abas: Options (para configurar a análise), Solver (para rodar a simulação) e Record (onde é gravado um registro do passo a passo de uma simulação).

Em options podemos configurar:
 1. se o algoritmo vai procurar por um máximo ou mínimo local.
 2. quantas gerações podem ser geradas sem evolução na função de aptidão.
 3. O tamanho da população
 4. quantas vezes a população inicial será aumentada na primeira geração
 5. O percentual de indivíduos a serem mantidos conforme critério da função de aptidão.
 6. Percentual de indivíduos a serem gerados a partir da combinação dos genes de indivíduos mantidos na geração anterior.

![galapagos](./galapagos_05.jpg)

1. Utilizar o solver genético
2. iniciar a otimização
3. diagrama das gerações
4. representação da população
5. representação do genoma
6. representação dos indivíduos de uma geração

![galapagos](./galapagos_06.jpg)

É possível selecionar uma gerção (1) e um indivíduo (2) de uma geração e ajustar os slidres para a posiçãod este individuo (3).

![galapagos](./galapagos_07.jpg)

O pequeno sinal de + no diagrama das gerações indica que um novo valor para máximo global foi encontrado.

Podemos ver o valor de máximo encontrado na geração 8 na imágem abaixo

![galapagos](./galapagos_08.jpg)

Na geração 10, outro valor de máximo foi encontrado.

![galapagos](./galapagos_09.jpg)

Na geração 22 um novo candidato a máximo global foi encontrado.

![galapagos](./galapagos_10.jpg)

na geração 23 um novo valor é encontrado.

![galapagos](./galapagos_11.jpg)

Após 40 gerações sem alternar o valor maior que o encontrado na geração 23, o solver atinge sua condição de parada.

![galapagos](./galapagos_12.jpg)  

Abaixo temos um arquivo com a cópia dos valores gravados durante a otimização.

[registro da otimização](./RECORD.TXT)