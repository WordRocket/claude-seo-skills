#!/usr/bin/env python3
"""Build playbooks/seo-tracker.xlsx (opens in Excel, Google Sheets, Numbers). Standard library only.

  python3 scripts/build-seo-tracker.py

Sheet 1 "Page 2 shortlist": queries Google almost ranks, the fix, the date, and a check-on date 21 days later that turns
orange when due. Sheet 2 "AI answers log": the exact questions asked in ChatGPT / Perplexity / AI Mode and whether you
were named. Sheet 3 "30 days": the plan with a Done column. Sheet 4 "How to use".
"""
import datetime as dt
import os
import zipfile
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(__file__), "..", "playbooks", "seo-tracker.xlsx")


def col(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def serial(d):
    return (d - dt.date(1899, 12, 30)).days


def cell(ref, v, style=0):
    if v is None or v == "":
        return f'<c r="{ref}" s="{style}"/>' if style else ""
    if isinstance(v, tuple) and v[0] == "f":
        return f'<c r="{ref}" s="{style}"><f>{escape(v[1])}</f></c>'
    if isinstance(v, (int, float)):
        return f'<c r="{ref}" s="{style}"><v>{v}</v></c>'
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{escape(str(v))}</t></is></c>'


def sheet(rows, widths, styles=None, freeze=True, extra=""):
    """rows: list of lists; styles: function(row_idx, col_idx) -> style id."""
    cols = "".join(f'<col min="{i}" max="{i}" width="{w}" customWidth="1"/>' for i, w in enumerate(widths, 1))
    data = []
    for r, row in enumerate(rows, 1):
        cells = "".join(cell(f"{col(c)}{r}", v, styles(r, c) if styles else 0) for c, v in enumerate(row, 1))
        data.append(f'<row r="{r}">{cells}</row>')
    pane = ('<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" '
            'state="frozen"/></sheetView></sheetViews>') if freeze else '<sheetViews><sheetView workbookViewId="0"/></sheetViews>'
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
            f'{pane}<sheetFormatPr defaultRowHeight="18"/><cols>{cols}</cols><sheetData>{"".join(data)}</sheetData>'
            f'{extra}</worksheet>')


# ---------- Sheet 1: Page 2 shortlist ----------
P_HEAD = ["Query (exact words)", "Page URL", "Impressions", "Clicks", "CTR", "Avg position", "Fix planned",
          "Date fixed", "Check on (day 21)", "Position after", "Clicks after (same length period)", "Change in clicks", "Notes"]
P_W = [34, 34, 12, 9, 8, 11, 40, 12, 15, 12, 18, 14, 30]
today = dt.date.today()
p_examples = [
    ["EXAMPLE: water heater replacement cost (delete me)", "/water-heater-replacement", 1200, 9, None, 11.4,
     "Price range in the first 2 lines, tank vs tankless table, 3 job photos", serial(today - dt.timedelta(days=3)),
     None, "", "", None, "Linked from the homepage + 2 service pages"],
    ["EXAMPLE: emergency plumber open sunday (delete me)", "/emergency-plumbing", 640, 4, None, 9.2,
     "Answer the hours question first; add Sunday call-out price", "", None, "", "", None, ""],
]
p_rows = [P_HEAD]
for i in range(2, 202):
    ex = p_examples[i - 2] if i - 2 < len(p_examples) else [""] * 13
    row = list(ex)
    row[4] = ("f", f'IF(OR(C{i}="",C{i}=0),"",D{i}/C{i})')
    row[8] = ("f", f'IF(H{i}="","",H{i}+21)')
    row[11] = ("f", f'IF(K{i}="","",K{i}-D{i})')
    p_rows.append(row)


def p_style(r, c):
    if r == 1:
        return 1
    if c in (8, 9):
        return 2
    if c == 5:
        return 4
    if c in (7, 13):
        return 3
    return 0


p_extra = (
    '<autoFilter ref="A1:M201"/>'
    '<conditionalFormatting sqref="I2:I201"><cfRule type="expression" dxfId="0" priority="1">'
    '<formula>AND(I2&lt;&gt;"",I2&lt;=TODAY(),J2="")</formula></cfRule></conditionalFormatting>')

# ---------- Sheet 2: AI answers log ----------
A_HEAD = ["Date", "Question (exact words your buyer would type)", "Tool", "Are you named?", "Your position / how",
          "Linked to your site?", "Who else is named", "Why the answer says they're good", "Page you'll fix", "Notes"]
A_W = [12, 46, 18, 14, 20, 16, 30, 40, 28, 28]
TOOLS = "ChatGPT,Perplexity,Google AI Mode,AI Overview,Claude,Copilot,Gemini"
a_rows = [A_HEAD]
for i in range(2, 202):
    a_rows.append([""] * 10)


def a_style(r, c):
    if r == 1:
        return 1
    if c == 1:
        return 2
    if c in (2, 7, 8, 10):
        return 3
    return 0


a_extra = (
    '<autoFilter ref="A1:J201"/>'
    '<dataValidations count="3">'
    f'<dataValidation type="list" allowBlank="1" sqref="C2:C201"><formula1>"{TOOLS}"</formula1></dataValidation>'
    '<dataValidation type="list" allowBlank="1" sqref="D2:D201"><formula1>"Yes,No"</formula1></dataValidation>'
    '<dataValidation type="list" allowBlank="1" sqref="F2:F201"><formula1>"Yes,No"</formula1></dataValidation>'
    '</dataValidations>')

# ---------- Sheet 3: 30 days ----------
PLAN = [
    ("Week 1", "Day 1", "Search Console: Performance › Search results › Average position on › filter Position > 7 › sort by Impressions. Copy the top 10 into 'Page 2 shortlist'."),
    ("Week 1", "Day 2", "Fix shortlist page 1: audit it with ranking principles, answer first, add what the top 5 don't have, link to it from 2–3 pages."),
    ("Week 1", "Day 3", "AI switches: robots.txt lets in the AI search crawlers (OAI-SearchBot, PerplexityBot, Claude-SearchBot, Googlebot, Bingbot); check your host or Cloudflare's AI bot setting; add the site to Bing Webmaster Tools."),
    ("Week 1", "Day 4", "Write 5 exact questions your best buyer would type. Ask ChatGPT, Perplexity and Google AI Mode. Log them in 'AI answers log'."),
    ("Week 1", "Day 5", "Save your humanizer prompt (3 samples of your writing) in ChatGPT Custom instructions or Claude Instructions."),
    ("Week 1", "Days 6–7", "Fix shortlist pages 2 and 3."),
    ("Week 2", "Days 8–10", "Write one new page that answers your best exact question in its first 2 sentences, with something only you have."),
    ("Week 2", "Days 11–12", "Fix shortlist pages 4 and 5. Request indexing for each fixed page (URL Inspection)."),
    ("Week 2", "Days 13–14", "Write a second new page. Link both from related pages with descriptive link text."),
    ("Week 3", "Day 15", "Search \"your brand\" -site:yourdomain.com. Find sites that mention you without a link and send 3 short, polite asks."),
    ("Week 3", "Days 16–17", "Find 3 resource pages or 'best of' lists in your niche where a page of yours truly fits; pitch one."),
    ("Week 3", "Days 18–19", "Answer one real question on Reddit, LinkedIn or YouTube where those already rank for your search. Follow the community's rules."),
    ("Week 3", "Days 20–21", "Check-on day for the first fixes: fill 'Position after' and 'Clicks after'."),
    ("Week 4", "Days 22–24", "Search Console › Performance › Compare the last 28 days with the 28 before. Watch clicks first. Big site (over 500 pages)? Check the Page indexing report too."),
    ("Week 4", "Days 25–26", "Ask your 5 questions again in the same tools. Note what changed."),
    ("Week 4", "Days 27–28", "Pick next month's 5 pages: the shortlist rows that moved least, plus 2 new questions."),
    ("Week 4", "Days 29–30", "Write down what worked. Keep doing that; drop what didn't."),
]
L_HEAD = ["Week", "When", "Task", "Done?", "Notes"]
L_W = [9, 11, 110, 9, 30]
l_rows = [L_HEAD] + [[w, d, t, "", ""] for w, d, t in PLAN]


def l_style(r, c):
    if r == 1:
        return 1
    if c == 3:
        return 3
    return 0


l_extra = (f'<dataValidations count="1"><dataValidation type="list" allowBlank="1" sqref="D2:D{len(l_rows)}">'
           '<formula1>"Yes,No"</formula1></dataValidation></dataValidations>')

# ---------- Sheet 4: How to use ----------
HOW = [
    ["How to use this tracker"],
    ["1. Page 2 shortlist: delete the 2 EXAMPLE rows. Copy queries from Search Console › Performance › Search results (Average position on, Position > 7, sorted by Impressions)."],
    ["2. When you fix a page, type the date in 'Date fixed'. 'Check on' fills in 21 days later and turns orange when it's due."],
    ["3. On the check-on day, compare the same length of time before and after (e.g. 21 days vs the 21 days before the fix)."],
    ["4. AI answers log: ask the exact sentence your buyer would type, in each tool, and write down who gets named and why."],
    ["5. 30 days: one task a day, about 15–30 minutes. Mark Done."],
    [""],
    ["Free Claude skills that do most of this with you: github.com/WordRocket/claude-seo-skills (seo-audit, ranking-principles,"],
    ["generative-ai-search, ai-humanizer, backlink-maxing, borrowed-authority). Nobody can promise rankings: results vary."],
]

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<numFmts count="1"><numFmt numFmtId="164" formatCode="yyyy-mm-dd"/></numFmts>
<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font></fonts>
<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FF0E2A47"/><bgColor indexed="64"/></patternFill></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="5">
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>
<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
<xf numFmtId="9" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
<dxfs count="2">
<dxf><font><b/><color rgb="FF9A3412"/></font><fill><patternFill patternType="solid"><bgColor rgb="FFFED7AA"/></patternFill></fill></dxf>
<dxf><font><color rgb="FF9CA3AF"/><strike/></font></dxf>
</dxfs>
</styleSheet>"""

WORKBOOK = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets><sheet name="Page 2 shortlist" sheetId="1" r:id="rId1"/><sheet name="AI answers log" sheetId="2" r:id="rId2"/><sheet name="30 days" sheetId="3" r:id="rId3"/><sheet name="How to use" sheetId="4" r:id="rId5"/></sheets>
<definedNames><definedName name="_xlnm._FilterDatabase" localSheetId="0" hidden="1">'Page 2 shortlist'!$A$1:$M$201</definedName><definedName name="_xlnm._FilterDatabase" localSheetId="1" hidden="1">'AI answers log'!$A$1:$J$201</definedName></definedNames>
<calcPr calcId="0" fullCalcOnLoad="1"/>
</workbook>"""

WB_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet3.xml"/>
<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet4.xml"/>
</Relationships>"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet3.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet4.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>"""

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", TYPES)
    z.writestr("_rels/.rels", ROOT_RELS)
    z.writestr("xl/workbook.xml", WORKBOOK)
    z.writestr("xl/_rels/workbook.xml.rels", WB_RELS)
    z.writestr("xl/styles.xml", STYLES)
    z.writestr("xl/worksheets/sheet1.xml", sheet(p_rows, P_W, p_style, extra=p_extra))
    z.writestr("xl/worksheets/sheet2.xml", sheet(a_rows, A_W, a_style, extra=a_extra))
    z.writestr("xl/worksheets/sheet3.xml", sheet(l_rows, L_W, l_style, extra=l_extra))
    z.writestr("xl/worksheets/sheet4.xml", sheet(HOW, [140], lambda r, c: 1 if r == 1 else 0, freeze=False))
print(f"{os.path.abspath(OUT)} ({os.path.getsize(OUT) / 1024:.0f} KB)")
