import csv
from fpdf import FPDF

# Step 1: Read CSV and analyze data
data = {}
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        price = int(row["Price"])
        if name in data:
            data[name] += price
        else:
            data[name] = price

# Step 2: Create a PDF report using FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Sales Summary Report", ln=1, align="C")

pdf.ln(10)  # Line break
pdf.set_font("Arial", size=12)
for name, total in data.items():
    pdf.cell(200, 10, txt=f"{name}: Rs. {total}", ln=1)

# Step 3: Save the PDF file
pdf.output("sales_report.pdf")

# Step 4: Confirmation message
print("✅ PDF report generated: sales_report.pdf")
