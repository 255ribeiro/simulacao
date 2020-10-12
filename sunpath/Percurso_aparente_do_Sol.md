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

Em seguida, clique no ponto desenhado.

