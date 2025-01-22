import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "SiSedeInversiones"
copyright = "2025, Jelsin Palomino"
author = "Jelsin Palomino"
release = "v0.0.1"

extensions_part1 = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
extensions_part2 = ["sphinx.ext.napoleon"]
extensions = extensions_part1 + extensions_part2

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "es"
# html_theme = 'alabaster'
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_theme_options = {
    "repository_url": "https://github.com/JelsinPalomino/SiSedeInversiones",
    "use_repository_button": True,
    "collapse_navbar": False,
    "use_sidenotes": True,
}
html_logo = "logo.jpg"
html_title = "SiSedeInversiones - v0.0.1"


# autoclass_content = "both"
