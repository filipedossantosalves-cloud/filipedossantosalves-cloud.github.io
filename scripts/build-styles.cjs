const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { createHash } = require('node:crypto');
const root = path.resolve(__dirname, '..');
const work = path.join(root, 'node_modules/.cache/viena');
fs.mkdirSync(work, { recursive: true });
const input = path.join(work, 'input.css');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
fs.writeFileSync(input, '@tailwind base;\n@tailwind components;\n@tailwind utilities;\n' + read('styles/fonts.css') + '\n' + read('styles/site.css'));
const result = spawnSync(process.execPath, [require.resolve('tailwindcss/lib/cli.js'), '--input', input, '--output', path.join(root,'assets/css/site.css'), '--config', path.join(root,'tailwind.config.cjs'), '--minify'], { cwd: root, stdio: 'inherit' });
if (result.status !== 0) process.exit(result.status || 1);
const hash = file => createHash('sha256').update(fs.readFileSync(path.join(root,file))).digest('hex').slice(0,12);
const versions = { 'assets/css/site.css':hash('assets/css/site.css'), 'assets/js/site.js':hash('assets/js/site.js') };
function updatePages(directory) {
  for (const file of fs.readdirSync(directory, { withFileTypes:true })) {
    const target = path.join(directory,file.name);
    if (file.isDirectory() && !['node_modules','.git','assets','styles','scripts','content'].includes(file.name)) updatePages(target);
    else if (file.name.endsWith('.html')) {
      let html = fs.readFileSync(target,'utf8');
      for (const [asset,version] of Object.entries(versions)) {
        html = html.replace(new RegExp('((?:href|src)="(?:\\.\\./)*'+asset.replaceAll('.','\\.')+')(?:\\?v=[^"\\s]+)?"','g'), '$1?v='+version+'"');
      }
      fs.writeFileSync(target,html);
    }
  }
}
updatePages(root);
console.log('Local CSS and JavaScript versioned by content.');
