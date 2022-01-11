# Interface Básica

1. Análise de conforto térmico (exterior)
     Para ilustrar o funcionamento do plug-in, vamos utilizar o componente **Ladybug UTCI Confort Calculator**
     ![Outdor Confort Calculator](.\UTCI.jpg)

1. Entradas
       Por padrão do Grasshopper as entradas ficam no lado esquerdo e as saídas no lado direito dos componentes. As entradas podem ser obrigatórias ou opcionais.

2. Entradas Obrigatórias
     Por convenção, todas as entradas obrigatórias dos componentes do LadyBug tem seus nomes iniciando por um caractere "_" (**underscore**). Para este componente as obrigatórias são:

    1. Temperatura de bulbo seco [*_dryBulbTemperature*](https://en.wikipedia.org/wiki/Dry-bulb_temperature)
    2. Umidade relativa do ar [*_relativeHumidity*](https://en.wikipedia.org/wiki/Relative_humidity)
    3. ***_run***

3. As entradas com (**underscore**) no início e no fim do nome, são opcionais, tendo valores padrões que são usados quando nenhuma informação é inserida.
   1. Temperatura radiante média [*_mrt_*](https://en.wikipedia.org/wiki/Mean_radiant_temperature)
   2. *_wind_vel_*

[arquivo exemplo](./inferface_básica_final_1_3_0.gh)