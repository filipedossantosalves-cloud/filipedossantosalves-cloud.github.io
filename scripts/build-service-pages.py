"""Generate static service pages from shared homepage navigation and branding.

Run after changing the shared header, footer, brand symbols or service copy.
No dependencies. Deploy the complete dist directory.
"""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT
BASE = 'https://filipedossantosalves-cloud.github.io/'
PHONE = '558192788355'
HOME = (DIST / 'index.html').read_text(encoding='utf-8')
TESTIMONIAL = json.loads((ROOT / 'content/giftz-testimonial.json').read_text(encoding='utf-8'))

def testimonial_html(prefix=''):
    t = TESTIMONIAL
    image = prefix + t['sourceImage']
    project_url = '#projeto' if prefix else 'projeto-giftz-3d-studio/'
    return f'''<figure class="testimonial">
      <figcaption class="testimonial-context"><p class="eyebrow label">Nas palavras do cliente</p><p class="testimonial-company">{escape(t['company'])}</p><p class="testimonial-meta"><strong>{escape(t['attribution'])}</strong><span>Trecho de mensagem pelo {escape(t['channel'])}<br><time datetime="{t['date']}">{escape(t['dateLabel'])}</time></span></p><a class="text-link" href="{project_url}">Conhecer o projeto <span aria-hidden="true">↗</span></a></figcaption>
      <div class="testimonial-content"><span class="testimonial-mark" aria-hidden="true">“</span><blockquote cite="{image}"><p>“{escape(t['quote'])}”</p></blockquote><a class="text-link testimonial-evidence" href="{image}" target="_blank" rel="noopener noreferrer">Ver mensagem original <span aria-hidden="true">↗</span></a></div>
    </figure>'''

HOME = re.sub(r'<!-- testimonial:giftz:start -->.*?<!-- testimonial:giftz:end -->', lambda m:'<!-- testimonial:giftz:start -->\n'+testimonial_html()+'\n        <!-- testimonial:giftz:end -->', HOME, flags=re.S)
(DIST / 'index.html').write_text(HOME, encoding='utf-8')

SERVICES = [
    {
        'path': 'criacao-de-sites-recife', 'key': 'sites', 'name': 'Landing pages',
        'title': 'Landing Page por R$ 997 em Recife | Viena Studio',
        'description': 'Criação de landing page por R$ 997: até 6 seções, design responsivo, WhatsApp e SEO básico. Confira o escopo. Viena Studio, Recife e atendimento online.',
        'badge': 'Criação de sites em Recife · Atendimento online',
        'heading': 'Uma página para sua oferta. <span class="hero-emphasis">Um caminho claro até o contato.</span>',
        'lead': 'A landing page reúne o essencial sobre um serviço, produto ou campanha em uma única página. Na Viena Studio, ela é desenhada para apresentar sua proposta, esclarecer dúvidas e facilitar o pedido de orçamento pelo WhatsApp.',
        'price': 'R$ 997', 'caption': 'Projeto de uma página · Até 6 seções · Confira as condições abaixo',
        'cta': 'Quero a landing page de R$ 997', 'message': 'a landing page de R$ 997 para minha empresa',
        'section_title': 'O essencial, bem resolvido.',
        'section_lead': 'Indicada para profissionais, empresas de serviços e campanhas com uma oferta principal. Cada seção tem uma função na apresentação do negócio.',
        'cards': [
            ('01 / Estrutura', 'Até 6 seções', 'Organizamos uma sequência com apresentação da oferta, benefícios, serviços, informações da empresa, dúvidas e contato. A composição é ajustada ao seu conteúdo e objetivo.'),
            ('02 / Experiência', 'Design e leitura no celular', 'Visual alinhado à sua identidade, adaptação a diferentes telas e botões de contato bem posicionados. Integrações com WhatsApp, links de redes sociais e mapa, quando aplicável.'),
            ('03 / Base técnica', 'Preparação para busca', 'Hierarquia de títulos, descrição da página, textos alternativos das imagens e estrutura semântica. A base ajuda buscadores a entender o conteúdo; não garante posição no Google.'),
        ],
        'scope_title': 'Incluído no pacote',
        'scope': [
            'Uma landing page com até 6 seções, design personalizado, versão responsiva e integrações essenciais de contato. Publicação técnica da página após aprovação.',
            'Registro de um domínio padrão disponível, não premium, por 12 meses. Por 6 meses após a entrega, pequenos ajustes de textos e imagens na estrutura contratada.',
        ],
        'limits_title': 'Condições antes de começar',
        'limits': [
            'Hospedagem e renovação do domínio são despesas separadas. Domínios premium, novas seções, novas funções, loja virtual, área de login e campanhas de anúncios não fazem parte do pacote.',
            'Você fornece as informações, identidade e materiais da empresa. A proposta confirma o conteúdo, prazo, forma de pagamento, domínio e eventuais custos recorrentes antes da contratação.',
        ],
        'faq': [
            ('Qual a diferença entre landing page e site institucional?', 'A landing page concentra uma oferta em uma página. Um site institucional organiza informações mais amplas sobre a empresa e seus serviços, podendo usar várias páginas. Se você precisa apresentar muitas áreas de atuação, o institucional pode ser mais adequado.'),
            ('O preço de R$ 997 é para o site inteiro?', 'Sim, para o projeto de uma landing page dentro do escopo de até 6 seções descrito nesta página. Hospedagem, renovação do domínio e serviços adicionais são separados. Não se trata de um preço para um site com várias páginas ou um sistema.'),
            ('Como funcionam os 6 meses de pequenos ajustes?', 'São alterações de textos e substituições de imagens na estrutura entregue, durante os 6 meses seguintes à publicação. Redesenho, novas seções, integrações e funcionalidades recebem orçamento próprio.'),
            ('Posso usar meu domínio atual?', 'Sim. Avaliamos a configuração do domínio existente e o destino da publicação. Você mantém o acesso à sua conta. O uso de um endereço já registrado e suas renovações são alinhados na proposta.'),
            ('Em quanto tempo a página fica pronta?', 'O prazo é informado na proposta depois de conferir conteúdo, materiais e integrações. Briefing, aprovação do visual, desenvolvimento e revisão são combinados antes do início.'),
            ('A landing page já inclui tráfego pago?', 'Não. A gestão de anúncios é um serviço separado, assim como a verba destinada ao Google ou à Meta. Podemos planejar a página para uma campanha e apresentar a proposta de gestão em conjunto.'),
        ],
        'closing': 'Sua oferta merece uma apresentação clara.',
        'closing_copy': 'Envie seu segmento, o serviço que deseja divulgar e as referências que você gosta. Vamos conferir se o pacote de R$ 997 atende ao seu projeto.',
    },
    {
        'path': 'sites-institucionais', 'key': 'institucional', 'name': 'Sites institucionais',
        'title': 'Criação de Sites Institucionais para Empresas | Viena Studio',
        'description': 'Sites institucionais sob medida para apresentar sua empresa, serviços e diferenciais. Design responsivo, SEO técnico e contato fácil. Recife e atendimento online.',
        'badge': 'Sites institucionais · Recife e online',
        'heading': 'Uma presença à altura <span class="hero-emphasis">da sua empresa.</span>',
        'lead': 'Um site institucional organiza o que seu cliente precisa saber: quem é a empresa, quais serviços oferece e como entrar em contato. A Viena Studio transforma essas informações em uma experiência visual coerente com sua marca.',
        'price': 'Sob proposta', 'caption': 'Estrutura, páginas e investimento definidos para o seu negócio',
        'cta': 'Pedir proposta de site institucional', 'message': 'um site institucional para minha empresa',
        'section_title': 'Clareza para quem chega. Identidade em cada página.',
        'section_lead': 'Indicado para empresas que precisam apresentar diferentes serviços, organizar conteúdo e oferecer um ponto de referência confiável na internet.',
        'cards': [
            ('01 / Arquitetura', 'Informação bem distribuída', 'Definimos quais páginas são necessárias e como elas se conectam: início, empresa, serviços, trabalhos e contato. O escopo considera a profundidade do conteúdo, sem páginas extras sem função.'),
            ('02 / Identidade', 'Design que representa a marca', 'Cores, tipografia, imagens e composição alinhadas ao posicionamento da empresa. Navegação compreensível e experiência responsiva para leitura no celular, tablet e computador.'),
            ('03 / Contato', 'Próximo passo evidente', 'Chamadas para orçamento nos pontos relevantes, links de WhatsApp, localização e informações de atendimento. Formulários ou outras integrações podem ser avaliados no escopo.'),
        ],
        'scope_title': 'O que definimos na proposta',
        'scope': [
            'Quantidade de páginas, organização dos serviços, conteúdo necessário, identidade visual e integrações. O projeto contempla a adaptação às telas e a revisão dos caminhos de navegação e contato.',
            'Títulos, descrições, estrutura semântica e organização das informações são planejados junto ao conteúdo. A preparação técnica para busca faz parte da construção, sem promessa de posições.',
        ],
        'limits_title': 'Um orçamento que considera sua operação',
        'limits': [
            'O investimento depende da quantidade de páginas e das funções necessárias. Domínio, hospedagem, manutenção, integrações e produção adicional de conteúdo são discriminados antes da contratação.',
            'A proposta também esclarece prazo, etapas de aprovação e materiais fornecidos pela empresa. Blog, painel de edição, loja virtual e área restrita exigem avaliação específica.',
        ],
        'faq': [
            ('Quantas páginas meu site precisa ter?', 'Depende do conteúdo. Uma empresa com vários serviços pode se beneficiar de páginas individuais para cada área. No diagnóstico, organizamos o mapa do site e definimos a quantidade na proposta.'),
            ('Quanto custa um site institucional?', 'O valor é personalizado conforme páginas, conteúdo, funcionalidades e integrações. Envie seu segmento, seus principais serviços e o que precisa apresentar para receber uma proposta com entregas, prazo e investimento.'),
            ('Vocês podem atualizar um site que já existe?', 'Sim. Primeiro avaliamos a plataforma, os acessos disponíveis, o conteúdo e o que precisa melhorar. A proposta pode considerar uma atualização da estrutura atual ou uma reformulação, conforme a necessidade.'),
            ('Preciso entregar textos e fotos?', 'Precisamos das informações reais da empresa e dos materiais que podem ser publicados. Na proposta, alinhamos o que você fornece e se será necessário contratar produção ou organização adicional de conteúdo.'),
            ('O site funciona no celular e pode aparecer no Google?', 'O projeto é responsivo e recebe preparação técnica para busca. Para rastreamento, a publicação precisa estar acessível publicamente. Indexação e posição dependem também de relevância, concorrência e dos próprios buscadores.'),
            ('Posso contratar anúncios depois?', 'Sim. O site institucional e a gestão de tráfego pago podem ser contratados separadamente. Quando houver uma campanha, avaliamos a página de destino e a forma de acompanhar os contatos.'),
        ],
        'closing': 'Vamos organizar a presença digital da sua empresa?',
        'closing_copy': 'Conte quais serviços oferece, se já possui um site e o que precisa melhorar. A partir daí, desenhamos uma proposta de estrutura, prazo e investimento.',
    },
    {
        'path': 'trafego-pago-recife', 'key': 'ads', 'name': 'Gestão de tráfego pago',
        'title': 'Gestão de Tráfego Pago em Recife: Google e Meta Ads | Viena Studio',
        'description': 'Gestão de Google Ads e Meta Ads em Recife, com atendimento online. Planejamento, acompanhamento e otimização de campanhas. Solicite uma proposta da Viena Studio.',
        'badge': 'Google Ads & Meta Ads · Recife e online',
        'heading': 'Sua oferta, diante <span class="hero-emphasis">das pessoas certas.</span>',
        'lead': 'Tráfego pago é a divulgação por anúncios em plataformas como Google, Instagram e Facebook. Na Viena Studio, a gestão conecta objetivo, público, mensagem e página de destino para buscar oportunidades de contato e orientar decisões com dados.',
        'price': 'Sob proposta', 'caption': 'Serviço de gestão · Verba de anúncios separada',
        'cta': 'Planejar os anúncios da minha empresa', 'message': 'gestão de tráfego pago para minha empresa',
        'section_title': 'Da estratégia ao acompanhamento.',
        'section_lead': 'Para empresas que querem divulgar serviços e ofertas com um objetivo definido. A seleção de canais depende do público, do orçamento e da estrutura de atendimento.',
        'cards': [
            ('01 / Planejamento', 'Objetivo antes da campanha', 'Avaliamos o negócio, a região de atendimento, a oferta e o caminho até o contato. Definimos se faz sentido captar buscas no Google, alcançar públicos na Meta ou combinar canais.'),
            ('02 / Implementação', 'Campanhas e direcionamento', 'Organização da conta, segmentação, configuração dos anúncios e definição da página de destino ou WhatsApp. Criativos, acessos e mensuração são alinhados no escopo antes de iniciar.'),
            ('03 / Evolução', 'Acompanhar para ajustar', 'Análise dos indicadores disponíveis, acompanhamento de investimento e testes de mensagens, públicos ou formatos. As otimizações seguem os dados e as prioridades combinadas.'),
        ],
        'scope_title': 'O que a gestão considera',
        'scope': [
            'Planejamento, configuração, acompanhamento e otimização das campanhas contratadas. Canais, quantidade de campanhas, criativos e formato de acompanhamento são definidos na proposta.',
            'Indicadores como cliques, custo por clique e contatos ou conversões são acompanhados conforme a mensuração disponível. O retorno do atendimento da empresa ajuda a avaliar a qualidade das oportunidades.',
        ],
        'limits_title': 'Gestão e mídia são investimentos diferentes',
        'limits': [
            'O serviço de gestão remunera o planejamento e o acompanhamento. A verba de mídia é destinada às plataformas para veicular os anúncios e não está incluída no valor da gestão.',
            'Resultados variam com oferta, mercado, orçamento, página de destino e atendimento. Não há garantia de vendas, faturamento ou retorno específico. Sites e produção adicional de materiais recebem escopo próprio.',
        ],
        'faq': [
            ('Qual a diferença entre Google Ads e Meta Ads?', 'O Google permite alcançar buscas relacionadas à necessidade do cliente, além de outros formatos. A Meta oferece anúncios em canais como Instagram e Facebook. Escolhemos os canais a partir do objetivo e do comportamento do público.'),
            ('Quanto preciso investir em anúncios?', 'O orçamento é definido conforme objetivo, região, concorrência e capacidade de atendimento. Primeiro avaliamos o cenário para propor um valor de mídia e uma gestão compatíveis, sem prometer resultados a partir de um investimento fixo.'),
            ('Preciso ter um site para anunciar?', 'Depende da campanha. Algumas estratégias direcionam para uma página; outras, para uma conversa no WhatsApp. Avaliamos se a estrutura disponível apresenta a oferta com clareza e permite receber os contatos.'),
            ('Posso contratar somente a gestão?', 'Sim. Podemos avaliar seu site ou destino atual e estruturar a gestão de anúncios sem contratar a criação de um novo site. Ajustes necessários na página são apresentados separadamente.'),
            ('A gestão inclui a verba e os criativos?', 'A verba dos anúncios é separada do serviço de gestão. A quantidade e a produção de criativos, assim como vídeos ou fotografias adicionais, são especificadas na proposta para evitar dúvidas sobre o escopo.'),
            ('Como acompanho os resultados?', 'Antes do início, alinhamos os indicadores, a forma de acompanhamento e a periodicidade de apresentação. Quando possível, relacionamos os dados das plataformas aos contatos recebidos e ao retorno do atendimento comercial.'),
        ],
        'closing': 'Antes de anunciar, vamos entender seu negócio.',
        'closing_copy': 'Envie seu segmento, sua região de atendimento e o objetivo da campanha. Conte também se já anuncia e se possui um site ou WhatsApp comercial.',
    },
]

def icon(name='arrow-up-right'):
    return f'<svg class="icon" aria-hidden="true"><use href="#{name}"/></svg>'

def contact(data, label=None):
    message = 'Olá! Quero conversar com a Viena Studio sobre ' + data['message'] + '.'
    return f'<a class="button button-primary" href="https://wa.me/{PHONE}?text={quote(message)}" data-whatsapp data-service="{escape(data["message"],quote=True)}">{icon("whatsapp")}{escape(label or data["cta"])}{icon()}</a>'

def shared_links(html):
    html = re.sub(r'(<a\b[^>]*?href=")#([^\"]*)"', r'\1../#\2"', html)
    for data in SERVICES:
        html = html.replace(f'href="{data["path"]}/"', f'href="../{data["path"]}/"')
    return html

head = HOME[:HOME.index('</head>')]
symbols_and_header = HOME[HOME.index('<body>'):HOME.index('  <main id="conteudo"')]
symbols_and_header = shared_links(symbols_and_header).replace('href="../#conteudo"','href="#conteudo"')
footer = shared_links(HOME[HOME.index('  <footer class="site-footer">'):])
footer = footer.replace('src="assets/', 'src="../assets/')
    # The footer's "top" link stays on the current page; brand links return home.
footer = footer.replace('class="back-top" href="../#inicio"','class="back-top" href="#inicio"')
footer = footer.replace('class="quick-top" href="../#inicio"','class="quick-top" href="#inicio"')
footer = footer.replace('<nav class="quick-navigation" aria-label="Navegação rápida"><a class="quick-top"', '<nav class="quick-navigation" aria-label="Navegação rápida"><a class="quick-home" href="../#inicio">Página inicial</a><a class="quick-top"')
home_graph = json.loads(re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', HOME, re.S).group(1))['@graph']

for data in SERVICES:
    canonical = BASE + data['path'] + '/'
    page_head = re.sub(r'<title>.*?</title>', f'<title>{escape(data["title"])}</title>', head)
    for name, value in [('description',data['description']),('twitter:title',data['title']),('twitter:description',data['description'])]:
        page_head = re.sub(r'(<meta name="'+re.escape(name)+r'" content=")[^"]*(">)', lambda m:m[1]+escape(value,quote=True)+m[2], page_head)
    for name, value in [('og:title',data['title']),('og:description',data['description']),('og:url',canonical)]:
        page_head = re.sub(r'(<meta property="'+re.escape(name)+r'" content=")[^"]*(">)',lambda m:m[1]+escape(value,quote=True)+m[2],page_head)
    page_head = re.sub(r'<link rel="canonical" href="[^"]+">',f'<link rel="canonical" href="{canonical}">',page_head)
    page_head = page_head.replace('href="assets/', 'href="../assets/')
    graph = [item for item in home_graph if item['@type'] in ('Organization','WebSite','Person') or item['@id']==BASE+'#service-'+data['key']]
    graph.extend([
        {'@type':'WebPage','@id':canonical+'#webpage','url':canonical,'name':data['title'],'description':data['description'],'inLanguage':'pt-BR','isPartOf':{'@id':BASE+'#website'},'mainEntity':{'@id':BASE+'#service-'+data['key']},'breadcrumb':{'@id':canonical+'#breadcrumb'}},
        {'@type':'BreadcrumbList','@id':canonical+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'Viena Studio','item':BASE},{'@type':'ListItem','position':2,'name':data['name'],'item':canonical}]},
    ])
    page_head = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">\n'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,indent=2)+'\n</script>',page_head,flags=re.S)
    cards = ''.join(f'<article class="detail-card"><p class="label">{escape(tag)}</p><h3>{escape(title)}</h3><p>{escape(copy)}</p></article>' for tag,title,copy in data['cards'])
    faq = ''.join(f'<details class="faq-item"{" open" if n==0 else ""}><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for n,(q,a) in enumerate(data['faq']))
    paragraphs = lambda texts: ''.join('<p>'+escape(text)+'</p>' for text in texts)
    related = ''.join(f'<a class="text-link" href="../{other["path"]}/">{escape(other["name"])} {icon()}</a>' for other in SERVICES if other!=data)
    main = f'''
  <main id="conteudo" tabindex="-1">
    <section class="hero service-hero" id="inicio" aria-labelledby="hero-title">
      <div class="hero-grid" aria-hidden="true"></div><svg class="hero-mark" aria-hidden="true"><use href="#viena-mark"/></svg>
      <div class="shell"><nav class="breadcrumb" aria-label="Localização"><a href="../">Viena Studio</a><span aria-hidden="true">/</span><span aria-current="page">{escape(data['name'])}</span></nav>
        <div class="hero-content"><p class="eyebrow label hero-badge">{escape(data['badge'])}</p><h1 class="display" id="hero-title">{data['heading']}</h1><p class="hero-lead">{escape(data['lead'])}</p><p class="service-price">{escape(data['price'])}</p><p class="service-price-caption">{escape(data['caption'])}</p><div class="hero-actions">{contact(data)}<a href="#entregas" class="button button-secondary">Conhecer as entregas {icon('arrow-down')}</a></div></div>
      </div>
    </section>
    <section class="section" id="entregas" aria-labelledby="deliverables-title"><div class="shell"><div class="section-heading"><div><p class="eyebrow label">Escopo &amp; possibilidades</p><h2 class="display section-title" id="deliverables-title">{escape(data['section_title'])}</h2></div><p>{escape(data['section_lead'])}</p></div><div class="detail-grid">{cards}</div>
      <div class="scope-panel"><div><h3>{escape(data['scope_title'])}</h3>{paragraphs(data['scope'])}</div><div><h3>{escape(data['limits_title'])}</h3>{paragraphs(data['limits'])}</div></div>
      <aside class="portfolio-next"><div><h3>Conheça o trabalho antes de decidir.</h3><p>Conheça os projetos Giftz 3D Studio e LL Para-brisas, além dos modelos demonstrativos. Veja também como Filipe conduz os projetos da Viena.</p></div><a class="button button-secondary" href="../#portfolio">Explorar portfólio {icon()}</a></aside>
    </div></section>
    <section class="section" id="duvidas" aria-labelledby="faq-title"><div class="shell faq-layout"><div class="faq-intro"><p class="eyebrow label">Dúvidas de contratação</p><h2 class="display section-title" id="faq-title">Informação clara.<br><span class="gold">Decisão tranquila.</span></h2><p>Saiba o que considerar antes de contratar {escape(data['name'].lower())}.</p><a class="text-link" href="../#metodo">Conheça nosso método {icon()}</a></div><div class="faq-list">{faq}</div></div></section>
    <section class="contact-section" id="contato" aria-labelledby="contact-title"><div class="shell"><div class="contact-frame"><svg class="contact-mark" aria-hidden="true"><use href="#viena-mark"/></svg><p class="label">Viena Studio · Design &amp; presença digital</p><h2 class="display contact-title" id="contact-title">{escape(data['closing'])}</h2><p class="contact-copy">{escape(data['closing_copy'])}</p>{contact(data)}<p class="contact-caption">Fale diretamente com Filipe · Recife–PE e atendimento online</p></div><nav class="service-related" aria-label="Outras soluções">{related}</nav></div></section>
  </main>
'''
    directory = DIST / data['path']
    directory.mkdir(exist_ok=True)
    (directory / 'index.html').write_text(page_head+'</head>\n'+symbols_and_header+main+footer, encoding='utf-8')

case_path = 'projeto-giftz-3d-studio/'
case_url = BASE + case_path
case_title = 'Projeto Giftz 3D Studio: Catálogo e Contato | Viena Studio'
case_description = 'Conheça a estrutura do projeto Giftz 3D Studio: catálogo de colecionáveis, galeria, processo de encomenda e contato pelo WhatsApp. Portfólio Viena Studio.'
case_head = head.replace('href="assets/', 'href="../assets/')
case_head = re.sub(r'<title>.*?</title>', '<title>'+case_title+'</title>', case_head)
for kind, attr, value in [('name','description',case_description),('name','twitter:title',case_title),('name','twitter:description',case_description),('property','og:title',case_title),('property','og:description',case_description),('property','og:url',case_url)]:
    case_head=re.sub(r'(<meta '+kind+'="'+attr+r'" content=")[^"]*(">)',lambda m:m[1]+escape(value,quote=True)+m[2],case_head)
case_head=re.sub(r'<link rel="canonical" href="[^"]+">','<link rel="canonical" href="'+case_url+'">',case_head)
case_graph=[item for item in home_graph if item['@type'] in ('Organization','WebSite','Person')]
case_graph.extend([
    {'@type':'WebPage','@id':case_url+'#webpage','url':case_url,'name':case_title,'description':case_description,'inLanguage':'pt-BR','isPartOf':{'@id':BASE+'#website'},'breadcrumb':{'@id':case_url+'#breadcrumb'},'mainEntity':{'@id':case_url+'#project'}},
    {'@type':'CreativeWork','@id':case_url+'#project','name':'Giftz 3D Studio — catálogo comercial','description':'Apresentação de linhas de colecionáveis, galeria, processo de encomenda e contato.','url':'https://giftz3dstudio.com.br/','creator':{'@id':BASE+'#organization'},'image':BASE+'assets/portfolio/giftz.png'},
    {'@type':'BreadcrumbList','@id':case_url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'Viena Studio','item':BASE},{'@type':'ListItem','position':2,'name':'Giftz 3D Studio','item':case_url}]}
])
case_head=re.sub(r'<script type="application/ld\+json">.*?</script>','<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':case_graph},ensure_ascii=False,indent=2)+'</script>',case_head,flags=re.S)
case_main='''
  <main id="conteudo" tabindex="-1">
    <section class="hero service-hero" id="inicio" aria-labelledby="hero-title"><div class="hero-grid" aria-hidden="true"></div><svg class="hero-mark" aria-hidden="true"><use href="#viena-mark"/></svg><div class="shell"><nav class="breadcrumb" aria-label="Localização"><a href="../">Viena Studio</a><span aria-hidden="true">/</span><span aria-current="page">Giftz 3D Studio</span></nav><div class="hero-content"><p class="eyebrow label hero-badge">Portfólio · Projeto publicado</p><h1 class="display" id="hero-title">Giftz 3D Studio.<br><span class="hero-emphasis">Uma vitrine para ideias em 3D.</span></h1><p class="hero-lead">Um catálogo de colecionáveis personalizados que apresenta as opções, mostra trabalhos e orienta o visitante até a conversa sobre sua encomenda.</p><div class="hero-actions"><a class="button button-primary" href="https://giftz3dstudio.com.br/" target="_blank" rel="noopener noreferrer">Visitar o site da Giftz <span aria-hidden="true">↗</span></a><a class="button button-secondary" href="#projeto">Conhecer a estrutura <span aria-hidden="true">↓</span></a></div></div></div></section>
    <section class="section" id="projeto" aria-labelledby="project-title"><div class="shell case-layout"><figure class="case-preview"><img src="../assets/portfolio/giftz.png" width="1221" height="6144" loading="lazy" decoding="async" alt="Prévia do projeto Giftz 3D Studio no portfólio da Viena"><figcaption>Prévia preservada do projeto.<br><a href="../assets/portfolio/giftz.png" target="_blank" rel="noopener noreferrer">Abrir a imagem completa <span aria-hidden="true">↗</span></a></figcaption></figure><div class="case-story"><div><p class="eyebrow label">O projeto em contexto</p><h2 class="display" id="project-title">Do produto personalizado<br><span class="gold">ao pedido de orçamento.</span></h2><p>A Giftz produz miniaturas e colecionáveis em Recife, com encomendas feitas a partir de fotos e referências. O site reúne catálogo, exemplos e orientações para quem quer transformar uma ideia em uma peça.</p></div><dl class="case-overview"><div><dt>Segmento</dt><dd>Impressão 3D e colecionáveis personalizados</dd></div><div><dt>Tipo de presença</dt><dd>Catálogo comercial com contato pelo WhatsApp</dd></div><div><dt>Conteúdos centrais</dt><dd>Coleções, trabalhos, processo e dúvidas</dd></div></dl><div><h2 class="display">O que a estrutura resolve.</h2><p>As linhas de produtos ajudam a comparar possibilidades. A galeria apresenta peças realizadas. A explicação do processo orienta o envio de referências, e as dúvidas frequentes esclarecem a encomenda antes do contato.</p><p>É uma referência de como organizar uma oferta visual e personalizada. Para sua empresa, o ponto de partida será o seu público, seu conteúdo e seu processo de atendimento.</p></div><a class="text-link" href="../#portfolio">Ver os outros modelos do portfólio <span aria-hidden="true">↗</span></a></div></div></section>
    <section class="contact-section" id="contato" aria-labelledby="contact-title"><div class="shell"><div class="contact-frame"><svg class="contact-mark" aria-hidden="true"><use href="#viena-mark"/></svg><p class="label">Seu projeto, com sua identidade</p><h2 class="display contact-title" id="contact-title">Como sua empresa pode<br><span class="gold">se apresentar melhor?</span></h2><p class="contact-copy">Conte o que você oferece e o que seu cliente precisa entender antes de pedir um orçamento. Vamos organizar esse caminho.</p><a class="button button-primary" href="https://wa.me/558192788355?text=Ol%C3%A1!%20Vi%20o%20projeto%20Giftz%20e%20quero%20um%20site%20para%20minha%20empresa." data-whatsapp data-service="um site para minha empresa, com referência no projeto Giftz">Conversar sobre meu site <span aria-hidden="true">↗</span></a><p class="contact-caption">Atendimento direto com Filipe · Recife–PE e online</p></div><nav class="service-related" aria-label="Soluções relacionadas"><a class="text-link" href="../criacao-de-sites-recife/">Site de uma página por R$ 997 <span aria-hidden="true">↗</span></a><a class="text-link" href="../sites-institucionais/">Sites institucionais <span aria-hidden="true">↗</span></a></nav></div></section>
  </main>
'''
case_main = case_main.replace('    <section class="contact-section"', '<div class="shell case-feedback" id="depoimento">'+testimonial_html('../')+'</div>\n    <section class="contact-section"',1)
(DIST/case_path).mkdir(exist_ok=True)
(DIST/case_path/'index.html').write_text(case_head+'</head>\n'+symbols_and_header+case_main+footer, encoding='utf-8')
ll_path = 'projeto-ll-parabrisas/'
ll_url = BASE + ll_path
ll_title = 'Projeto LL Para-brisas: Site Empresarial em Recife | Viena Studio'
ll_description = 'Conheça o site da LL Para-brisas, em Recife: apresentação de serviços, categorias de veículos, dúvidas, localização e contato. Projeto da Viena Studio.'
ll_head = head.replace('href="assets/', 'href="../assets/')
ll_head = re.sub(r'<title>.*?</title>', '<title>'+ll_title+'</title>', ll_head)
for kind, attr, value in [('name','description',ll_description),('name','twitter:title',ll_title),('name','twitter:description',ll_description),('property','og:title',ll_title),('property','og:description',ll_description),('property','og:url',ll_url),('property','og:image',BASE+'assets/portfolio/ll-parabrisas-fachada.webp'),('name','twitter:image',BASE+'assets/portfolio/ll-parabrisas-fachada.webp'),('property','og:image:alt','Fachada da LL Para-brisas em Recife'),('name','twitter:image:alt','Fachada da LL Para-brisas em Recife')]:
    ll_head=re.sub(r'(<meta '+kind+'="'+attr+r'" content=")[^"]*(">)',lambda m:m[1]+escape(value,quote=True)+m[2],ll_head)
ll_head=re.sub(r'<link rel="canonical" href="[^"]+">','<link rel="canonical" href="'+ll_url+'">',ll_head)
ll_graph=[item for item in home_graph if item['@type'] in ('Organization','WebSite','Person')]
ll_graph.extend([
    {'@type':'WebPage','@id':ll_url+'#webpage','url':ll_url,'name':ll_title,'description':ll_description,'inLanguage':'pt-BR','isPartOf':{'@id':BASE+'#website'},'breadcrumb':{'@id':ll_url+'#breadcrumb'},'mainEntity':{'@id':ll_url+'#project'}},
    {'@type':'CreativeWork','@id':ll_url+'#project','name':'LL Para-brisas — site empresarial','description':'Site de serviços automotivos em Recife com categorias de veículos, dúvidas frequentes, localização e contato pelo WhatsApp.','url':'https://www.llparabrisas.com.br/','creator':{'@id':BASE+'#organization'},'image':BASE+'assets/portfolio/ll-parabrisas-fachada.webp'},
    {'@type':'BreadcrumbList','@id':ll_url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'Viena Studio','item':BASE},{'@type':'ListItem','position':2,'name':'LL Para-brisas','item':ll_url}]}
])
ll_head=re.sub(r'<script type="application/ld\+json">.*?</script>','<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':ll_graph},ensure_ascii=False,indent=2)+'</script>',ll_head,flags=re.S)
ll_main=f'''
  <main id="conteudo" tabindex="-1">
    <section class="hero service-hero" id="inicio" aria-labelledby="hero-title">
      <div class="hero-grid" aria-hidden="true"></div><svg class="hero-mark" aria-hidden="true"><use href="#viena-mark"/></svg>
      <div class="shell"><nav class="breadcrumb" aria-label="Localização"><a href="../">Viena Studio</a><span aria-hidden="true">/</span><span aria-current="page">LL Para-brisas</span></nav>
        <div class="hero-content"><p class="eyebrow label hero-badge">Portfólio · Projeto publicado · Recife</p>
          <h1 class="display" id="hero-title">LL Para-brisas.<br><span class="hero-emphasis">Do serviço local ao contato digital.</span></h1>
          <p class="hero-lead">Um site empresarial que reúne serviços, informações de atendimento e orientações para quem precisa trocar o para-brisa e consultar a disponibilidade da peça.</p>
          <div class="hero-actions"><a class="button button-primary" href="https://www.llparabrisas.com.br/" target="_blank" rel="noopener noreferrer">Visitar o site da LL Para-brisas {icon()}</a><a class="button button-secondary" href="#projeto">Conhecer a estrutura {icon('arrow-down')}</a></div>
        </div>
      </div>
    </section>
    <section class="section" id="projeto" aria-labelledby="project-title"><div class="shell case-layout">
      <figure class="case-preview case-photo"><img src="../assets/portfolio/ll-parabrisas-fachada.webp" width="1086" height="1448" loading="lazy" decoding="async" alt="Fachada e área de atendimento da LL Para-brisas em Recife"><figcaption>Imagem da empresa utilizada no projeto.<br><a href="https://www.llparabrisas.com.br/" target="_blank" rel="noopener noreferrer">Conhecer o site completo {icon()}</a></figcaption></figure>
      <div class="case-story"><div><p class="eyebrow label">O projeto em contexto</p><h2 class="display" id="project-title">Informações organizadas.<br><span class="gold">Próximo passo evidente.</span></h2><p>A LL Para-brisas atua com troca e instalação de para-brisas em Recife. A página apresenta o atendimento para carros nacionais, importados, elétricos, vans e caminhões, com orientação para consultar a peça adequada.</p></div>
        <dl class="case-overview"><div><dt>Segmento</dt><dd>Serviços automotivos · Para-brisas</dd></div><div><dt>Tipo de presença</dt><dd>Site empresarial de uma página</dd></div><div><dt>Conteúdos centrais</dt><dd>Serviços, veículos atendidos, diferenciais, dúvidas e localização</dd></div><div><dt>Contato</dt><dd>Consulta de preço e disponibilidade pelo WhatsApp</dd></div></dl>
        <div><h2 class="display">Um percurso até o orçamento.</h2><p>O visitante encontra as categorias de veículos, os cuidados apresentados pela empresa e respostas às dúvidas de atendimento. Os botões de contato orientam o envio de marca, modelo e ano, enquanto a seção de localização oferece acesso à rota no mapa.</p><p>Essa organização é uma referência para negócios locais: apresentar o serviço, esclarecer informações e oferecer um caminho direto para conversar com a equipe.</p></div>
        <a class="text-link" href="../projeto-giftz-3d-studio/">Conhecer também o projeto Giftz {icon()}</a>
      </div>
    </div></section>
    <section class="section" aria-labelledby="structure-title"><div class="shell">
      <div class="section-heading"><div><p class="eyebrow label">A estrutura do site</p><h2 class="display section-title" id="structure-title">Três pontos de atenção.</h2></div><p>Conteúdo que acompanha as perguntas de quem procura um serviço automotivo.</p></div>
      <div class="detail-grid">
        <article class="detail-card"><p class="eyebrow label">01 / Apresentação</p><h3>O serviço e a empresa</h3><p>A abertura identifica a atividade e a região de atendimento, acompanhada por uma imagem da empresa. As seções seguintes detalham os diferenciais apresentados pela LL.</p></article>
        <article class="detail-card"><p class="eyebrow label">02 / Informação</p><h3>Veículos e dúvidas</h3><p>As categorias de veículos e as perguntas frequentes ajudam a entender o atendimento e quais informações levar para a consulta de disponibilidade.</p></article>
        <article class="detail-card"><p class="eyebrow label">03 / Contato</p><h3>WhatsApp e localização</h3><p>Chamadas distribuídas pela página levam à conversa com a equipe. A localização reúne as informações para planejar a visita e abrir a rota no mapa.</p></article>
      </div>
    </div></section>
    <section class="contact-section" id="contato" aria-labelledby="contact-title"><div class="shell"><div class="contact-frame">
      <svg class="contact-mark" aria-hidden="true"><use href="#viena-mark"/></svg><p class="label">Seu negócio local, bem apresentado</p><h2 class="display contact-title" id="contact-title">Seu cliente encontra<br><span class="gold">o que precisa saber?</span></h2><p class="contact-copy">Conte o seu segmento, sua região de atendimento e quais serviços quer divulgar. Vamos planejar uma apresentação alinhada à sua empresa.</p>
      {contact({'message':'um site para minha empresa, com referência no projeto LL Para-brisas','cta':'Conversar sobre meu site'})}
      <p class="contact-caption">Atendimento direto com Filipe · Recife–PE e online</p></div>
      <nav class="service-related" aria-label="Soluções e projetos relacionados"><a class="text-link" href="../criacao-de-sites-recife/">Site de uma página por R$ 997 {icon()}</a><a class="text-link" href="../sites-institucionais/">Sites institucionais {icon()}</a><a class="text-link" href="../#portfolio">Voltar ao portfólio {icon()}</a></nav>
    </div></section>
  </main>
'''
(DIST/ll_path).mkdir(exist_ok=True)
(DIST/ll_path/'index.html').write_text(ll_head+'</head>\n'+symbols_and_header+ll_main+footer, encoding='utf-8')
urls = [BASE] + [BASE+s['path']+'/' for s in SERVICES] + [case_url,ll_url]
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{url}</loc><lastmod>2026-10-15</lastmod></url>\n' for url in urls)+'</urlset>\n', encoding='utf-8')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'sitemap.xml\n', encoding='utf-8')
print(f'Generated {len(SERVICES)} service pages, Giftz and LL Para-brisas projects, robots.txt and sitemap.')
