from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_summary_pdf(summary):

    pdf_file = "reports/AI_Medical_Summary.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(pdf_file)

    story = []

    story.append(
        Paragraph("<b>MediLens AI</b>", styles["Title"])
    )

    story.append(
        Paragraph("Medical Report Analysis", styles["Heading2"])
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
    )

    story.append(
        Paragraph("<br/><br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            "<b>Disclaimer:</b> "
            "This report is AI-generated and should not replace professional medical advice.",
            styles["Italic"]
        )
    )

    doc.build(story)

    return pdf_file