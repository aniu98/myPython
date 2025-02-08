# pip install docling


from docling.document_converter import DocumentConverter

source = "C:\\Users\\admin\\Desktop\\SKM_C36824120509390.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"