# Índice do Material

## Capítulos editoriais

- [Fundação](./chapters/fundacao.md)
- [Convênios](./chapters/convenio.md)
- [Formulário](./chapters/formulario.md)
- [Valores](./chapters/valores.md)
- [Material para participantes](./material-para-participantes.md)
- [Material para participantes em HTML](./material-para-participantes.html)
- [Material para participantes em PDF](./material-para-participantes.pdf)

## Apresentação

- [Roteiro do deck](../presentation/apresentacao-onboard-asof.md)
- [Arquivo `.pptx`](../presentation/onboard-asof.pptx)
- [Arquivo `.html`](../presentation/onboard-asof.html)
- [Arquivo `.pdf`](../presentation/onboard-asof-web.pdf)
- [CSS da apresentação](../presentation/onboard-asof.css)
- [JS da apresentação](../presentation/onboard-asof.js)

## Geração e manutenção

- [README](../README.md)
- [Script de geração do `.pptx`](../scripts/generate_presentation.py)
- [Script de geração do PDF via HTML](../scripts/render_presentation_pdf.py)

## Uso sugerido

1. Ler os capítulos editoriais para revisar o conteúdo-base.
2. Ajustar o roteiro em `presentation/apresentacao-onboard-asof.md`, se necessário.
3. Regenerar o `.pptx` com `uv run --with python-pptx scripts/generate_presentation.py`.
4. Regenerar o PDF via HTML com `uv run --with playwright python scripts/render_presentation_pdf.py`.
