# Software ETL - Psychology School

> Pipeline ETL desenvolvido para integração, tratamento e centralização dos dados históricos de atendimentos de uma escola de Psicologia.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Supabase](https://img.shields.io/badge/Supabase-Backend-3ECF8E)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automation-2088FF)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-Dashboard-F9AB00)

---

## 📌 Sobre o projeto

Este projeto consiste em um **pipeline ETL automatizado** desenvolvido para integrar, tratar e centralizar os registros históricos de atendimentos de uma escola de Psicologia.

A solução foi desenvolvida a partir da necessidade de evitar a fragmentação dos dados em diferentes arquivos e permitir que o histórico permanecesse organizado em uma única estrutura, facilitando sua atualização e análise.

---

## 🎯 Objetivos

- Centralizar os dados históricos de atendimentos;
- Automatizar o processo de integração dos dados;
- Padronizar e tratar os registros antes do armazenamento;
- Evitar duplicidade de registros;
- Permitir atualizações de informações existentes;
- Disponibilizar os dados para análise em um dashboard;
- Reduzir a necessidade de execução manual do processo.

---

## 🏗️ Arquitetura

```text
┌──────────────────┐
│   Google Sheets  │
│   Fonte dos      │
│      dados       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│     Extract      │
│    gspread       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    Transform     │
│ Python + Pandas  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│       Load       │
│ Supabase /       │
│    PostgreSQL    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Looker Studio   │
│    Dashboard     │
└──────────────────┘

       ▲
       │
┌──────┴───────────┐
│  GitHub Actions  │
│    Automação     │
└──────────────────┘
