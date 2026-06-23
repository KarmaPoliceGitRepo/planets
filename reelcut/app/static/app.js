// ReelCut front-end — vanilla JS, no build step.
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const esc = s => (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const mmss = t => { t=Math.max(0,Math.floor(t)); return String(t/60|0).padStart(2,'0')+':'+String(t%60).padStart(2,'0'); };
let PID = null, PROJECT = null, TRANSITIONS = [];

// ---------- step navigation ----------
function go(step){
  $$('.panel').forEach(p=>p.classList.toggle('on', p.dataset.panel==step));
  $$('#steps span').forEach(s=>s.classList.toggle('on', s.dataset.step==step));
  if(step==2) loadProject().then(renderSeq);
  if(step==3) loadSequence();
}
$$('[data-go]').forEach(b=>b.onclick=()=>go(b.dataset.go));
$$('#steps span').forEach(s=>s.onclick=()=>{ if(PID||s.dataset.step==0) go(s.dataset.step); });

// ---------- API ----------
const api = (p,o={}) => fetch(p,o).then(r=>r.json());
async function loadProject(){ PROJECT = await api('/api/project?id='+PID); return PROJECT; }
async function saveProject(){ await api('/api/save',{method:'POST',headers:{'Content-Type':'application/json'},
  body:JSON.stringify({id:PID,project:PROJECT})}); }

// ---------- upload ----------
const drop=$('#drop');
['dragover','dragenter'].forEach(e=>drop.addEventListener(e,ev=>{ev.preventDefault();drop.classList.add('hover');}));
['dragleave','drop'].forEach(e=>drop.addEventListener(e,ev=>{ev.preventDefault();drop.classList.remove('hover');}));
drop.addEventListener('drop',ev=>{ if(ev.dataTransfer.files[0]) upload(ev.dataTransfer.files[0]); });
$('#file').addEventListener('change',e=>{ if(e.target.files[0]) upload(e.target.files[0]); });

async function upload(file){
  $('#uplog').textContent = `Copying ${file.name} (${(file.size/1048576).toFixed(1)} MB)…`;
  const r = await fetch('/api/upload',{method:'POST',headers:{'X-Filename':file.name},body:file});
  const d = await r.json();
  if(d.error){ $('#uplog').textContent='⚠️ '+d.error; return; }
  PID = d.id;
  $('#uplog').innerHTML = `✅ Ready: ${esc(file.name)} — ${d.info.has_video?d.info.width+'×'+d.info.height:'audio'} · ${mmss(d.info.duration)}`;
  setTimeout(()=>go(1),500);
}

async function loadRecent(){
  const d = await api('/api/projects');
  if(!d.projects.length){ $('#recent').style.display='none'; return; }
  $('#recent').innerHTML = '<h2>Recent projects</h2>' + d.projects.map(p=>
    `<div class="row"><span class="grow">${esc(p.name)} <span class="muted small">(${p.engine||'…'})</span></span>
     <button class="ghost" onclick="openProject('${p.id}')">Open</button></div>`).join('');
}
window.openProject = id => { PID=id; go(1); loadProject().then(renderSegs); };

// ---------- step 1: segments ----------
$('#btn-segment').onclick = async ()=>{
  if(!PID) return;
  await api('/api/segment',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,model:$('#model').value})});
  poll(async ()=>{ await loadProject(); renderSegs(); });
};
function renderSegs(){
  $('#engineNote').textContent = PROJECT.engine ? `Split engine: ${PROJECT.engine}` : '';
  const box=$('#segList'); box.innerHTML='';
  (PROJECT.segments||[]).forEach((seg,si)=>{
    const el=document.createElement('div'); el.className='seg';
    el.innerHTML=`<div class="seghead">
      <input type="checkbox" ${seg.keep!==false?'checked':''} data-seg="${seg.id}">
      <b>${esc(seg.title||seg.id)}</b> <span class="tag">${esc(seg.tag||'topic')}</span>
      <span class="time">${mmss(seg.start)}–${mmss(seg.end)}</span></div>` +
      (seg.subsections||[]).map(s=>`<div class="subrow ${(seg.keep===false||s.keep===false)?'off':''}">
        <input type="checkbox" ${s.keep!==false?'checked':''} data-sub="${s.id}">
        <div><span class="muted small">${mmss(s.start)}–${mmss(s.end)} · <b>${esc(s.tag||'')}</b></span><br>${esc((s.text||'').slice(0,160))}</div></div>`).join('');
    box.appendChild(el);
  });
  box.querySelectorAll('[data-seg]').forEach(c=>c.onchange=()=>toggle(c.dataset.seg,c.checked));
  box.querySelectorAll('[data-sub]').forEach(c=>c.onchange=()=>toggle(c.dataset.sub,c.checked));
}
async function toggle(item,keep){
  await api('/api/keep',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,item,keep})});
  await loadProject(); renderSegs();
}

// ---------- step 2: order ----------
function keptSubs(){
  const out=[];
  (PROJECT.segments||[]).forEach(seg=>{ if(seg.keep!==false)
    (seg.subsections||[]).forEach(s=>{ if(s.keep!==false) out.push(s); }); });
  out.sort((a,b)=>(a.order||1e4)-(b.order||1e4)||a.start-b.start);
  return out;
}
function renderSeq(){
  const list=$('#seqList'); list.innerHTML='';
  keptSubs().forEach((s,i)=>{
    const li=document.createElement('li'); li.draggable=true; li.dataset.id=s.id;
    li.innerHTML=`<span class="pos">${i+1}</span>
      <div class="body"><b>${esc(s.tag||s.id)}</b> <span class="muted small">${mmss(s.start)}–${mmss(s.end)}</span><br>
      <span class="muted small">${esc((s.text||'').slice(0,120))}</span></div><span class="grab">⠿</span>`;
    list.appendChild(li);
  });
  wireDrag(list);
}
function wireDrag(list){
  let dragEl=null;
  list.querySelectorAll('li').forEach(li=>{
    li.addEventListener('dragstart',()=>{dragEl=li;li.classList.add('dragging');});
    li.addEventListener('dragend',()=>{li.classList.remove('dragging');commitOrder();});
    li.addEventListener('dragover',e=>{
      e.preventDefault();
      const after=[...list.querySelectorAll('li:not(.dragging)')].find(el=>
        e.clientY <= el.getBoundingClientRect().top + el.offsetHeight/2);
      if(after) list.insertBefore(dragEl,after); else list.appendChild(dragEl);
    });
  });
}
async function commitOrder(){
  const ids=[...$('#seqList').querySelectorAll('li')].map(li=>li.dataset.id);
  // translate to a permutation of the *previous* kept order
  const prev=keptSubs().map(s=>s.id);
  const perm=ids.map(id=>prev.indexOf(id)+1);
  await api('/api/reorder',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,method:'permutation',order:perm})});
  await loadProject(); renderSeq();
}
$('#btn-swap').onclick=async()=>{
  const r=await api('/api/reorder',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,method:'swap',a:+$('#swapA').value,b:+$('#swapB').value})});
  if(r.error)alert(r.error); await loadProject(); renderSeq();
};
$('#btn-perm').onclick=async()=>{
  const order=$('#perm').value.split(/[,\s]+/).filter(Boolean).map(Number);
  const r=await api('/api/reorder',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,method:'permutation',order})});
  if(r.error)alert(r.error); await loadProject(); renderSeq();
};
$('#btn-reset').onclick=async()=>{
  PROJECT.segments.forEach(seg=>seg.subsections.forEach(s=>s.order=Math.round(s.start*1000)));
  await saveProject();
  await api('/api/reorder',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,method:'permutation',order:keptSubs().map((_,i)=>i+1)})});
  await loadProject(); renderSeq();
};

// ---------- step 3: transitions ----------
async function loadSequence(){
  if(!TRANSITIONS.length) TRANSITIONS=(await api('/api/transitions')).transitions;
  const seq=await api('/api/sequence?id='+PID);
  const box=$('#boundList'); box.innerHTML='';
  if(seq.error){ box.innerHTML=`<p class="muted">${esc(seq.error)}</p>`; return; }
  seq.boundaries.forEach((b,i)=>{
    const it=seq.items, fromTag=it[i].tag||it[i].id, toTag=it[i+1].tag||it[i+1].id;
    const el=document.createElement('div'); el.className='bound'+(b.auto_gap?' isgap':'');
    el.innerHTML=`<span class="lbl"><b>${i+1} → ${i+2}</b> &nbsp; ${esc(fromTag)} → ${esc(toTag)}
        ${b.auto_gap?'<span class="gap small">● gap</span>':'<span class="muted small">adjacent</span>'}</span>
      <select data-to="${b.to}">${TRANSITIONS.map(t=>`<option ${t===b.type?'selected':''}>${t}</option>`).join('')}</select>
      <input type="number" step="0.1" min="0.1" value="${b.duration}" class="mini" data-dur="${b.to}">`;
    box.appendChild(el);
  });
  box.querySelectorAll('select[data-to]').forEach(sel=>sel.onchange=()=>setTrans(sel.dataset.to,sel.value,
    box.querySelector(`[data-dur="${sel.dataset.to}"]`).value));
  box.querySelectorAll('input[data-dur]').forEach(inp=>inp.onchange=()=>setTrans(inp.dataset.dur,
    box.querySelector(`select[data-to="${inp.dataset.dur}"]`).value,inp.value));
}
async function setTrans(to,type,duration){
  await api('/api/transition',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:PID,to,type,duration:+duration})});
}
$('#btn-allgaps').onclick=async()=>{
  const seq=await api('/api/sequence?id='+PID);
  for(const b of seq.boundaries) if(b.auto_gap) await setTrans(b.to,'crossfade',0.5);
  loadSequence();
};

// ---------- step 4: export ----------
$('#btn-render').onclick=async()=>{
  $('#result').innerHTML=''; $('#log').textContent='Starting…';
  await api('/api/render',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:PID})});
  poll(showResult);
};
function showResult(j){
  if(!j.result) return;
  const r=j.result;
  $('#result').innerHTML=`
    <p>${r.pass?'<span class="pass">PASS ✅</span>':'<span class="warn">CHECK ⚠️</span>'}
       &nbsp; ${r.duration}s · loudness ${r.loudness} LUFS · peak ${r.true_peak} dBTP</p>
    ${r.mp4?`<video controls src="/api/file?id=${PID}&name=episode.mp4"></video>`:''}
    <p>Download:
      ${r.mp4?`<a class="dl" href="/api/file?id=${PID}&name=episode.mp4" download>episode.mp4</a> · `:''}
      <a class="dl" href="/api/file?id=${PID}&name=episode.mp3" download>episode.mp3</a> ·
      <a class="dl" href="/api/file?id=${PID}&name=episode.srt" download>episode.srt</a></p>`;
}

// ---------- job polling ----------
function poll(onDone){
  const t=setInterval(async()=>{
    const j=await api('/api/job');
    $('#log').textContent=j.log||'…';
    const log=$('#log'); log.scrollTop=log.scrollHeight;
    if(!j.running && j.done){ clearInterval(t); onDone && onDone(j); }
  },700);
}

loadRecent();
