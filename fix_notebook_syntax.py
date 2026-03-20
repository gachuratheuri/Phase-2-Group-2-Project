import nbformat

NB_PATH = r"C:\Users\david\Documents\Flatiron\Phase2\Phase-2-Group-2-Project\notebooks\exploratory.ipynb"
nb = nbformat.read(NB_PATH, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'code':
        # Replace the literal newlines inside these specific string literals with escaped \n
        replacements = [
            ("'Top 10 Movie Genres by Average Worldwide Box Office Revenue\n", "'Top 10 Movie Genres by Average Worldwide Box Office Revenue\\n"),
            ("'Does Audience Rating Drive Box Office Revenue?\n", "'Does Audience Rating Drive Box Office Revenue?\\n"),
            ("'Which Budget Range Delivers the Best Return on Investment (ROI)?\n", "'Which Budget Range Delivers the Best Return on Investment (ROI)?\\n"),
            ("'Average Worldwide Box Office Revenue by Year\n", "'Average Worldwide Box Office Revenue by Year\\n"),
            ("'Micro\n", "'Micro\\n"),
            ("'Low\n", "'Low\\n"),
            ("'Mid\n", "'Mid\\n"),
            ("'High\n", "'High\\n"),
            ("'Blockbuster\n", "'Blockbuster\\n"),
            ("'Sweet Spot:\n", "'Sweet Spot:\\n"),
            ("'COVID-19\n", "'COVID-19\\n")
        ]
        
        for old, new in replacements:
            cell.source = cell.source.replace(old, new)

nbformat.write(nb, NB_PATH)
print("Syntax errors fixed in notebook.")
