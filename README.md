# 📦 PASTA LIMPA PARA DEPLOY NO VERCEL

## ✅ Esta é a pasta que vai para o Vercel:
📁 `vercel-deploy/` (apenas **36 KB** vs **150+ MB** da pasta original)

```
vercel-deploy/
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

## ❌ O que NÃO vai (fica na pasta original):
- **`.venv/`** - 150+ MB de ambiente virtual local
- **`backend/`** - Servidor Flask local (substituído pelas APIs)
- **`frontend/`** - Arquivos de desenvolvimento
- **Scripts .py** - Ferramentas locais de extração de dados
- **Documentação .md** - Guias e instruções
- **Scripts .bat/.sh** - Automatização local

## 🎯 RESUMO:
- **Pasta original**: `emissao_app (3)` - Para desenvolvimento local
- **Pasta deploy**: `vercel-deploy` - Só o essencial para produção

## 🚀 COMO FAZER O DEPLOY:
1. **Acesse**: https://vercel.com
2. **Arraste** apenas a pasta `vercel-deploy` 
3. **Configure** o nome do projeto
4. **Deploy** automático!

✨ **Pronto!** Muito mais leve e rápido para upload!