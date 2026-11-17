"""Build the slide template (needs python-pptx).

    python3 scripts/build_slide_template.py      # writes deliverables/slide-template.pptx with [placeholders]

fill.py calls build(path, fields) to write a copy filled with a company's plan numbers and stage names.
"""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

INK, MUTED, LINE = RGBColor(0x1F, 0x29, 0x37), RGBColor(0x6B, 0x72, 0x80), RGBColor(0xE5, 0xE7, 0xEB)
GREEN, AMBER, RED = RGBColor(0x16, 0xA3, 0x4A), RGBColor(0xD9, 0x77, 0x06), RGBColor(0xDC, 0x26, 0x26)


def build(out, f=None):
    f = f or {}
    v = lambda key, placeholder: f.get(key, placeholder)
    MQLs, SQLs = v("MQLs", "MQLs"), v("SQLs", "SQLs")
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    blank = prs.slide_layouts[6]

    def text(s, x, y, w, h, body, size=18, bold=False, color=INK):
        tf = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)).text_frame
        tf.word_wrap = True
        for i, line in enumerate(body.split("\n")):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text, p.font.size, p.font.bold, p.font.color.rgb = line, Pt(size), bold, color

    def slide(title, note=""):
        s = prs.slides.add_slide(blank)
        text(s, 0.6, 0.4, 12, 1.0, title, 28, True)
        if note:
            text(s, 0.6, 6.8, 12, 0.4, note, 11, color=MUTED)
        return s

    def table(s, rows, y=1.7):
        t = s.shapes.add_table(len(rows), len(rows[0]), Inches(0.6), Inches(y), Inches(12.1), Inches(0.45 * len(rows))).table
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                t.cell(r, c).text = val
                for p in t.cell(r, c).text_frame.paragraphs:
                    p.font.size, p.font.bold = Pt(14), r == 0

    def two(title, a, b, note=""):
        s = slide(title, note)
        for i, (h, body) in enumerate((a, b)):
            text(s, 0.6 + i * 6.2, 1.7, 5.8, 0.5, h, 20, True)
            text(s, 0.6 + i * 6.2, 2.4, 5.8, 3.5, body, 16)

    # 1. Title
    s = prs.slides.add_slide(blank)
    text(s, 0.6, 2.4, 12, 1.2, "[Deck name]", 44, True)
    text(s, 0.6, 3.6, 12, 1.0, f"{v('company', '[Company]')} · {v('period', '[Period]')} · [Presenter]", 20, color=MUTED)

    # 2. Headline
    s = slide("[One-sentence headline: pipeline vs plan and the main reason]", "Plan numbers from the budget tracker. Fill actuals for the period.")
    for i, (k, plan) in enumerate([("Pipeline (plan)", v("pipeline_goal", "[$X]")), ("SAOs (plan)", v("saos", "[N]")),
                                   ("Spend (plan)", v("budget", "[$X]")), ("Cost per SAO (plan)", v("cost_per_sao", "[$X]"))]):
        text(s, 0.6 + i * 3.1, 2.4, 2.9, 1.0, plan, 36, True)
        text(s, 0.6 + i * 3.1, 3.4, 2.9, 0.6, k, 16, color=MUTED)
        text(s, 0.6 + i * 3.1, 4.0, 2.9, 0.6, "Actual: [ ]", 16)

    # 3. Funnel vs plan
    s = slide("[Funnel takeaway, e.g. SQLs on plan but SAO rate fell to 48%]",
              "Plan shown for the full period; compare actuals with plan to date. Status: green ≥100% of plan to date, amber 80-99%, red <80% (rule of thumb).")
    table(s, [["Stage", "Plan", "Actual", "Variance", "Status"],
              [MQLs, v("mqls", ""), "", "", ""], [SQLs, v("sqls", ""), "", "", ""], ["SAOs", v("saos", ""), "", "", ""],
              ["Pipeline", v("pipeline_goal", ""), "", "", ""], ["Closed won", v("closed_won", ""), "", "", ""],
              ["Spend", v("budget", ""), "", "", ""]])
    for i, (c, label) in enumerate([(GREEN, "On plan"), (AMBER, "Watch"), (RED, "Act")]):
        sh = s.shapes.add_shape(1, Inches(0.6 + i * 1.6), Inches(5.3), Inches(0.25), Inches(0.25))
        sh.fill.solid(); sh.fill.fore_color.rgb = c; sh.line.fill.background()
        text(s, 0.9 + i * 1.6, 5.22, 1.2, 0.4, label, 12, color=MUTED)

    # 4. Trend
    s = slide("[Trend takeaway, e.g. pipeline caught up in month 3 after the budget shift]",
              f"Chart: pipeline by month vs plan ({v('monthly_pipeline', '[$X]')} a month). Source: [system], [period].")
    box = s.shapes.add_shape(1, Inches(0.6), Inches(1.7), Inches(12.1), Inches(4.8))
    box.fill.background(); box.line.color.rgb = LINE
    text(s, 5.2, 3.8, 4, 0.6, "[Insert chart]", 18, color=MUTED)

    # 5-6. Drivers, capture vs creation
    two("[What drove the result]", ("Levers we control", "• [Budget, bids, copy, pages, offers]\n• \n• "),
        ("Outside forces", "• [Seasonality, competitors, market]\n• \n• "))
    two("[Capture and creation each judged on their own measures]",
        ("Demand capture", f"• Budget: {v('capture_budget', '[$X]')}\n• Sourced pipeline: \n• Cost per SAO: \n• Branded vs non-branded search: "),
        ("Demand creation (lower confidence)", f"• Budget: {v('creation_budget', '[$X]')}\n• Target-account engagement: \n• Self-reported source: \n• Influenced pipeline (not added to sourced): "),
        "Creation is never judged on last click.")

    # 7. Tests
    s = slide("[Tests: what we learned]")
    table(s, [["Test", "ICS score", "Predicted", "Actual", "Decision"]] + [["", "", "", "", ""] for _ in range(4)])

    # 8. Plan
    s = slide("[Plan: goal, budget, priorities]")
    text(s, 0.6, 1.7, 12, 4,
         f"Goal: {v('pipeline_goal', '[pipeline]')} pipeline, {v('revenue', '[revenue]')} expected closed won\n"
         f"Budget: {v('budget', '[total]')}, capture {v('capture_budget', '[X]')} / creation {v('creation_budget', '[Y]')}\n"
         f"Funnel: {v('mqls', '[N]')} {MQLs} → {v('sqls', '[N]')} {SQLs} → {v('saos', '[N]')} SAOs\n"
         "Priorities:\n1. [Initiative · principle · owner]\n2. \n3. ", 20)

    # 9-10. Asks, appendix
    s = slide("[Asks and risks]")
    table(s, [["Ask or risk", "Owner", "By when"]] + [["", "", ""] for _ in range(4)])
    s = slide("Appendix")
    text(s, 0.6, 1.7, 12, 1, "[Detail tables]", 18, color=MUTED)
    prs.save(out)


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "deliverables" / "slide-template.pptx"
    build(out)
    print("wrote", out)
