#!/usr/bin/env python3
"""
cleanup.py - Remove artefatos temporários do projeto Birds/Cats/Dogs
Uso: python scripts/cleanup.py
"""

import os
import shutil
from pathlib import Path

# Diretórios a serem removidos
DIRS_TO_REMOVE = [
    "/tmp/data",
    "/tmp/data/imbalanced",
    "/tmp/model-balanced",
    "/tmp/model-imbalanced",
    "/tmp/model-augmented",
    "/tmp/history-balanced",
    "/tmp/history-imbalanced",
    "/tmp/history-augmented",
    "/tmp/downloads",
    "/tmp/lab_archive",
]

def cleanup():
    """Remove todos os diretórios temporários do projeto."""
    print("=" * 70)
    print("Limpeza de Artefatos Temporários")
    print("=" * 70)

    removed_count = 0
    skipped_count = 0

    for dir_path in DIRS_TO_REMOVE:
        path = Path(dir_path)

        if path.exists() and path.is_dir():
            print(f" Removendo: {dir_path}")
            try:
                shutil.rmtree(path)
                removed_count += 1
            except Exception as e:
                print(f"Erro ao remover {dir_path}: {e}")
        else:
            print(f" Não encontrado (já limpo): {dir_path}")
            skipped_count += 1

    print()
    print("=" * 70)
    print("Limpeza concluída!")
    print("=" * 70)
    print(f"Resumo: {removed_count} removidos, {skipped_count} já limpos")


if __name__ == "__main__":
    cleanup()
