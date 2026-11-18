# Atlas VTT em PT-BR

Tradução para português do Brasil do plugin **Atlas VTT** (Obsidian), versão 0.12.1: 3.989 textos da interface.

Este repositório **não contém o plugin**. O Atlas VTT é de Fabian Urbanek (ByteMirror) e pertence a ele. Aqui estão só a tradução e um script que a aplica à cópia que você já instalou.

## Como usar

1. Instale o Atlas VTT 0.12.1 pelo Obsidian.
2. Rode, apontando para a pasta do plugin (a que tem o `main.js`):

```
python aplicar.py "<cofre>\.obsidian\plugins\atlas-vtt"
```

3. Reinicie o Obsidian.

O script guarda o original em `main.js.original` e confere se a versão do plugin tem o formato esperado antes de alterar. Para voltar ao inglês: `python aplicar.py "<pasta>" --desfazer`.

## Atualizações do plugin

Atualizar o plugin desfaz a tradução. Basta rodar o script de novo. Se uma versão nova mudar a estrutura interna, o script avisa e não altera nada; nesse caso a tradução precisa ser adaptada, e textos novos aparecem em inglês.

## Licença

O script e a tradução estão sob a licença MIT (ver `LICENSE`). Isso não se estende ao Atlas VTT, que segue a licença do autor original.
