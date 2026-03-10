# ONBOARD ASOF

Material-base para apresentar a ASOF a associados atuais e potenciais associados, combinando texto editorial e uma apresentação institucional reutilizável.

## Quick Start

### Ler os capítulos-base

- [fundacao.md](docs/chapters/fundacao.md)
- [convenio.md](docs/chapters/convenio.md)
- [formulario.md](docs/chapters/formulario.md)
- [valores.md](docs/chapters/valores.md)

### Abrir a apresentação pronta

- [onboard-asof.pptx](presentation/onboard-asof.pptx)
- [onboard-asof-web.pdf](presentation/onboard-asof-web.pdf)

### Regenerar as saídas

#### Saída `.pptx`

```bash
uv venv .venv
uv run --with python-pptx scripts/generate_presentation.py
```

#### Saída web + PDF

```bash
uv run --with playwright python scripts/render_presentation_pdf.py
```

Arquivos gerados:

- HTML: [presentation/onboard-asof.html](presentation/onboard-asof.html)
- CSS: [presentation/onboard-asof.css](presentation/onboard-asof.css)
- JS: [presentation/onboard-asof.js](presentation/onboard-asof.js)
- PDF: [presentation/onboard-asof-web.pdf](presentation/onboard-asof-web.pdf)

## Objetivo

Este repositório consolida textos de apoio para um manual de apresentação da ASOF, voltado a associados atuais e potenciais associados. A proposta é transformar documentos institucionais e arquivos operacionais em capítulos claros, reaproveitáveis e fáceis de evoluir.

## Entregáveis

- capítulos editoriais em Markdown sobre fundação, convênios, formulário e contribuição;
- roteiro estruturado de apresentação em [apresentacao-onboard-asof.md](presentation/apresentacao-onboard-asof.md);
- deck institucional em [onboard-asof.pptx](presentation/onboard-asof.pptx);
- apresentação web em [onboard-asof.html](presentation/onboard-asof.html);
- PDF derivado do HTML em [onboard-asof-web.pdf](presentation/onboard-asof-web.pdf);
- scripts reprodutíveis de geração em [generate_presentation.py](scripts/generate_presentation.py) e [render_presentation_pdf.py](scripts/render_presentation_pdf.py).

## Capítulos disponíveis

- [fundacao.md](docs/chapters/fundacao.md): origem da ASOF, contexto da reunião de fundação e base estatutária inicial.
- [convenio.md](docs/chapters/convenio.md): visão geral da política de convênios, categorias atendidas e panorama do acervo existente.
- [formulario.md](docs/chapters/formulario.md): explicação do formulário de atualização de dados e instruções de preenchimento.
- [valores.md](docs/chapters/valores.md): contribuição associativa e observações práticas derivadas do formulário disponível.

## Estrutura do repositório

| Arquivo | Finalidade |
|---------|------------|
| `README.md` | Visão geral do projeto |
| `docs/chapters/` | Capítulos editoriais do onboard |
| `presentation/apresentacao-onboard-asof.md` | Estrutura narrativa do deck |
| `presentation/onboard-asof.pptx` | Saída em PowerPoint |
| `presentation/onboard-asof.html` | Versão web da apresentação |
| `presentation/onboard-asof.css` | Estilos da versão web |
| `presentation/onboard-asof.js` | Navegação da versão web |
| `presentation/onboard-asof-web.pdf` | PDF gerado a partir do HTML |
| `scripts/generate_presentation.py` | Geração automatizada do `.pptx` |
| `scripts/render_presentation_pdf.py` | Geração automatizada do PDF a partir do HTML |

## Fontes utilizadas nesta etapa

- Ata de fundação da ASOF.
- Estatuto social da ASOF.
- Formulário de atualização de dados do associado.
- Acervo em `04-Convenios`, incluindo contratos, minutas e modelo de convênio.

## Conteúdo previsto para evolução

- `conquistas`: ainda não há, neste repositório, um documento-base que liste resultados institucionais, vitórias da carreira ou entregas históricas da ASOF.
- `comodidades`: parte do conteúdo pode futuramente ser desdobrada de `convenio.md`, mas ainda falta um recorte editorial que diferencie convênios de comodidades permanentes da associação.

## Observações editoriais

- Os capítulos foram escritos apenas com base no material já localizado.
- Dados pessoais presentes em arquivos de apoio não foram reproduzidos.
- O capítulo de convênios privilegia estrutura, categorias e funcionamento do benefício, evitando presumir descontos específicos sem confirmação consolidada.
