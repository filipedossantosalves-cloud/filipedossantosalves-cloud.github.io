# Domínio canônico e redirecionamentos

O endereço canônico escolhido para o site é `https://www.vienastudio.com.br/`.

O arquivo `CNAME` também contém apenas `www.vienastudio.com.br`. Canonical, Open Graph, Twitter, dados estruturados, `robots.txt`, `sitemap.xml` e links internos usam a mesma versão.

## DNS e hospedagem atual no Cloudflare

1. Mantenha `www.vienastudio.com.br` e `vienastudio.com.br` conectados ao mesmo Worker/Pages no Cloudflare.
2. Crie uma regra de redirecionamento permanente (301) de `vienastudio.com.br/*` para `https://www.vienastudio.com.br/$1`.
3. Confirme que o certificado HTTPS está ativo para os dois hostnames antes de ativar a regra.
4. Depois de publicar uma alteração, teste a página inicial, `/portfolio/`, `robots.txt` e `sitemap.xml` nos dois endereços. O endereço sem `www` deve terminar em `www`.

## Caso o GitHub Pages volte a hospedar o site

1. Em **Settings > Pages**, informe `www.vienastudio.com.br` como domínio personalizado e mantenha este arquivo `CNAME` na raiz publicada.
2. Crie no DNS um CNAME de `www` para `filipedossantosalves-cloud.github.io` (ou use o destino indicado pelo GitHub Pages).
3. Para o domínio raiz, use os registros A/AAAA indicados pelo GitHub Pages ou um redirecionamento no Cloudflare para `www`.
4. Ative HTTPS e aguarde a validação do domínio no GitHub Pages.

## Endereço antigo `filipedossantosalves-cloud.github.io`

Não é possível redirecionar esse hostname apenas com DNS do domínio Viena, porque ele pertence ao GitHub. O redirecionamento só pode acontecer se o GitHub Pages continuar ativo, receber `www.vienastudio.com.br` como domínio personalizado e estiver configurado para forçar HTTPS. Caso a hospedagem permaneça somente no Cloudflare, o endereço `github.io` deve ser tratado como uma cópia legada até que seja removido ou redirecionado por uma configuração feita no próprio GitHub.
