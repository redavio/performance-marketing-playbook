"""Build deliverables/slide-template.pptx (needs python-pptx). Plain, brand-neutral layouts."""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

INK, MUTED, LINE = RGBColor(0x1F, 0x29, 0x37), RGBColor(0x6B, 0x72, 0x80), RGBColor(0xE5, 0xE7, 0xEB)
GREEN, AMBER, RED = RGBColor(0x16, 0xA3, 0x4A), RGBColor(0xD9, 0x77, 0x06), RGBColor(0xDC, 0x26, 0x26)
prs = Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
blank = prs.slide_layouts[6]

def text(slide, x, y, w, h, s, size=18, bold=False, color=INK):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, line in enumerate(s.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line; p.font.size = Pt(size); p.font.bold = bold; p.font.color.rgb = color
    return tb

def slide(title, note=""):
    s = prs.slides.add_slide(blank)
    text(s, 0.6, 0.4, 12, 1.0, title, 28, True)
    if note: text(s, 0.6, 6.8, 12, 0.4, note, 11, color=MUTED)
    return s

def table(s, rows, x=0.6, y=1.7, w=12.1):
    t = s.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(0.45 * len(rows))).table
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            cell = t.cell(r, c); cell.text = v
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(14); p.font.bold = r == 0
    return t

s = prs.slides.add_slide(blank)
text(s, 0.6, 2.4, 12, 1.2, "[Deck name]", 44, True)
text(s, 0.6, 3.6, 12, 1.0, "[Company] · [Period] · [Presenter]", 20, color=MUTED)

s = slide("[One-sentence headline: pipeline vs plan and the main reason]", "Source: budget tracker, [period]")
for i, (k, v) in enumerate([("Pipeline vs plan", "[+/-X%]"), ("SAOs", "[N]"), ("Spend", "[$X]"), ("Cost per SAO", "[$X]")]):
    text(s, 0.6 + i * 3.1, 2.4, 2.9, 1.0, v, 40, True); text(s, 0.6 + i * 3.1, 3.4, 2.9, 0.6, k, 16, color=MUTED)

s = slide("[Funnel takeaway, e.g. SQLs on plan but SAO rate fell to 48%]", "Status: green ≥100% of plan to date, amber 80-99%, red <80% (rule of thumb)")
table(s, [["Stage", "Plan", "Actual", "Variance", "Status"]] + [[st, "", "", "", ""] for st in ("MQLs", "SQLs", "SAOs", "Pipeline", "Closed won", "Spend")])
for i, (c, l) in enumerate([(GREEN, "On plan"), (AMBER, "Watch"), (RED, "Act")]):
    sh = s.shapes.add_shape(1, Inches(0.6 + i * 1.6), Inches(5.3), Inches(0.25), Inches(0.25)); sh.fill.solid(); sh.fill.fore_color.rgb = c; sh.line.fill.background()
    text(s, 0.9 + i * 1.6, 5.22, 1.2, 0.4, l, 12, color=MUTED)

s = slide("[Trend takeaway, e.g. pipeline caught up in month 3 after the budget shift]", "Chart: [metric] by month vs plan. Source: [system], [period]")
box = s.shapes.add_shape(1, Inches(0.6), Inches(1.7), Inches(12.1), Inches(4.8)); box.fill.background(); box.line.color.rgb = LINE
text(s, 5.2, 3.8, 4, 0.6, "[Insert chart]", 18, color=MUTED)

def two(title, a, b, note=""):
    s = slide(title, note)
    for i, (h, body) in enumerate((a, b)):
        text(s, 0.6 + i * 6.2, 1.7, 5.8, 0.5, h, 20, True); text(s, 0.6 + i * 6.2, 2.4, 5.8, 3.5, body, 16)
two("[What drove the result]", ("Levers we control", "• [Budget, bids, copy, pages, offers]\n• \n• "), ("Outside forces", "• [Seasonality, competitors, market]\n• \n• "))
two("[Capture and creation each judged on their own measures]", ("Demand capture", "• Pipeline: \n• Cost per SAO: \n• Branded vs non-branded search: "), ("Demand creation (lower confidence)", "• Target-account engagement: \n• Self-reported source: \n• Influenced pipeline: "), "Creation is never judged on last click.")

s = slide("[Tests: what we learned]")
table(s, [["Test", "ICS score", "Predicted", "Actual", "Decision"]] + [["", "", "", "", ""] for _ in range(4)])

s = slide("[Plan: goal, budget, priorities]")
text(s, 0.6, 1.7, 12, 4, "Goal: [pipeline], [revenue]\nBudget: [total], capture [X] / creation [Y]\nPriorities:\n1. [Initiative · principle · owner]\n2. \n3. ", 20)

s = slide("[Asks and risks]")
table(s, [["Ask or risk", "Owner", "By when"]] + [["", "", ""] for _ in range(4)])

s = slide("Appendix")
text(s, 0.6, 1.7, 12, 1, "[Detail tables]", 18, color=MUTED)

out = Path(__file__).resolve().parent.parent / "deliverables" / "slide-template.pptx"
prs.save(out); print("wrote", out)
