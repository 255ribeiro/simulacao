# Guia de instalação dos programas

## Instalação do **Rhinoceros**

1. Instalar o **Rhinoceros** ( versão 6 ou 7 )
   - link: [https://www.rhino3d.com/download/](https://www.rhino3d.com/download/)

1. Caso o **Rhinoceros** seja instalado em português, mudar o idioma para inglês.
   - Instruções: [https://wiki.mcneel.com/rhino/6/addlanguages](https://wiki.mcneel.com/rhino/6/addlanguages)

## Instalação do Ladybug Tools

2. Baixar o **Ladybugtools**.
   - Link : [https://www.food4rhino.com/en/app/ladybug-tools#downloads_list](https://www.food4rhino.com/en/app/ladybug-tools#downloads_list)
3. Seguir as instruções de instalação.
   - link: [https://github.com/ladybug-tools/lbt-grasshopper/wiki](https://github.com/ladybug-tools/lbt-grasshopper/wiki)

4. Executar os passos opcionais de instalação do **Radiance** e do **Openstudio**:
   - [https://github.com/ladybug-tools/lbt-grasshopper/wiki/1.1-Windows-Installation-Steps#optional-steps](https://github.com/ladybug-tools/lbt-grasshopper/wiki/1.1-Windows-Installation-Steps#optional-steps)

## Testando a instalação:

Para testar a instalação, na aba **HoneyBee** na paleta **1::Visualize**, utilize os componentes **HB Check Version** e **HB Config**.

- [Arquivo Teste](./install_check.gh)

![Install_check](../imagens/Install_check.jpg)


- Pasta da instalação do Ladybug tools: 
        ``` %userprofile%\ladybug_tools ```
- Pasta da instalação dos **Plugins** do **Grasshopper**: 
        ``` %APPDATA%\Grasshopper ```
- Pasta de download dos dados climáticos:
        ``` C:\ladybug ```
