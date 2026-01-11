from .nodes import (
    TranslateLocallyNode,
    SelectOrDownloadTranslateModelNode,
)

# Mapping de classes pour ComfyUI
NODE_CLASS_MAPPINGS = {
    "TranslateLocally": TranslateLocallyNode,
    "SelectOrDownloadTranslateModel": SelectOrDownloadTranslateModelNode,
}

# Noms affichés dans l'UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "TranslateLocally": "Translate Locally (Offline)",
    "SelectOrDownloadTranslateModel": "Download and select Translate Model",
}
