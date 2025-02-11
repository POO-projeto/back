# BACKEND - SIGAD

## 🛠 Pré-requisitos
Antes de rodar o projeto, certifique-se de ter instalado:

- [Git](#)
- [Python 3](#)
- [PostgreSQL](#)

## 🚫 Clonando o Repositório
Para obter o código-fonte em sua máquina, execute o seguinte comando:
```bash
git clone https://github.com/POO-projeto/back.git
```
Entre no repositório: 
```bash
cd back
```

## 🔧 Configuração do Ambiente

- **Para Windows:**
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
- **Para Linux:**

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

## 📦 Configuração do Banco de Dados

Antes de prosseguir, crie um banco de dados PostgreSQL com o nome **daily_db**:
```bash
psql -U postgres
```
```bash
create database daily_db;
```
Depois, configure o ambiente:
```bash
flask db upgrade
```
```bash
psql -U postgres -h localhost -d daily_db -f init_database.sql
```
```bash
pre-commit install
```

## 🚀 Rodando o Projeto
- **Para Windows:**
```bash
venv\Scripts\activate
```
```bash
flask run
```

**Para Linux:**
```bash
source venv/bin/activate
```
```bash
flask run
```

O servidor estará disponível em http://localhost:5000.