# dogs_cats_birds (MLOps / WSL2 + Conda) — Birds vs Cats vs Dogs

Este projeto implementa um pipeline completo (data engineering → treinamento → avaliação) para classificação de imagens em **3 classes**: **birds**, **cats** e **dogs**, com foco em práticas de **MLOps** (reprodutibilidade, qualidade de dados, avaliação robusta e organização de artefatos).

O trabalho foi desenvolvido a partir do laboratório **`C1W2_Ungraded_Lab_Birds_Cats_Dogs`** (referência original do curso) e consolidado em um projeto “rodável” localmente.

## O que foi feito

### 1) Ambiente (Windows + WSL2)
- Execução em **WSL2 (Linux)** para maior estabilidade com bibliotecas científicas.
- Isolamento de dependências via **Conda**.

### 2) Engenharia de dados (dataset)
- Download/extração e organização dos dados em pastas no formato do Keras (`train/` e `eval/`).
- Limpeza de dados:
  - remoção de arquivos com tamanho 0
  - remoção de arquivos com extensões inesperadas
- Birds (CUB-200-2011): tratamento de **colisões de nomes** na etapa de “flatten” (quando imagens de subpastas são movidas para uma única pasta).

### 3) Experimentos
Foram executados **3 cenários** para evidenciar problemas clássicos de MLOps (principalmente desbalanceamento):

1. **Imbalanced**: treino e avaliação com classes desbalanceadas (simulando um cenário realista).
2. **Balanced**: mesmo modelo, mas com dataset balanceado.
3. **Augmented**: dataset balanceado + **data augmentation** para reduzir overfitting.

### 4) Avaliação (métricas “à prova de desbalanceamento”)
Além de `accuracy`, foram usadas métricas mais apropriadas:
- `balanced_accuracy_score`
- `confusion_matrix`
- `classification_report` (precision/recall/F1)

E foi demonstrado um **baseline ingênuo** (modelo que prevê sempre a classe majoritária) para mostrar como `accuracy` pode enganar.

## Estrutura do projeto

Este projeto está na pasta compactada **`dogs_cats_birds.7z`**.

Estrutura recomendada após extração:

```text
.
├── README.md
├── cleanup.py
├── birds_cats_dogs_mlops.ipynb
├── environment.yml
└── (outros arquivos do projeto)
```

> Observação: durante o desenvolvimento, muitos artefatos foram gravados em `/tmp/...` (WSL2/Linux) para simplificar.

## Como usar

### 1) Pré-requisitos
- Windows 10/11
- WSL2 habilitado + Ubuntu (ou distro Linux)
- Conda instalado **dentro do WSL2**

### 2) Criar e ativar ambiente

```bash
conda create -n mlops python=3.11 -y
conda activate mlops
```

### 3) Instalar dependências

**Opção A (recomendado): via `environment.yml`**

```bash
conda env update -n mlops -f environment.yml
conda activate mlops
```

**Opção B (manual):**

```bash
conda install -c conda-forge -y \
  jupyterlab numpy pandas scikit-learn matplotlib seaborn

pip install tensorflow
```

> Nota MLOps: evitar `pip freeze` para capturar ambiente conda (pode gerar `@ file:///...`). Prefira `environment.yml`.

### 4) Rodar o notebook

```bash
jupyter lab --no-browser --ip=0.0.0.0 --port=8888
```

Abra no navegador do Windows via `http://localhost:8888/?token=...`.

O notebook executa, em geral, as seguintes etapas:
1. download/extração dos dados
2. organização em `train/` e `eval/`
3. limpeza de arquivos inválidos
4. (opcional) criação do dataset desbalanceado
5. treino/avaliação dos modelos
6. geração de métricas e gráficos

## Onde ficam os dados/artefatos

No fluxo atual (WSL2), são usados diretórios temporários:

- Dataset balanceado:
  - `/tmp/data/train`
  - `/tmp/data/eval`
- Dataset desbalanceado:
  - `/tmp/data/imbalanced/train`
  - `/tmp/data/imbalanced/eval`
- Modelos e históricos (se existirem):
  - `/tmp/model-balanced`, `/tmp/history-balanced/history-balanced.csv`
  - `/tmp/model-imbalanced`, `/tmp/history-imbalanced/history-imbalanced.csv`
  - `/tmp/model-augmented`, `/tmp/history-augmented/history-augmented.csv`

## Limpeza (cleanup) 


Para remover os artefatos temporários e “resetar” o ambiente local:

```bash
python cleanup.py
```

O script remove (se existirem):
- `/tmp/data`
- `/tmp/data/imbalanced`
- `/tmp/model-balanced`, `/tmp/model-imbalanced`, `/tmp/model-augmented`
- `/tmp/history-balanced`, `/tmp/history-imbalanced`, `/tmp/history-augmented`
- `/tmp/downloads`
- `/tmp/lab_archive`

> Dica: rode o `cleanup.py` antes de reexecutar o notebook do zero, especialmente se você mudou alguma lógica de preparação do dataset.

## Keras 3 e carregamento de modelos (SavedModel)

Se você estiver em **Keras 3** (TensorFlow 2.16+), pode ver este erro ao tentar `load_model()` em um SavedModel:

> `ValueError: File format not supported ... Keras 3 only supports V3 .keras files and legacy H5 ...`

### Opção A (inferência): `TFSMLayer`

```python
import keras

layer = keras.layers.TFSMLayer('/tmp/model-balanced', call_endpoint='serving_default')
model = keras.Sequential([layer])
```

### Opção B (treino/continuação): TensorFlow 2.15 (legado)

```bash
pip install "tensorflow==2.15.1" "numpy<2"
```

## Sobre os arquivos `.7z` (referência do lab e projeto compactado)

Os arquivos compactados usados neste repositório:
- `dogs_cats_birds.7z` (projeto)
- `C1W2_Ungraded_Lab_Birds_Cats_Dogs.7z` (referência original)

**these documents can only be used in code execution**.

### Por que a extração de texto falha?
Isso ocorre porque:
- `.7z` é um container compactado, não um documento com texto linear
- o conteúdo costuma ser binário (imagens, notebooks, modelos)
- o extrator de texto pode não suportar o formato 7z ou o arquivo pode estar organizado de forma que não há texto diretamente extraível

### Exemplo: como extrair o `.7z` via Python (WSL)

```python
import os
import subprocess

archive = 'dogs_cats_birds.7z'
out_dir = '/tmp/dogs_cats_birds'

os.makedirs(out_dir, exist_ok=True)

# Requer p7zip no Ubuntu/WSL:
#   sudo apt-get update && sudo apt-get install -y p7zip-full

subprocess.check_call(['7z', 'x', archive, f'-o{out_dir}', '-y'])
print('Extraído em:', out_dir)
```

## Troubleshooting

### TensorFlow não encontrado
```bash
conda activate mlops
pip install tensorflow
```

### Logs sobre CUDA (CPU)
Em CPU/WSL2 é comum ver logs dizendo que não encontrou drivers CUDA. Não é erro.

### Colisão de nomes no flatten de birds
Se aparecer `Destination path ... already exists`, ajuste a estratégia de renomeação (prefixo por espécie ou sufixo incremental/hash).

## Créditos
- Baseado no laboratório: `C1W2_Ungraded_Lab_Birds_Cats_Dogs.7z`.
