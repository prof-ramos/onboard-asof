from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.util import Inches, Pt


SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

NAVY = RGBColor(0x1E, 0x27, 0x61)
TEAL = RGBColor(0x06, 0x5A, 0x82)
ICE = RGBColor(0xCA, 0xDC, 0xFC)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x5C, 0x66, 0x74)
LIGHT = RGBColor(0xF5, 0xF8, 0xFC)
ACCENT = RGBColor(0x00, 0xA8, 0x96)
GOLD = RGBColor(0xF9, 0xE7, 0x95)
CORAL = RGBColor(0xF9, 0x61, 0x67)
ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT_DIR / "presentation" / "onboard-asof.pptx"


def set_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text(slide, text, left, top, width, height, *, size=20, color=INK,
             bold=False, font_name="Aptos", align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    lines = text.split("\n") if text else [""]
    for idx, line in enumerate(lines):
        paragraph = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        paragraph.alignment = align
        run = paragraph.add_run()
        run.text = line
        run.font.name = font_name
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return box


def add_card(slide, left, top, width, height, fill, radius_text=None):
    shape = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = fill
    if radius_text:
        shape.adjustments[0] = radius_text
    return shape


def add_circle_stat(slide, left, top, diameter, number, label, fill):
    circle = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.OVAL, left, top, diameter, diameter
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = fill
    circle.line.color.rgb = fill
    add_text(
        slide, number, left, top + Inches(0.28), diameter, Inches(0.45),
        size=30, color=WHITE, bold=True, align=PP_ALIGN.CENTER, font_name="Aptos Display"
    )
    add_text(
        slide, label, left - Inches(0.2), top + diameter + Inches(0.12),
        diameter + Inches(0.4), Inches(0.6), size=14, color=INK,
        align=PP_ALIGN.CENTER
    )


def add_title(slide, kicker, title, *, dark=False):
    kicker_color = ICE if dark else TEAL
    title_color = WHITE if dark else NAVY
    body_color = ICE if dark else MUTED
    add_text(slide, kicker.upper(), Inches(0.8), Inches(0.45), Inches(3.4), Inches(0.3),
             size=12, color=kicker_color, bold=True)
    add_text(slide, title, Inches(0.8), Inches(0.8), Inches(8.8), Inches(1.05),
             size=28, color=title_color, bold=True, font_name="Aptos Display")
    return body_color


def add_footer(slide, idx, total, dark=False):
    color = ICE if dark else MUTED
    add_text(slide, f"{idx:02d} / {total:02d}", Inches(11.9), Inches(7.0), Inches(0.7), Inches(0.25),
             size=10, color=color, align=PP_ALIGN.RIGHT)


def add_timeline_node(slide, left, top, label, sublabel, fill):
    circ = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.OVAL, left, top, Inches(0.42), Inches(0.42))
    circ.fill.solid()
    circ.fill.fore_color.rgb = fill
    circ.line.color.rgb = fill
    add_text(slide, label, left - Inches(0.2), top + Inches(0.55), Inches(1.2), Inches(0.25),
             size=13, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, sublabel, left - Inches(0.45), top + Inches(0.85), Inches(1.7), Inches(0.5),
             size=11, color=MUTED, align=PP_ALIGN.CENTER)


def build_deck():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]
    total = 14

    # 1. Cover
    slide = prs.slides.add_slide(blank)
    set_bg(slide, NAVY)
    add_text(slide, "ONBOARD ASOF", Inches(0.8), Inches(0.7), Inches(4.5), Inches(0.5),
             size=16, color=ICE, bold=True)
    add_text(slide, "A associação criada pela carreira para representar, apoiar e conectar Oficiais de Chancelaria.",
             Inches(0.8), Inches(1.3), Inches(6.5), Inches(1.5),
             size=28, color=WHITE, bold=True, font_name="Aptos Display")
    add_text(slide, "Origem, missão, convênios, cadastro e contribuição associativa",
             Inches(0.8), Inches(3.0), Inches(5.0), Inches(0.5), size=16, color=ICE)
    add_card(slide, Inches(8.4), Inches(0.8), Inches(4.0), Inches(5.6), TEAL)
    add_text(slide, "1990", Inches(8.9), Inches(1.4), Inches(2.0), Inches(0.7),
             size=34, color=WHITE, bold=True, font_name="Aptos Display")
    add_text(slide, "Fundação deliberada\npor 24 votos a 2", Inches(8.9), Inches(2.2),
             Inches(2.4), Inches(0.8), size=18, color=WHITE, bold=True)
    add_text(slide, "26 Oficiais de Chancelaria reunidos em Brasília decidiram criar uma entidade própria e juridicamente independente.",
             Inches(8.9), Inches(3.4), Inches(2.6), Inches(1.5), size=16, color=WHITE)
    add_text(slide, "Mensagem central", Inches(8.9), Inches(5.25), Inches(2.0), Inches(0.3),
             size=11, color=GOLD, bold=True)
    add_text(slide, "A ASOF une representação institucional e apoio prático ao associado.", Inches(8.9), Inches(5.55),
             Inches(2.7), Inches(0.7), size=15, color=WHITE, bold=True)
    add_footer(slide, 1, total, dark=True)

    # 2. Origin timeline
    slide = prs.slides.add_slide(blank)
    set_bg(slide, LIGHT)
    body_color = add_title(slide, "Origem", "A ASOF nasce de uma decisão coletiva da carreira", dark=False)
    add_text(slide, "Em 7 de agosto de 1990, Oficiais de Chancelaria decidiram criar uma associação própria para representar a carreira com autonomia institucional.",
             Inches(0.8), Inches(1.75), Inches(7.0), Inches(0.8), size=18, color=body_color)
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1.2), Inches(4.0), Inches(11.6), Inches(4.0))
    line.line.color.rgb = ICE
    line.line.width = Pt(3)
    add_timeline_node(slide, Inches(1.35), Inches(3.78), "7 ago 1990", "Reunião inicial", TEAL)
    add_timeline_node(slide, Inches(4.35), Inches(3.78), "26", "participantes", ACCENT)
    add_timeline_node(slide, Inches(7.3), Inches(3.78), "24 x 2", "votação", CORAL)
    add_timeline_node(slide, Inches(10.2), Inches(3.78), "ASOF", "fundação imediata", NAVY)
    add_card(slide, Inches(8.8), Inches(1.45), Inches(3.6), Inches(1.5), WHITE)
    add_text(slide, "Brasília, ASMRE, 18h", Inches(9.1), Inches(1.75), Inches(2.8), Inches(0.25),
             size=17, color=NAVY, bold=True)
    add_text(slide, "O debate considerou manter apenas um núcleo em outra entidade, mas prevaleceu a necessidade de representação própria.",
             Inches(9.1), Inches(2.1), Inches(2.8), Inches(0.65), size=13, color=MUTED)
    add_footer(slide, 2, total)

    # 3. Autonomy choice
    slide = prs.slides.add_slide(blank)
    set_bg(slide, WHITE)
    body_color = add_title(slide, "Escolha central", "A autonomia institucional foi a opção que definiu a associação", dark=False)
    add_text(slide, "A fundação da ASOF responde a uma necessidade específica: representar os interesses da carreira com identidade própria e personalidade jurídica independente.",
             Inches(0.8), Inches(1.8), Inches(7.2), Inches(0.8), size=18, color=body_color)
    add_card(slide, Inches(0.9), Inches(3.0), Inches(5.55), Inches(2.7), LIGHT)
    add_text(slide, "Alternativa considerada", Inches(1.2), Inches(3.3), Inches(2.8), Inches(0.3),
             size=14, color=TEAL, bold=True)
    add_text(slide, "Manter apenas um núcleo de Oficiais de Chancelaria dentro de uma estrutura associativa já existente.", Inches(1.2), Inches(3.75),
             Inches(4.7), Inches(1.1), size=20, color=INK, bold=True)
    add_text(slide, "Preservaria apoio inicial, mas não resolveria a necessidade de identidade institucional própria.", Inches(1.2), Inches(5.0),
             Inches(4.7), Inches(0.45), size=13, color=MUTED)
    add_card(slide, Inches(6.85), Inches(3.0), Inches(5.55), Inches(2.7), NAVY)
    add_text(slide, "Opção aprovada", Inches(7.15), Inches(3.3), Inches(2.0), Inches(0.3),
             size=14, color=GOLD, bold=True)
    add_text(slide, "Criar uma associação exclusiva da categoria, com foco integral nos interesses dos Oficiais de Chancelaria.", Inches(7.15), Inches(3.75),
             Inches(4.75), Inches(1.15), size=20, color=WHITE, bold=True)
    add_text(slide, "A decisão consolidou autonomia, representação específica e continuidade institucional.", Inches(7.15), Inches(5.0),
             Inches(4.75), Inches(0.45), size=13, color=ICE)
    add_footer(slide, 3, total)

    # 4. Mission pillars
    slide = prs.slides.add_slide(blank)
    set_bg(slide, LIGHT)
    body_color = add_title(slide, "Missão", "O estatuto transforma a fundação em compromisso permanente", dark=False)
    add_text(slide, "O estatuto consolida a ASOF como entidade civil sem fins lucrativos voltada à união da carreira, à representação institucional e à geração de apoio prático ao associado.",
             Inches(0.8), Inches(1.75), Inches(8.0), Inches(0.75), size=18, color=body_color)
    cards = [
        (Inches(0.95), Inches(3.0), TEAL, "União da carreira"),
        (Inches(3.95), Inches(3.0), NAVY, "Representação institucional"),
        (Inches(6.95), Inches(3.0), ACCENT, "Aprimoramento profissional"),
        (Inches(9.95), Inches(3.0), CORAL, "Benefícios e convênios"),
    ]
    for left, top, color, text in cards:
        add_card(slide, left, top, Inches(2.3), Inches(2.25), color)
        add_text(slide, text, left + Inches(0.25), top + Inches(0.75), Inches(1.8), Inches(0.8),
                 size=19, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, 4, total)

    # 5. Value system
    slide = prs.slides.add_slide(blank)
    set_bg(slide, WHITE)
    body_color = add_title(slide, "Entrega de valor", "O valor da ASOF combina representação, organização e apoio ao associado", dark=False)
    add_text(slide, "A atuação associativa não se limita à defesa institucional. Ela também organiza o vínculo do associado e viabiliza benefícios concretos para a carreira e seus dependentes.",
             Inches(0.8), Inches(1.8), Inches(7.3), Inches(0.7), size=18, color=body_color)
    steps = [
        ("1", "Representar", "Leva demandas da carreira a autoridades e instituições."),
        ("2", "Organizar", "Mantém base cadastral, regras e relacionamento associativo."),
        ("3", "Conectar", "Articula convênios e benefícios em diferentes frentes."),
        ("4", "Apoiar", "Transforma a associação em suporte contínuo ao associado."),
    ]
    lefts = [Inches(0.95), Inches(3.05), Inches(5.15), Inches(7.25)]
    colors = [TEAL, NAVY, ACCENT, CORAL]
    for i, (num, title, desc) in enumerate(steps):
        add_card(slide, lefts[i], Inches(3.1), Inches(1.8), Inches(2.7), LIGHT)
        add_circle_stat(slide, lefts[i] + Inches(0.57), Inches(3.3), Inches(0.65), num, "", colors[i])
        add_text(slide, title, lefts[i] + Inches(0.18), Inches(4.15), Inches(1.45), Inches(0.3),
                 size=18, color=INK, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, desc, lefts[i] + Inches(0.15), Inches(4.55), Inches(1.5), Inches(0.9),
                 size=12, color=MUTED, align=PP_ALIGN.CENTER)
    add_footer(slide, 5, total)

    # 6. Convenios
    slide = prs.slides.add_slide(blank)
    set_bg(slide, NAVY)
    add_title(slide, "Benefícios", "Convênios ampliam o valor da associação no dia a dia", dark=True)
    add_text(slide, "O acervo disponível mostra uma rede ampla de parcerias que leva a atuação da ASOF para educação, saúde, bem-estar e serviços.", Inches(0.8), Inches(1.75),
             Inches(7.5), Inches(0.7), size=18, color=ICE)
    add_circle_stat(slide, Inches(1.0), Inches(3.0), Inches(1.15), "28", "Educação", TEAL)
    add_circle_stat(slide, Inches(3.25), Inches(3.0), Inches(1.15), "24", "Saúde", ACCENT)
    add_circle_stat(slide, Inches(5.5), Inches(3.0), Inches(1.15), "25", "Lazer e bem-estar", CORAL)
    add_circle_stat(slide, Inches(7.75), Inches(3.0), Inches(1.15), "5", "Serviços", GOLD)
    add_card(slide, Inches(10.0), Inches(2.55), Inches(2.1), Inches(2.65), WHITE)
    add_text(slide, "Mais que desconto", Inches(10.25), Inches(2.95), Inches(1.6), Inches(0.3),
             size=14, color=TEAL, bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, "Os convênios ajudam a transformar presença associativa em valor percebido no cotidiano.", Inches(10.25), Inches(3.4),
             Inches(1.6), Inches(1.1), size=18, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, 6, total, dark=True)

    # 7. Convenio flow
    slide = prs.slides.add_slide(blank)
    set_bg(slide, LIGHT)
    body_color = add_title(slide, "Funcionamento", "Os convênios operam como uma rede de acesso organizada pela ASOF", dark=False)
    add_text(slide, "A associação articula o benefício, identifica o associado e divulga as parcerias. A prestação do serviço permanece com a empresa conveniada.", Inches(0.8), Inches(1.8),
             Inches(7.9), Inches(0.65), size=18, color=body_color)
    for left, label, fill in [
        (Inches(1.0), "ASOF", TEAL),
        (Inches(4.7), "Associado\ne dependentes", NAVY),
        (Inches(8.65), "Empresa\nconveniada", ACCENT),
    ]:
        add_card(slide, left, Inches(3.15), Inches(2.7), Inches(1.75), fill)
        add_text(slide, label, left + Inches(0.25), Inches(3.65), Inches(2.2), Inches(0.6),
                 size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    for start, end in [(Inches(3.72), Inches(4.7)), (Inches(7.4), Inches(8.65))]:
        conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, start, Inches(4.0), end, Inches(4.0))
        conn.line.color.rgb = ICE
        conn.line.width = Pt(2.5)
    add_text(slide, "declaração ou carteirinha", Inches(3.2), Inches(3.5), Inches(1.6), Inches(0.3),
             size=11, color=MUTED, align=PP_ALIGN.CENTER)
    add_text(slide, "prestação do serviço", Inches(7.45), Inches(3.5), Inches(1.5), Inches(0.3),
             size=11, color=MUTED, align=PP_ALIGN.CENTER)
    add_footer(slide, 7, total)

    # 8. Form
    slide = prs.slides.add_slide(blank)
    set_bg(slide, WHITE)
    body_color = add_title(slide, "Cadastro", "O vínculo associativo depende de dados claros e atualizados", dark=False)
    add_text(slide, "O formulário de atualização de dados organiza informações pessoais, funcionais, bancárias e de contato, sustentando comunicação, atendimento e cobrança associativa.", Inches(0.8), Inches(1.8),
             Inches(8.1), Inches(0.7), size=18, color=body_color)
    steps = [("1", "Preencher"), ("2", "Assinar"), ("3", "Remeter à ASOF")]
    step_lefts = [Inches(1.05), Inches(4.25), Inches(7.45)]
    for i, (num, label) in enumerate(steps):
        add_card(slide, step_lefts[i], Inches(3.1), Inches(2.35), Inches(2.1), LIGHT)
        add_circle_stat(slide, step_lefts[i] + Inches(0.86), Inches(3.35), Inches(0.6), num, "", [TEAL, NAVY, ACCENT][i])
        add_text(slide, label, step_lefts[i] + Inches(0.22), Inches(4.32), Inches(1.9), Inches(0.35),
                 size=19, color=INK, bold=True, align=PP_ALIGN.CENTER)
    add_card(slide, Inches(10.3), Inches(2.9), Inches(2.0), Inches(2.5), TEAL)
    add_text(slide, "Dados-chave", Inches(10.55), Inches(3.2), Inches(1.5), Inches(0.25),
             size=13, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, "contatos\nsituação funcional\ndependentes\ndados bancários", Inches(10.55), Inches(3.65),
             Inches(1.5), Inches(1.2), size=15, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, 8, total)

    # 9. Contribution
    slide = prs.slides.add_slide(blank)
    set_bg(slide, LIGHT)
    body_color = add_title(slide, "Sustentação", "A contribuição associativa financia a continuidade institucional da ASOF", dark=False)
    add_text(slide, "O estatuto prevê a contribuição mensal como fonte regular de receita. O formulário atual mostra os valores praticados para desconto em folha.", Inches(0.8), Inches(1.8),
             Inches(7.7), Inches(0.65), size=18, color=body_color)
    table = [
        (Inches(1.1), TEAL, "Ativo", "R$ 40,00"),
        (Inches(4.2), NAVY, "Aposentado", "R$ 20,00"),
        (Inches(7.3), ACCENT, "Exterior", "US$ 25,00"),
    ]
    for left, fill, label, value in table:
        add_card(slide, left, Inches(3.0), Inches(2.45), Inches(2.2), fill)
        add_text(slide, label, left + Inches(0.2), Inches(3.4), Inches(2.05), Inches(0.35),
                 size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, value, left + Inches(0.2), Inches(4.0), Inches(2.05), Inches(0.5),
                 size=26, color=WHITE, bold=True, align=PP_ALIGN.CENTER, font_name="Aptos Display")
    add_text(slide, "Leitura útil para o onboard:\n\nEstatuto: define a contribuição como base regular de receita.\nFormulário: explicita os valores operacionais do documento em uso.", Inches(10.2), Inches(2.85),
             Inches(2.0), Inches(2.0), size=14, color=MUTED)
    add_footer(slide, 9, total)

    # 10. Closing
    slide = prs.slides.add_slide(blank)
    set_bg(slide, NAVY)
    add_title(slide, "Fechamento", "Associar-se é entrar em uma estrutura de representação e suporte", dark=True)
    add_text(slide, "A ASOF conecta identidade profissional, ação coletiva e benefícios concretos em uma mesma estrutura associativa.", Inches(0.8), Inches(1.8),
             Inches(7.4), Inches(0.7), size=20, color=ICE)
    pillars = [
        (Inches(0.95), TEAL, "Representar\na carreira"),
        (Inches(4.35), ACCENT, "Fortalecer\nvínculos"),
        (Inches(7.75), CORAL, "Gerar apoio\nprático"),
    ]
    for left, fill, text in pillars:
        add_card(slide, left, Inches(3.05), Inches(2.7), Inches(2.0), fill)
        add_text(slide, text, left + Inches(0.2), Inches(3.65), Inches(2.3), Inches(0.7),
                 size=21, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_card(slide, Inches(10.75), Inches(2.85), Inches(1.25), Inches(2.35), WHITE)
    add_text(slide, "Desde\n1990", Inches(10.9), Inches(3.4), Inches(0.95), Inches(0.7),
             size=25, color=NAVY, bold=True, align=PP_ALIGN.CENTER, font_name="Aptos Display")
    add_text(slide, "Criada pela carreira\npara servir à carreira", Inches(10.75), Inches(4.45),
             Inches(1.25), Inches(0.6), size=12, color=TEAL, bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, 10, total, dark=True)

    # 11. Convenios - Educacao
    slide = prs.slides.add_slide(blank)
    set_bg(slide, WHITE)
    body_color = add_title(slide, "Apêndice", "Convênios de educação", dark=False)
    add_text(slide, "Lista dos parceiros identificados no acervo consultado para a frente de educação.", Inches(0.8), Inches(1.75),
             Inches(7.0), Inches(0.5), size=17, color=body_color)
    add_card(slide, Inches(0.85), Inches(2.55), Inches(3.8), Inches(3.8), LIGHT)
    add_card(slide, Inches(4.85), Inches(2.55), Inches(3.8), Inches(3.8), LIGHT)
    add_card(slide, Inches(8.85), Inches(2.55), Inches(3.6), Inches(3.8), LIGHT)
    add_text(slide, "Aliança Francesa\nCCAA\nCIMAN\nColégio Dinatos COC\nCultura Inglesa\nCurso Ignis\nEscola Franciscana Fátima\nEscola Presbiteriana Mackenzie\nFACITEC",
             Inches(1.1), Inches(2.95), Inches(3.1), Inches(2.9), size=16, color=INK)
    add_text(slide, "FGV\nGran Cursos\nIBMEC\nIDP\nIESB\nInstituto Blaise Pascal\nLaboro\nMS Educação\nPositive Idiomas",
             Inches(5.1), Inches(2.95), Inches(3.0), Inches(2.9), size=16, color=INK)
    add_text(slide, "Rede de Ensino JK\nSt. Giles\nStudio On-line\nSwiss International School\nThomas Jefferson\nUDF\nUniCEUB\nUNIP\nWizard",
             Inches(9.1), Inches(2.95), Inches(2.9), Inches(2.9), size=16, color=INK)
    add_footer(slide, 11, total)

    # 12. Convenios - Educacao complementar + Saude
    slide = prs.slides.add_slide(blank)
    set_bg(slide, LIGHT)
    body_color = add_title(slide, "Apêndice", "Convênios de educação complementar e saúde", dark=False)
    add_text(slide, "Além da lista principal, o acervo contém parceiros complementares em educação e uma frente extensa de saúde.", Inches(0.8), Inches(1.75),
             Inches(8.0), Inches(0.5), size=17, color=body_color)
    add_card(slide, Inches(0.85), Inches(2.55), Inches(3.4), Inches(3.9), TEAL)
    add_text(slide, "Educação complementar", Inches(1.1), Inches(2.9), Inches(2.8), Inches(0.3),
             size=18, color=WHITE, bold=True)
    add_text(slide, "Centro Educacional Maria Auxiliadora\nUNYLEYA\nInstituto Formação para a Educação\n3W Educacional Editora e Cursos",
             Inches(1.1), Inches(3.35), Inches(2.7), Inches(2.2), size=16, color=WHITE)
    add_card(slide, Inches(4.55), Inches(2.55), Inches(3.8), Inches(3.9), WHITE)
    add_card(slide, Inches(8.55), Inches(2.55), Inches(3.8), Inches(3.9), WHITE)
    add_text(slide, "Aquafisio Hidroterapia Esportiva\nBonvena Medicina Reprodutiva\nCBV\nCDI Centro Diagnóstico por Imagem\nCentro de Medicina Nuclear da Guanabara\nCIORB\nClínica Plenus Psicologia e Saúde Integrada\nDermatologic\nEBM-Odonto\nEndogastrus\nHome Hospital Ortopédico e Medicina Especializada\nImplantocard",
             Inches(4.8), Inches(2.9), Inches(3.1), Inches(3.1), size=14, color=INK)
    add_text(slide, "Juliana Cristina Paim Psicóloga Clínica e Neuropsicóloga\nLaboratório Citoprev\nMei Li Acupuntura\nOculare Oftalmologia\nOdontobrasília\nOdontoempresa\nRessonance\nRita Trindade\nRM Clínica Médica e Estética\nSabin\nSouli Psicologia e Psicopedagogia",
             Inches(8.8), Inches(2.9), Inches(3.1), Inches(3.1), size=14, color=INK)
    add_footer(slide, 12, total)

    # 13. Convenios - Saude complementar + Lazer
    slide = prs.slides.add_slide(blank)
    set_bg(slide, WHITE)
    body_color = add_title(slide, "Apêndice", "Convênios de saúde complementar e lazer e bem-estar", dark=False)
    add_card(slide, Inches(0.85), Inches(1.9), Inches(3.2), Inches(4.6), NAVY)
    add_text(slide, "Saúde complementar", Inches(1.15), Inches(2.25), Inches(2.5), Inches(0.3),
             size=18, color=WHITE, bold=True)
    add_text(slide, "Microsom\nOftalmocenter\nImplantomed\nInstituto Oftalmológico Visão\nOlhar Hospital Oftalmológico Ltda.",
             Inches(1.15), Inches(2.8), Inches(2.35), Inches(2.0), size=16, color=WHITE)
    add_card(slide, Inches(4.35), Inches(1.9), Inches(3.8), Inches(4.6), LIGHT)
    add_card(slide, Inches(8.35), Inches(1.9), Inches(4.0), Inches(4.6), LIGHT)
    add_text(slide, "Academia Club 22\nAcademia Companhia Athletica\nAcademia Dom Bosco\nAcademia Runway\nAcademia Team Nogueira\nAcademia Vasco Neto\nASBAC\nAssociação Cristã de Moços\nATP Atividades Físicas\nBancorbrás Consórcios\nBancorbrás Turismo\nBay Park Resort Hotel",
             Inches(4.6), Inches(2.25), Inches(3.1), Inches(3.7), size=14, color=INK)
    add_text(slide, "Camisaria Nyll\nClube dos Previdenciários\nCorpus Studio de Pilates\nElia Spa\nEquilibriom Estética e Podologia\nEscola Ballet Garden\nGrandBittar Hotel\nHotel Fazenda Mestre Darmas\nMontreal Turismo\nNuwa Spa\nStudio Caracóis\nStudio Hair 180 Graus\nThermas do Rio Quente",
             Inches(8.6), Inches(2.25), Inches(3.2), Inches(3.7), size=14, color=INK)
    add_footer(slide, 13, total)

    # 14. Convenios - Servicos
    slide = prs.slides.add_slide(blank)
    set_bg(slide, NAVY)
    add_title(slide, "Apêndice", "Convênios de serviços", dark=True)
    add_text(slide, "Parcerias ligadas ao apoio ao dia a dia do associado identificadas no acervo disponível.", Inches(0.8), Inches(1.75),
             Inches(7.1), Inches(0.5), size=17, color=ICE)
    service_cards = [
        (Inches(1.0), Inches(3.0), TEAL, "Hertz"),
        (Inches(3.4), Inches(3.0), ACCENT, "Lavanderia\nCleaners Club"),
        (Inches(5.8), Inches(3.0), CORAL, "Lavanderia\nSelecta BonaSecco"),
        (Inches(8.2), Inches(3.0), GOLD, "Óptica Elen"),
        (Inches(10.6), Inches(3.0), WHITE, "Grupo Porcão"),
    ]
    for left, top, fill, label in service_cards:
        add_card(slide, left, top, Inches(1.75), Inches(1.9), fill)
        text_color = NAVY if fill == WHITE or fill == GOLD else WHITE
        add_text(slide, label, left + Inches(0.15), top + Inches(0.58), Inches(1.45), Inches(0.7),
                 size=18, color=text_color, bold=True, align=PP_ALIGN.CENTER)
    add_text(slide, "Esses convênios complementam a proposta de valor da ASOF ao conectar representação institucional com utilidade cotidiana.", Inches(1.0), Inches(5.55),
             Inches(11.0), Inches(0.6), size=18, color=ICE, align=PP_ALIGN.CENTER)
    add_footer(slide, 14, total, dark=True)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(OUTPUT_PATH))


if __name__ == "__main__":
    build_deck()
