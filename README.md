# Ferramentas de Simulação em Modelos Paramétricos

_______

## MBI BIM | SENAI-CIMATEC | 2022

### Prof. Fernando Ferraz Ribeiro | ffribeiro@gmail.com

_______

### [Edital de Avaliação](./edital/edital_01.md)

_______
_______

## Parte I - Introdução


### [Simulação e Bim - Conceitos](./Conceitos/conceitos.md)

1. Conceito de BIM
1. Conceito de Simulação Computacional
1. Conceito de Otimização

### [Projeto e Simulação](./Conceitos/proj_simula.md)

1. Relações entre projeto e simulação
1. Algumas ferramentas de simulação para a construção civil 



### [Matemática das simulações](./Conceitos/math_sim.md)

1. Matemática das simulações.

### Instalação: Ladybug + Honebee

[Guia de instalação](./instala_130/instala.md)


### Interface básica Ladybug tools

[guia de interface](./interface_basica/interface_basica.md)

1. Ambiente de trabalho

    1. Análise de conforto térmico (exterior)
    1. Temperatura de bulbo seco
    1. Sensação Térmica (Universal Thermal Climate Index)
    1. PMV e Adaptive Comfort
    1. *_run*

1. Introdução à Geração de Gráficos no Ladybugs Tools
   
   1. [Psychometric Chart](./psychometric/psychart.md)
   

   
   
### Salvando Imagens das telas do Rhinoceros e do Grasshopper

[guia de geração de imagens raster](./print_view/print_de_viewport.md)
1. Salvando Imagens da viewport do Rhinoceros
1. Salvando algoritmos do Grasshopper

## Parte II - Análises Climaticas

_______
_______

### Trabalhado com arquivos EPW


1. [Baixando Arquivos EPW e Importando os Dados](./epw_arq/ladybug_epw.md)

1. [Avaliação inicial dos dados do arquivo](./epw_arq/epw_avaliando.md)


### Gráficos de Temperatura e Ventos

1. [Gráficos mensais](./m_chart/month_chart.md)

2. [Mapa de calor](./hourly/hourly_chart.md)

3. [Rosa dos ventos](./wind_rose/Rosa_dos_ventos.md)

![Imagem](.\imagens\LadyBug_01.png)

Arquivos EPW utilizados na aula:

[cidade01](./epw_arq_exemplos/BRA_BA_Salvador.866780_INMET.zip)

[cidade02](epw_arq_exemplos/BRA_SC_Chapeco.838830_TMYx.zip)

### Análise de Insolejamento - parte 1

1. [Percurso aparente do Sol](./sunpath/Percurso_aparente_do_Sol.md)

    * [Movimento anual do sol](http://www.if.ufrgs.br/fis02001/aulas/aula_movsol.htm)

1. [Análise de horas de insolejamento](./sunpath/Analise_horas_de_sol.md)

    ![Imagem](.\imagens\LadyBug_02.png)

### Análise de Insolejamento - parte 2

1. [Arquivo base para análise de radiação solar](./radiation/radiation.md)

1. [Sky Dome](./radiation/skydome.md)

1. [Radiation Rose](./radiation/radiationrose.md)

1. [Radiação nas Superfícies](./radiation/rad_surf.md)

    ![Imagem](.\imagens\LadyBug_03.png)

#### Fontes de informação

[docs](https://docs.ladybug.tools/ladybug-primer/#installation)

[Tutoriais Chris Mackey](https://www.youtube.com/playlist?list=PLruLh1AdY-Sho45_D4BV1HKcIz7oVmZ8v)

[EPWMAP](https://www.ladybug.tools/epwmap/)

[Hydra](https://hydrashare.github.io/hydra/)

_______
_______

## Parte III - Otimização

 1. [Otimização estocástica](./galapagos_lb/otimiza.md)

### Bim e ciência de dados


1. IOT Internet of Things

1. IOT e BIM

1. Ciência de Dados

1. Ciência de dados e ambiente construído

    1. IOT
    1. Big Data
    1. Modelagem da Informação da Cidade - City Information Modeling
    1. Vizualização de Dados
    1. Exemplos de aplicação

1. Encerramento do curso
