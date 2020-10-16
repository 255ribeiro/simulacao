# Análise de radiação solar nas fachadas

Partindo do [arquivo final](./radiation_01.gh) do guia [Arquivo base para análise de radiação solar](./radiation.md). Utilizando o arquivo do [RADIATION_EXEMPLO.3dm](./RADIATION_EXEMPLO.3dm).


Selecione um componente **Ladybug_Radiation Analisys** e conecte a saída **select_SkyMtx** do componente Ladybug de mesmo nome na respectiva entrada. 

![img rad surf](.\rad_04_01.jpg)

As configurações de **north\_**, **\_geometry**, **context\_**, **\_gridSize\_** e **_disFromBase** seguem a mesma lógica das respectivas confgurações realizadas no guia [Análise de horas de insolejamento](../sunpath/Analise_horas_de_sol.md). 

![img rad surf](.\rad_04_01_a.jpg)

conectando um **Boolean Toogle** à entrada **_runIt** é possível rodar a simulação.

![img rad surf](.\rad_04_02.jpg)

O resultado da análise aparece nas **Viewports** do Rhinoceros. É possível observar as fachadas por ângulos diferentes e avaliar os níveis de radiação pelo [diagrama de falsa cor](https://en.wikipedia.org/wiki/False_color).

![img rad surf](.\rad_04_03.jpg)

Através do componente **Ladybug_Orientation Study Parameters** é possível calcular a radiação nas fachadas simulando rotações da edificação em diversos ângulos.

![img rad surf](.\rad_04_04.jpg)

Coloque o **Boolean Toggle** da entrada **_runIt** do componente **Ladybug_Radiation Analisys** no estado False. Sem desconectar da entrada, conecte-o também na entrada **_runStudy** do componente **Ladybug_Orientation Study Parameters**.

O parâmetro **_divisionAngle** recebe um valor maior que zero e menor que 180, indica de quanto em quantos ângulos o prédio deve girar de uma análise para outra.

O Parâmetro **_totalAngle** representa o ângulo máximo (final) das rotações.

Clique duas vezes na tela do Grasshopper e digite 0,0,0. Este atalho gera um ponto locado nas coordenadas digitadas.

![img rad surf](.\rad_04_05.jpg)

Conecte o componetente **Point** na entrada **basePoint_**. Rode o estudo mudando o estado do componente **Boolean Toggle** no estado True.

Com essas configurações, a saída **totalRadiation** mostrara 19 valores de radiação, um para cada posição de rotação do edifício.

![img rad surf](.\rad_04_06.jpg)

Ordene a saída das radiações com um componente **Sort List**. O primeiro valor desta lista representa o menor valor da radiação nas fachadas dentre todos os ângulos estudados. 

![img rad surf](.\rad_04_07.jpg)

É preciso criar uma série de valores, representando os ângulos de o a 360, de 20 em 20 graus. 

![img rad surf](.\rad_04_08.jpg)

Configurando os componentes da série como indicado na figura baixo, a sequência será automaticamente ajustada para qualquer submúltiplo de 360.

![img rad surf](.\rad_04_09.jpg)

colocando a série na entrada **values** do componente **Sort List**, o primeiro valor da saída **values** será o ângulo de rotação no qual o menor valor para a radiação foi medido

![img rad surf](.\rad_04_10.jpg)

Para visualizar a posição do edifício nesta configuração, utilize um componente **Rotate 3D**.

![img rad surf](.\rad_04_11.jpg)

Use um componente **List Item** para selecionar o primeiro valor da lista de ângulos e passar o valor para o componente *Rotate 3D**.

![img rad surf](.\rad_04_12.jpg)

__________________________________________________________

![img rad surf](.\rad_04_13.jpg)

![img rad surf](.\rad_04_14.jpg)
__________________________________________________________
__________________________________________________________

[Arquivo Final](radiation_04.gh)
![img rad_surf](./radiation_04_final.png)