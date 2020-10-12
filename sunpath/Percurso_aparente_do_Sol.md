# Percurso Aparente do Sol

Partindo do [arquivo final](../epw_arq/ladybug_epw.gh) do guia [Baixando Arquivos EPW e importando dados](../epw_arq/ladybug_epw.md).

Selecione o componente **Ladybug_Sun Path**.

![lb sun path](./sunpath_comp.jpg)


Conecte a saída **location** do arquivo epw com a entrada **_location_** do componente **Ladybug_Sun Path**.

![lb sun path](./sunpath_comp_02.jpg)

O percurso aparente do sol já pode ser visto nas janelas do Rhinoceros.

![rhino sunpath](./sunpath_rhino_01.jpg)

Alguns aspectos do componente **Ladybug_Sun Path** podem ser ajustados nas entradas indicadas abaixo.

![lb sun path](./sunpath_comp_03.jpg)

Para mudar o ponto central do diagrama, insira um ponto no rhino:


![lb sun path](./sunpath_comp_04.jpg)

clique na tela ou digite as coordenadas

![lb sun path](./sunpath_comp_05.jpg)


No Grasshopper, selecione um componente **Point**

![lb sun path](./sunpath_comp_06.jpg)

Clique com o botão direito no centro do componente **Point** e selecione a opção **Set one Point**.

![lb sun path](./sunpath_comp_07.jpg)

Na tela do rhino, mude o tipo de seleção de **Coorrdinate** para **Point**

![lb sun path](./sunpath_comp_08.jpg)

Em seguida, clique no ponto desenhado. Voltando para a tela do Grasshopper, conecte o componente **Point** na entrada **_centerPt_** do componente **Ladybug_Sun Path**.

![lb sun path](./sunpath_comp_09.jpg)

As entradas **_sunpPathScale_** e **_sunScale_** recebem valores numéricos reais que controlam os tamanhos do diagrama e das marcações da posição do sol respectivamente.

A entrada **_projection_** recebe valores inteiros entre 0 e 2. O valor 0 é o padrão e gera o gráfico tridimensional.

![lb sun path](./sunpath_comp_10.jpg)

O valor 1 gera uma projeção ortogonal do diagrama sob o Plano XY.

![lb sun path](./sunpath_comp_11.jpg)

![lb sun path](./sunpath_comp_12.jpg)

![lb sun path](./sunpath_comp_13.jpg)