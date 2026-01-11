import os
import glob
import subprocess

class TranslateLocallyNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "model": ("STRING", {"default": "en-fr-tiny"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "translate"
    CATEGORY = "Text / Translation"

    def find_binary(self):
        """Search for translateLocally.exe in the node folder"""
        base_dir = os.path.dirname(__file__)
        exe_files = glob.glob(os.path.join(base_dir, "translateLocally*.exe"))
        if exe_files:
            return exe_files[0]
        return None

    def translate(self, text, model):
        binary_path = self.find_binary()
        if not binary_path or not os.path.isfile(binary_path):
            return (f"ERROR: translateLocally.exe not found. Checked path: {binary_path}",)

        try:
            process = subprocess.run(
                [binary_path, "-m", model],
                input=text,
                text=True,
                capture_output=True,
                check=False,
                encoding="utf-8"
            )
            output = process.stdout.strip() or process.stderr.strip()
            if not output:
                output = "ERROR: The binary did not return any output"
            return (output,)
        except Exception as e:
            return (f"ERROR: Python exception: {e}",)


class SelectOrDownloadTranslateModelNode:
    # List of all official models
    MODELS = [
        "cs-en-base", "cs-en-tiny", "en-cs-base", "en-cs-tiny",
        "de-en-base", "de-en-tiny", "en-de-base", "en-de-tiny",
        "es-en-tiny", "en-es-tiny", "et-en-tiny", "en-et-tiny",
        "is-en-base", "is-en-tiny", "nb-en-tiny", "nn-en-tiny",
        "bg-en-tiny", "en-bg-tiny", "pl-en-tiny", "en-pl-tiny",
        "fr-en-tiny", "en-fr-tiny", "hbs-eng-tiny", "sl-en-tiny",
        "mk-en-tiny", "mt-en-tiny", "tr-en-tiny", "sq-en-tiny",
        "ca-en-tiny", "el-en-tiny", "uk-en-tiny"
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": (cls.MODELS,),  # simple list; ComfyUI will display as selectable options
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "select_translate_model"
    CATEGORY = "Text / Translation"

    def find_binary(self):
        """Search for translateLocally.exe in the node folder"""
        base_dir = os.path.dirname(__file__)
        exe_files = glob.glob(os.path.join(base_dir, "translateLocally*.exe"))
        if exe_files:
            return exe_files[0]
        return None

    def list_local_models(self, binary_path):
        """Retrieve models already present locally"""
        try:
            process = subprocess.run(
                [binary_path, "--list-models"],
                text=True,
                capture_output=True,
                check=False,
                encoding="utf-8"
            )
            output = process.stdout.strip() or ""
            local_models = []
            for line in output.splitlines():
                if "To invoke do -m" in line:
                    model_name = line.split("To invoke do -m")[-1].strip()
                    local_models.append(model_name)
            return local_models
        except Exception:
            return []

    def download_model(self, binary_path, model):
        """Download the model via translateLocally"""
        try:
            process = subprocess.run(
                [binary_path, "--download-model", model],
                text=True,
                capture_output=True,
                check=False,
                encoding="utf-8"
            )
            return process.stdout.strip() or process.stderr.strip()
        except Exception as e:
            return f"ERROR: Python exception: {e}"

    def select_translate_model(self, model):
        binary_path = self.find_binary()
        if not binary_path or not os.path.isfile(binary_path):
            return (f"ERROR: translateLocally.exe not found. Checked path: {binary_path}",)

        # Check if the model is already present locally
        local_models = self.list_local_models(binary_path)
        if model in local_models:
            return (model,)

        # Otherwise, download the model
        download_output = self.download_model(binary_path, model)
        local_models = self.list_local_models(binary_path)
        if model in local_models:
            return (model,)
        else:
            return (f"ERROR: Failed to download model {model}. Output: {download_output}",)
