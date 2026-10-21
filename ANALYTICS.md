# Medição de cliques no WhatsApp

O site prepara o evento `whatsapp_click` em todos os links com `data-whatsapp`. Cada evento envia `event_category`, `event_label`, `section_origin` e `destination`.

Para ativar o envio real, falta uma das identificações abaixo fornecida pelo proprietário:

- `[PREENCHER: ID de medição GA4, por exemplo G-XXXXXXXXXX]`; ou
- `[PREENCHER: ID do container GTM, por exemplo GTM-XXXXXXX]`.

Depois de receber o ID, inserir apenas o snippet oficial da plataforma escolhida no `<head>` e testar o evento no DebugView do GA4 ou no modo Preview do GTM. Não há ID inventado nem rastreamento externo ativo nesta versão local.
