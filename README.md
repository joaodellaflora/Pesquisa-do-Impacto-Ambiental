# 🌱 Pesquisa do Impacto Ambiental - Univates

## 📋 Sobre o Projeto
O propósito do questionário é coletar informações sobre o deslocamento para a Semana Acadêmica dos Cursos Técnicos da Univates. Os dados serão utilizados para análise do impacto ambiental dos transportes utilizados.

## 🚀 Aplicação Online
Formulário web moderno para coleta de dados sobre emissões de CO₂ dos deslocamentos dos participantes.

## 📁 Estrutura do Projeto
```
├── public/           ← Frontend (HTML + JS)
│   ├── index.html   ← Interface do usuário
│   └── index.js     ← JavaScript do formulário
├── api/             ← Funções serverless
│   ├── salvar-dados.py     ← Endpoint principal
│   ├── estatisticas.py     ← Estatísticas
│   ├── registros.py        ← Listar dados
│   └── fatores-emissao.py  ← Fatores de cálculo
├── vercel.json      ← Configuração do Vercel
└── requirements.txt ← Dependências Python
```

## 🌐 Tecnologias
- **Frontend**: HTML5, CSS3 (Tailwind), JavaScript
- **Backend**: Python com serverless functions
- **Banco**: SQLite
- **Deploy**: Vercel
- **Cálculos**: Fatores de emissão baseados no IPCC

## 📊 Funcionalidades
- ✅ Formulário responsivo e moderno
- ✅ Validação em tempo real
- ✅ Cálculo automático de emissões CO₂
- ✅ Armazenamento seguro de dados
- ✅ Múltiplos meios de transporte
- ✅ Conformidade LGPD

## 🎯 Como Usar
1. Acesse o formulário online
2. Preencha os dados de deslocamento
3. Envie o formulário
4. Os dados são processados automaticamente

## 🔗 Links
- **GitHub**: https://github.com/joaodellaflora/Pesquisa-do-Impacto-Ambiental
- **Deploy**: Em breve via Vercel

*Desenvolvido para a Semana Acadêmica dos Cursos Técnicos da Univates*