# Viena Studio — Design & Presença Digital

Domínio canônico: https://www.vienastudio.com.br/

Versão estática completa, em português, com HTML, Tailwind CSS compilado, fontes locais e JavaScript sem dependências no navegador. O GitHub Pages publica a raiz da branch `main`. O arquivo `.nojekyll` mantém os arquivos estáticos sem processamento de Jekyll.

## Conteúdo

- Página inicial com serviços, investimento, portfólio, diferenciais, apresentação, método, FAQ e contato.
- Páginas de criação de sites, sites institucionais e tráfego pago.
- Dois projetos reais: Giftz 3D Studio e LL Para-brisas, com páginas próprias e links para os sites publicados.
- Quatro modelos demonstrativos preservados, identificados como modelos.
- Depoimento autorizado da Giftz, com mensagem original, data e atribuição.
- Robots, sitemap, metadados e dados estruturados apontando para o domínio canônico.

## Desenvolvimento

Requisitos: Node.js, npm e Python 3. Instale com `npm ci` e execute `npm run build`.

`index.html` é a fonte da página inicial e dos elementos compartilhados. `scripts/build-service-pages.py` gera as páginas secundárias e o sitemap. Edite `styles/site.css` e `styles/fonts.css`; `scripts/build-styles.cjs` compila o CSS e atualiza os hashes dos assets. `scripts/validate-site.py` confere HTML, links internos, metadados, dados estruturados, robots, sitemap, imagens, fontes e sintaxe JavaScript.

Os arquivos publicados ficam na raiz. A pasta `assets/` inclui todas as imagens e fontes necessárias. Os arquivos antigos que já existiam no repositório e não são utilizados pela nova página foram preservados; o histórico continua disponível.

## Publicação e validação

O repositório mantém um `CNAME` para compatibilidade com GitHub Pages; a hospedagem atual usa Cloudflare. Leia [DOMINIO-E-REDIRECIONAMENTOS.md](DOMINIO-E-REDIRECIONAMENTOS.md) antes de trocar a hospedagem ou configurar redirecionamentos. O envio do commit sozinho não comprova que o endereço público foi atualizado.

O código foi preparado a partir do commit `de23f7f2dd4c43a43f9b4f5e2d22b6f252e130d9` da versão Viena no Sites. Esta publicação não altera o acesso da cópia mantida no Sites. Não há credenciais ou chaves de API neste pacote.

A validação do código não equivale a um teste visual ou medição de Core Web Vitals. Após a publicação, conferir as seis páginas, carregamento de assets, navegação e contatos; depois medir desempenho e acompanhar indexação no Search Console. Nenhuma posição no Google ou citação por IA é garantida.
