# Gráfico de Linhas

Partindo do [arquivo final](../epw_arq/ladybug_epw.gh) do guia [Baixando Arquivos EPW e importando dados](../epw_arq/ladybug_epw.md)

Na seção **2\| Visualize Wheather Data**, selecione o componente **ladybug_line Chart**

![line chart 1](./line_chart_01.jpg)

Conecte a saída de temperatura (dryBulbTemperature) do componente ladybug_Import epw** na entrada **_InputData** do componente **Ladybug_Line Chart**.

![line chart 2](./line_chart_02.jpg)

O resultado na interface do Grasshopper é um gráfico de temperaturas medidas hora à hora em todos os dias do ano. Do lado esquerdo vemos a escala de valores da temperatura e do lado direito uma legende de cores (no caso apénas uma cor) que não corresponde à cor da linha (desenhada na cor padrão de geometria do Grasshopper). 

![line chart rhino 1](./line_chart_rhino_01.jpg)

![line chart rhino 1](./line_chart_rhino_02.jpg)

Para ver as linhas nas cores certas, utilize o componente **Custom Preview** conforme figura abaixo:

![line chart 3](./line_chart_03.jpg)

![line chart rhino 1](./line_chart_rhino_03.jpg)

É possível colocar múltiplos dados na entrada do gráfico. Pode-se, por exemplo, conectar a saída de umidade na mesma entrada **_InputData** segurando a tecla **shift** para manter as duas entradas ao mesmo tempo.

![line chart 4](./line_chart_04.jpg)

Ou, de maneira mais clara, usar um componente **Merge** para agregar as informações.

![line chart 5](./line_chart_05.jpg)

Por ambos os caminhos, teremos gráficos semelhantes, com a escala do primeiro conjunto de dados do lado esquerdo e do segundo conjunto de dados do lado direito, junto com a escala gráfica.

![line chart rhino 4a](./line_chart_rhino_04a.jpg)

![line chart rhino 4b](./line_chart_rhino_04b.jpg)

Com mais de dois conjuntos de dados, já não é possível visualizar as escalas de todos os dados. Adicionando a velocidade do vento às entradas do componente, temos:

![line chart 6](./line_chart_06.jpg)

![line chart rhino 5a](./line_chart_rhino_05a.jpg)

![line chart rhino 5a](./line_chart_rhino_05b.jpg)

Considerando apenas duas entradas, algumas personalizações foram feitas no gráfico utilizando:

O componente **Ladybug_Deconstruct Location** que separa as informações da saída Location do arquivo epw.

![line chart 7](./line_chart_07.jpg)

Um componente **Concatenate** que junta informações de texto.

![line chart 8](./line_chart_08.jpg)


Um componente **ladybug_Legend Parameters** que permite alterações nas propriedades as legendas de um gráfico.

![line chart 8b](./line_chart_08b.jpg)

Alguns painéis e alguns componentes **Color Swatch**

![line chart 9](./line_chart_09.jpg)

Clicando duas vezes na parte de um componente **Color Swatch** que exibe uma cor:

![line chart 10a](./line_chart_10a.jpg)

É possível selecionar uma nova cor, ajustando os controles e clicando na opção accept

![line chart 10](./line_chart_10.jpg)

[Arquivo final](./gra_temp_um_line.gh)

![grass final](./line_chart_temp_umi_exemplo.png)

![rhino 01](./line_chart_rhino_exemplo_01.jpg)

![rhino 02](./line_chart_rhino_exemplo_02.jpg)