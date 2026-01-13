# MLOps Engineering Hub 🚀

Este repositório é um portfólio progressivo focado em **Engenharia de Machine Learning (MLOps)**. Aqui, documento a implementação de padrões, ferramentas e fluxos de trabalho necessários para levar modelos de ML do ambiente de experimentação para sistemas de produção robustos e confiáveis.

Diferente de repositórios de Data Science tradicionais, o foco aqui não é apenas a acurácia isolada do modelo, mas sim a **reprodutibilidade, confiabilidade, automação e monitoramento** de todo o ciclo de vida de ML (ML Lifecycle).

---

## 🎯 Pilares Técnicos
- **Pipelines de Produção:** Orquestração e automação de fluxos (TFX, Prefect/Airflow).
- **Data-Centric AI:** Qualidade de dados, validação de esquemas e detecção de *skew/drift* (TFDV).
- **Serving & Infra:** Deploy escalável com FastAPI, Docker, Kubernetes e TF Serving.
- **Governança & Linhagem:** Metadados de ML, versionamento de experimentos e análise de performance (TFMA, ML Metadata).
- **Confiabilidade:** Testes de carga (Locust), CI/CD para ML (CT - Continuous Training) e Fairness.

---

## 🚀 Roadmap de Projetos

Abaixo, a lista de implementações práticas. O repositório evolui de experimentos controlados para pipelines complexos de produção.

| Status | # | Projeto | Foco Principal |
| :--- | :---: | :--- | :--- |
| 🚀 **Ativo** | 2 | [Birds, Cats, and Dogs](./projects/birds-cats-dogs/README.md) | CNN, Data-centric AI, tratamento de desbalanceamento e Data Augmentation. |
| 📅 Planejado | 3 | YouTube Spam | Estratégias de rotulagem, performance e análise de erros. |
| 📅 Planejado | 4 | Earnings Predictor | Estatísticas de dados e detecção de anomalias com TFDV. |
| 📅 Planejado | 5 | Patient Readmission | Schema inference, validação avançada e Data Validation. |
| 📅 Planejado | 6 | Feature Engineering | Pipelines de pré-processamento escaláveis com TF Transform. |
| 📅 Planejado | 7 | TFX Pipeline | Implementação completa: ExampleGen, StatisticsGen e SchemaGen. |

---

## 🛠️ Stack Tecnológica
- **Linguagem:** Python (Ambientes isolados com Conda/WSL2)
- **Frameworks:** TensorFlow, Keras, Scikit-learn
- **MLOps:** TFX, TFDV, TFMA, ML Metadata
- **DevOps/Infra:** Docker, Kubernetes, FastAPI, GitHub Actions
- **Testes & Monitoramento:** Locust (Load Testing), Pytest

---

## 🧠 Por que este repositório existe?
O objetivo é demonstrar a aplicação prática dos conceitos de **Machine Learning Engineering for Production**. Cada projeto resolve um desafio real de engenharia, como:
- **Reprodutibilidade:** Como garantir que o modelo treinado hoje possa ser replicado exatamente igual amanhã?
- **Data Drift:** O que acontece quando os dados de produção mudam em relação ao treino?
- **Escalabilidade:** Como servir modelos com baixa latência e alta disponibilidade para milhares de usuários?
- **Monitoramento:** Como saber se o modelo ainda é válido após semanas em produção?

---

## ⭐ Contato
Desenvolvido por **Jefferson Hoy Valente**.  
Vamos trocar ideias no [LinkedIn](https://www.linkedin.com/in/jefferson-hoy-valente/)!

---
*Inspirado nas práticas de MLOps de Andrew Ng, Laurence Moroney e Robert Crowe.*
