# Plano de Execução: Melhorias na apresentação HTML da ASOF

## Objetivo

Resolver os principais problemas de experiência e direção visual identificados na auditoria heurística do deck HTML:

- reduzir aparência genérica/AI slop;
- diminuir repetição de cards e grids;
- separar melhor narrativa principal e apêndice;
- tornar a navegação menos intrusiva;
- reforçar hierarquia tipográfica e ritmo visual.

## Tarefas

### T1: Redesenhar o chrome da interface

**Arquivos canônicos**

- `presentation/onboard-asof.html`
- `presentation/onboard-asof.css`
- `presentation/onboard-asof.js`

**Descrição**

Reduzir a dominância da toolbar fixa, tornar os controles menos ruidosos e mais compatíveis com uma apresentação institucional.

**Critérios de aceite**

- toolbar deixa de competir com a capa;
- controles continuam descobríveis;
- modo impressão continua limpo.

**Status**

- [ ] Pendente

### T2: Variar a linguagem visual dos slides principais

**Arquivos canônicos**

- `presentation/onboard-asof.html`
- `presentation/onboard-asof.css`

**Descrição**

Quebrar a repetição excessiva de “headline + cards + grid”, dando mais contraste entre tipos de slide da narrativa principal.

**Critérios de aceite**

- pelo menos 4 slides principais usam composições claramente distintas;
- redução perceptível do uso de cards como solução universal;
- melhora da hierarquia tipográfica.

**Status**

- [ ] Pendente

### T3: Reestruturar visualmente o apêndice

**Arquivos canônicos**

- `presentation/onboard-asof.html`
- `presentation/onboard-asof.css`

**Descrição**

Separar o apêndice da narrativa principal e tratá-lo como material de referência, não como continuação estética do deck.

**Critérios de aceite**

- apêndice parece um anexo deliberado;
- listas ficam mais escaneáveis;
- menor densidade visual por slide.

**Status**

- [ ] Pendente

### T4: Validar render web e PDF

**Arquivos canônicos**

- `presentation/onboard-asof.html`
- `presentation/onboard-asof.css`
- `presentation/onboard-asof.js`
- `presentation/onboard-asof-web.pdf`
- `scripts/render_presentation_pdf.py`

**Descrição**

Regenerar o PDF, revisar renderização web e impressão, e corrigir regressões.

**Critérios de aceite**

- HTML abre corretamente;
- PDF é gerado sem chrome indevido;
- conteúdo principal e apêndice permanecem íntegros.

**Status**

- [ ] Pendente
