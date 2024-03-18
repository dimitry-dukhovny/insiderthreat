# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Insider Threat Program'
copyright = '2024, Dimitry Dukhovny'
author = 'Dimitry Dukhovny'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    'sphinx.ext.graphviz',
    'rst2pdf.pdfbuilder',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'images/logo_extract.png'

html_theme_options = {
#    'codebgcolor': '#000000',
#    'codetextcolor': '#FFFF00',
#    'sidebarbgcolor': '#7C7C7C',
}

master_doc = 'index'

pdf_documents = [
    (master_doc, 'insiderthreat', 'Insider Threat Program', 'Dimitry Dukhovny'),
]

pdf_stylesheets = ['sphinx']
pdf_style_path = ['.', '_styles']
pdf_use_index = False
pdf_use_modindex = False
pdf_use_coverpage = True
pdf_cover_template = 'sphinxcover.tmpl'
pdf_toc_depth = 9999
pdf_use_numbered_links = True
pdf_fit_background_mode = 'scale'
pdf_repeat_table_rows = False
pdf_smartquotes = 0

