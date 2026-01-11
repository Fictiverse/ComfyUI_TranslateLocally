# ComfyUI Translate Locally Nodes

This repository contains two nodes for **ComfyUI** to enable offline translation using [translateLocally](https://github.com/XapaJIaMnu/translateLocally).  

- **Translate Locally (Offline)**: Translate text using a selected offline model.  
- **Download and Select Translate Model**: Download official translation models and select one for use.  

---

## Installation

1. **Download translateLocally.exe CLI**       

   Go to the latest release page:  
   [https://github.com/XapaJIaMnu/translateLocally/releases/tag/latest](https://github.com/XapaJIaMnu/translateLocally/releases/tag/latest)  

2. **Rename the binary**  

   Rename the downloaded file to:  ```translateLocally.exe```

3. **Place it in your ComfyUI custom nodes folder**  

   Place the file in the following path:  ```ComfyUI\custom_nodes\ComfyUI_TranslateLocally```   


   Your folder structure should look like this:   

``` ComfyUI/ 
└─ custom_nodes/
  └─ ComfyUI_TranslateLocally/
    ├─ nodes.py
    ├─ _init_.py
    └─ translateLocally.exe
```

      
---

## Usage

### Translate Locally (Offline)

**Inputs:**

- `text` (STRING, multiline) – Text to translate  
- `model` (STRING) – Model to use (e.g., `en-fr-tiny`)  

**Output:**

- Translated text (STRING)  

---

### Download and Select Translate Model

**Inputs:**

- `model` (STRING) – Select from official models. The node will check if the model is already downloaded; if not, it will download it automatically.  

**Output:**

- Model code (STRING) – e.g., `en-fr-tiny`  

**Official Models:**

| Model Code    | Type | Source → Target |
|---------------|------|----------------|
| cs-en-base    | base | Czech → English |
| cs-en-tiny    | tiny | Czech → English |
| en-cs-base    | base | English → Czech |
| en-cs-tiny    | tiny | English → Czech |
| de-en-base    | base | German → English |
| de-en-tiny    | tiny | German → English |
| en-de-base    | base | English → German |
| en-de-tiny    | tiny | English → German |
| es-en-tiny    | tiny | Spanish → English |
| en-es-tiny    | tiny | English → Spanish |
| et-en-tiny    | tiny | Estonian → English |
| en-et-tiny    | tiny | English → Estonian |
| is-en-base    | base | Icelandic → English |
| is-en-tiny    | tiny | Icelandic → English |
| nb-en-tiny    | tiny | Norwegian (Bokmål) → English |
| nn-en-tiny    | tiny | Norwegian (Nynorsk) → English |
| bg-en-tiny    | tiny | Bulgarian → English |
| en-bg-tiny    | tiny | English → Bulgarian |
| pl-en-tiny    | tiny | Polish → English |
| en-pl-tiny    | tiny | English → Polish |
| fr-en-tiny    | tiny | French → English |
| en-fr-tiny    | tiny | English → French |
| hbs-eng-tiny  | tiny | Serbo-Croatian → English |
| sl-en-tiny    | tiny | Slovene → English |
| mk-en-tiny    | tiny | Macedonian → English |
| mt-en-tiny    | tiny | Maltese → English |
| tr-en-tiny    | tiny | Turkish → English |
| sq-en-tiny    | tiny | Albanian → English |
| ca-en-tiny    | tiny | Catalan → English |
| el-en-tiny    | tiny | Greek → English |
| uk-en-tiny    | tiny | Ukrainian → English |

---

## Notes

- Only tested on **Windows**, as it requires the `translateLocally.exe` binary.  
- Make sure `translateLocally.exe` is in the same folder as this node (`ComfyUI_TranslateLocally`).  
- Models are downloaded (once and only when it is missing) and reused automatically.  
- Install only if you trust this repo : https://github.com/XapaJIaMnu/translateLocally
- My repo is just a wrapper, i am not the author of this tool.   
  
---

## References

- [translateLocally GitHub](https://github.com/XapaJIaMnu/translateLocally)


      
