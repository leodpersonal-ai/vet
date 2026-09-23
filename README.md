# Atlas Veterinario

Biblioteca visual em espanhol com seis materiais de estudo para medicina veterinária. O projeto contém leitura digital, quiz interativo, exercícios SOAP e os seis PDFs para download.

## Rodar localmente

```bash
npm install
npm run dev
```

Para gerar a versão estática: `npm run build`.

## Conteúdo

- `src/content.json`: conteúdo estruturado dos seis materiais.
- `src/main.jsx` e `src/style.css`: biblioteca e leitores responsivos.
- `public/materiales/`: PDFs finais para download.
- `scripts/build_materials.py`: fonte editorial e gerador dos PDFs. Para recriar os PDFs, instale `reportlab` e execute `python3 scripts/build_materials.py`.

Os materiais são educativos. A prescrição veterinária deve considerar avaliação clínica, ficha técnica do produto e regras locais.
