"""Build gate for public-page integrity. Standard Python library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
import json, re, subprocess

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT
ORIGIN = 'https://www.vienastudio.com.br'
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.elements=[]; self.stack=[]; self.errors=[]
        self.source=path.read_text(encoding='utf-8'); self.feed(self.source)
        assert not self.errors and not self.stack, (path,self.errors,self.stack)
    def handle_starttag(self, tag, attributes):
        self.elements.append((tag,dict(attributes)))
        if tag not in VOID: self.stack.append(tag)
    def handle_startendtag(self, tag, attributes): self.elements.append((tag,dict(attributes)))
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1]!=tag: self.errors.append((self.getpos(),tag,self.stack[-3:]))
        else: self.stack.pop()
    def select(self, tag=None, **attrs):
        return [a for t,a in self.elements if (tag is None or t==tag) and all(a.get(k)==v for k,v in attrs.items())]
    @property
    def ids(self): return [a['id'] for t,a in self.elements if 'id' in a]

pages={path:Page(path) for path in [DIST/'index.html',*DIST.glob('*/index.html')]}
canonicals=set(); descriptions=set(); titles=set(); whatsapp=0; faq=0
for path,page in pages.items():
    assert not any(glyph in page.source for glyph in ('↗','↘','↑','↓')), (path, 'use SVG icons instead of text-arrow characters')
    assert len(page.ids)==len(set(page.ids)),(path,'duplicate IDs')
    assert len(page.select('h1'))==1,(path,'H1')
    assert page.select('html')[0]['lang']=='pt-BR'
    assert page.select('main')[0].get('tabindex')=='-1'
    title=re.search(r'<title>(.*?)</title>',page.source).group(1)
    description=page.select('meta',name='description')[0]['content']
    canonical=page.select('link',rel='canonical')[0]['href']
    assert title not in titles and description not in descriptions and canonical not in canonicals
    titles.add(title);descriptions.add(description);canonicals.add(canonical)
    assert canonical==page.select('meta',property='og:url')[0]['content']
    assert 'noindex' not in page.select('meta',name='robots')[0]['content']
    schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',page.source,re.S).group(1))
    graph_ids=[item['@id'] for item in schema['@graph']]
    assert len(graph_ids)==len(set(graph_ids))
    assert any(item['@type']=='WebPage' and item['url']==canonical for item in schema['@graph'])
    assert 'href="../#portfolio"' not in page.source, (path, 'portfolio must link to its dedicated page')
    for tag,attrs in page.elements:
        if tag=='script' and attrs.get('src'):
            assert not urlsplit(attrs['src']).scheme,(path,'third-party runtime')
        if tag=='img': assert all(key in attrs for key in ('width','height','alt','loading'))
        if 'data-whatsapp' in attrs:
            assert attrs.get('href','').startswith('https://wa.me/558192788355?text=')
            whatsapp+=1
        for key in ('href','src'):
            if not attrs.get(key): continue
            url=urlsplit(attrs[key])
            if url.scheme or url.netloc:
                if url.scheme+'://'+url.netloc!=ORIGIN: continue
                target=DIST / unquote(url.path.lstrip('/'))
            else: target=(path.parent/unquote(url.path)).resolve() if url.path else path
            if target.is_dir(): target=target/'index.html'
            assert target.exists(),(path,attrs[key],'missing file')
            if url.fragment and target in pages: assert url.fragment in pages[target].ids,(path,attrs[key],'missing anchor')
        for reference in ('aria-labelledby','aria-describedby','aria-controls'):
            if reference in attrs:
                for identifier in attrs[reference].split(): assert identifier in page.ids,(path,reference,identifier)
    faq+=len(page.select('details'))
    print(path.relative_to(DIST), 'OK')

home_schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', (DIST/'index.html').read_text(encoding='utf-8'), re.S).group(1))
assert any('ProfessionalService' in item.get('@type', []) for item in home_schema['@graph'])
assert any(item['@type']=='FAQPage' for item in home_schema['@graph'])
site_js=(DIST/'assets/js/site.js').read_text(encoding='utf-8')
assert "whatsapp_click" in site_js and "section_origin" in site_js

robot=RobotFileParser();robot.parse((DIST/'robots.txt').read_text(encoding='utf-8').splitlines())
assert robot.site_maps()==[ORIGIN+'/sitemap.xml']
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap=ET.parse(DIST/'sitemap.xml')
urls={e.text for e in sitemap.findall('.//s:loc',ns)}
assert urls==canonicals,(urls,canonicals)
for agent in ('Googlebot','bingbot','OAI-SearchBot'):
    assert all(robot.can_fetch(agent,url) for url in urls)

css=(DIST/'assets/css/site.css').read_text(encoding='utf-8')
assert '@font-face' in css and 'font-display:swap' in css
assert '9.5s' in css and 'prefers-reduced-motion' in css
for font in (DIST/'assets/fonts').glob('*.woff2'): assert font.read_bytes()[:4]==b'wOF2'
for url in re.findall(r'url\(([^)]+)\)',css):
    if url.startswith('data:'): continue
    assert (DIST/'assets/css'/url.strip('"\'')).resolve().exists(),url
ET.parse(DIST/'assets/favicon.svg')
subprocess.run(['node','--check',str(DIST/'assets/js/site.js')],check=True)
print(f'PASS: {len(pages)} pages, {len(urls)} sitemap URLs, {faq} FAQ answers, {whatsapp} contextual WhatsApp links.')
print('Checks cover source integrity; browser UX, public HTTP/indexing and Core Web Vitals require separate verification.')
