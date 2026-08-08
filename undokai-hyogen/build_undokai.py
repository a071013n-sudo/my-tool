#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
運動会・表現運動 指導資料ジェネレーター
guides/*.json を読み、演目ごとの自己完結HTMLを out/ に出力する。
"""
import json, os, re, sys, glob, zipfile

BASE = "https://a071013n-sudo.github.io/my-tool/undokai-hyogen/"

CSS = r"""
:root{
  --paper:#EFEAD8; --paper-hi:#FAF7EC; --sumi:#1F1C19; --sumi-soft:#5B554C;
  --aka:#C0362C; --aka-soft:#E8C6C1; --ao:#2C5F87; --ao-soft:#C6D6E1; --rule:#CFC7AE;
  --mincho:"Hiragino Mincho ProN","Yu Mincho","YuMincho","MS PMincho","Noto Serif JP",serif;
  --gothic:"Hiragino Kaku Gothic ProN","Yu Gothic","YuGothic","Meiryo","Noto Sans JP",sans-serif;
}
*{box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{margin:0;background:var(--paper);color:var(--sumi);font-family:var(--gothic);font-size:15px;line-height:1.75;}
.wrap{max-width:1000px;margin:0 auto;padding:0 18px 80px;}
header{padding:36px 0 22px;border-bottom:3px double var(--aka);}
.eyebrow{font-size:11px;letter-spacing:.32em;color:var(--aka);margin:0 0 12px;font-weight:700;}
h1{font-family:var(--mincho);font-size:clamp(28px,6vw,46px);font-weight:600;letter-spacing:.06em;margin:0 0 6px;line-height:1.25;}
.sub{font-family:var(--mincho);font-size:clamp(13px,2.5vw,16px);color:var(--sumi-soft);margin:0 0 18px;letter-spacing:.06em;}
.specs{display:flex;flex-wrap:wrap;gap:6px 22px;font-size:12.5px;color:var(--sumi-soft);margin:0;}
.specs b{color:var(--sumi);}
.backlink{margin:14px 0 0;font-size:12px;color:var(--sumi-soft);}
.backlink a{color:var(--ao);text-decoration:none;}
.backlink a:hover{color:var(--aka);}
section{margin-top:44px;}
h2{font-family:var(--mincho);font-size:22px;font-weight:600;letter-spacing:.06em;margin:0 0 6px;padding-bottom:8px;border-bottom:1px solid var(--rule);}
h2 small{font-family:var(--gothic);font-size:11px;letter-spacing:.2em;color:var(--aka);display:block;margin-bottom:4px;font-weight:700;}
.intro{font-size:13.5px;color:#4A463F;margin:12px 0 20px;max-width:62ch;}
h3{font-size:14px;letter-spacing:.06em;margin:26px 0 8px;}
.timeline{border:1px solid var(--rule);background:var(--paper-hi);}
.trow{display:grid;grid-template-columns:78px 1fr;border-bottom:1px solid var(--rule);}
.trow:last-child{border-bottom:0;}
.trow .tm{padding:10px 8px;font-size:12px;font-variant-numeric:tabular-nums;background:rgba(192,54,44,.06);border-right:1px solid var(--rule);color:var(--aka);font-weight:700;text-align:center;}
.trow .td{padding:10px 14px;font-size:13px;}
.trow .td b{display:block;font-size:13.5px;margin-bottom:2px;}
.trow .td span{color:var(--sumi-soft);font-size:12.5px;}
.moves{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;}
.move{background:var(--paper-hi);border:1px solid var(--rule);padding:12px;}
.move .num{font-size:10.5px;letter-spacing:.2em;color:var(--aka);font-weight:700;}
.move h4{font-family:var(--mincho);font-size:17px;margin:2px 0 8px;font-weight:600;}
.move svg{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--rule);}
.move p{font-size:12.5px;margin:9px 0 0;color:#3C3831;}
.move .cue{margin-top:7px;font-size:12.5px;color:var(--aka);border-left:2px solid var(--aka);padding-left:8px;}
.cue::before{content:"かける言葉　";font-weight:700;font-size:10.5px;letter-spacing:.12em;}
.block{background:var(--paper-hi);border:1px solid var(--rule);padding:14px 16px;margin-bottom:16px;}
.block h4{font-family:var(--mincho);font-size:18px;margin:0 0 2px;font-weight:600;}
.block .bnote{font-size:12.5px;color:var(--sumi-soft);margin:0 0 12px;}
.counts{display:flex;border:1px solid var(--sumi);overflow:hidden;}
.counts div{flex:1;border-right:1px solid var(--rule);text-align:center;font-size:11px;padding:4px 1px;background:#fff;line-height:1.35;}
.counts div:last-child{border-right:0;}
.counts div b{display:block;font-size:12px;color:var(--aka);}
.counts div.hold{background:var(--ao-soft);}
.counts div.key{background:var(--aka-soft);}
.ckey{display:flex;gap:14px;flex-wrap:wrap;font-size:11px;color:var(--sumi-soft);margin-top:6px;}
.ckey i{display:inline-block;width:11px;height:11px;border:1px solid var(--sumi);vertical-align:-1px;margin-right:4px;font-style:normal;}
.forms{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;}
.form{background:var(--paper-hi);border:1px solid var(--rule);padding:13px;}
.form h4{font-family:var(--mincho);font-size:17px;margin:0 0 3px;font-weight:600;}
.form .fno{font-size:10.5px;letter-spacing:.2em;color:var(--aka);font-weight:700;}
.form svg{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--rule);margin-top:8px;}
.form p{font-size:12.5px;margin:9px 0 0;color:#3C3831;}
table{width:100%;border-collapse:collapse;font-size:13px;background:var(--paper-hi);}
th,td{border:1px solid var(--rule);padding:7px 10px;text-align:left;vertical-align:top;}
th{background:rgba(192,54,44,.07);font-size:12px;letter-spacing:.06em;color:var(--aka);white-space:nowrap;}
td.n{font-variant-numeric:tabular-nums;white-space:nowrap;}
.gearsvg{max-width:420px;margin:0 0 18px;}
.gearsvg svg{width:100%;height:auto;background:#fff;border:1px solid var(--rule);}
.check{list-style:none;padding:0;margin:0;}
.check li{background:var(--paper-hi);border:1px solid var(--rule);padding:9px 12px;margin-bottom:7px;font-size:13px;display:flex;gap:10px;align-items:flex-start;}
.check input{margin-top:5px;flex:none;width:15px;height:15px;accent-color:var(--aka);}
.warn{border-left:3px solid var(--aka);background:rgba(192,54,44,.06);padding:11px 13px;font-size:13px;color:#6E241E;margin:16px 0 0;}
.warn b{letter-spacing:.1em;}
.note{font-size:12px;color:var(--sumi-soft);margin-top:10px;}
footer{margin-top:52px;padding-top:22px;border-top:3px double var(--aka);font-size:12.5px;color:#4A463F;}
footer h2{font-size:16px;border:0;padding:0;margin-bottom:8px;}
footer ul{margin:0 0 14px;padding-left:1.2em;}
footer li{margin-bottom:5px;}
@media print{
  body{background:#fff;font-size:11pt;}
  .wrap{padding:0;max-width:none;}
  section{break-inside:avoid;}
  .move,.form,.block{break-inside:avoid;background:#fff;}
  .backlink{display:none;}
  @page{size:A4;margin:14mm;}
}
"""

JS = r"""
var C={ink:"#1F1C19",aka:"#C0362C",ao:"#2C5F87",rule:"#CFC7AE",soft:"#8C867A"};
var RAD=Math.PI/180;

/* 角度は 0=真下, 90=画面右, 180=真上, 270=画面左 */
function offset(o,deg,len){return {x:o.x+len*Math.sin(deg*RAD), y:o.y+len*Math.cos(deg*RAD)};}

function legs(st){
  var L='stroke="'+C.ink+'" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"';
  switch(st){
    case "wide":   return '<path d="M50,60 L34,92 M50,60 L66,92" '+L+'/>';
    case "lunge":  return '<path d="M50,60 L28,90 M50,60 L64,74 L68,92" '+L+'/>';
    case "crouch": return '<path d="M50,62 L36,76 L34,92 M50,62 L64,76 L66,92" '+L+'/>';
    case "kneel":  return '<path d="M50,60 L64,76 L70,90 M50,60 L40,80 L28,88" '+L+'/>';
    case "jump":   return '<path d="M50,58 L38,76 L44,86 M50,58 L62,76 L56,86" '+L+'/>';
    case "toe":    return '<path d="M50,60 L46,90 M50,60 L54,90" '+L+'/>';
    default:       return '<path d="M50,60 L45,92 M50,60 L55,92" '+L+'/>';
  }
}

function prop(p,hR,hL){
  if(!p||p.type==="none") return "";
  var a=p.angle===undefined?180:p.angle, len=p.len||42, s="";
  var grip = p.grip==="L" ? hL : hR;
  if(p.from&&p.to){ grip=p.from; a=Math.atan2(p.to.x-p.from.x, p.to.y-p.from.y)/RAD; len=Math.sqrt(Math.pow(p.to.x-p.from.x,2)+Math.pow(p.to.y-p.from.y,2)); }
  if(p.type==="pom"||p.type==="cloth"){
    var r=p.type==="pom"?6:0;
    [hR,hL].forEach(function(h){
      if(p.type==="pom"){
        s+='<circle cx="'+h.x+'" cy="'+h.y+'" r="'+r+'" fill="'+C.aka+'" fill-opacity=".55" stroke="'+C.aka+'" stroke-width="1"/>';
      }else{
        var t=offset(h,a,16), m=offset(h,a+35,11);
        s+='<path d="M'+h.x+','+h.y+' L'+t.x+','+t.y+' Q'+m.x+','+m.y+' '+h.x+','+h.y+' Z" fill="'+C.aka+'" fill-opacity=".55" stroke="'+C.aka+'" stroke-width="1"/>';
      }
    });
    return s;
  }
  if(p.type==="naruko"){
    [hR,hL].forEach(function(h){
      s+='<rect x="'+(h.x-3.5)+'" y="'+(h.y-5)+'" width="7" height="10" rx="1.5" fill="'+C.aka+'" fill-opacity=".6" stroke="'+C.aka+'" stroke-width="1"/>';
    });
    return s;
  }
  if(p.type==="taiko"){
    var c=p.center||{x:38,y:52};
    s+='<ellipse cx="'+c.x+'" cy="'+c.y+'" rx="13" ry="14" fill="#fff" stroke="'+C.ink+'" stroke-width="2"/>';
    s+='<ellipse cx="'+c.x+'" cy="'+c.y+'" rx="8" ry="9" fill="'+C.aka+'" fill-opacity=".25" stroke="'+C.aka+'" stroke-width="1"/>';
    var b=offset(hR,a,15);
    s+='<line x1="'+hR.x+'" y1="'+hR.y+'" x2="'+b.x+'" y2="'+b.y+'" stroke="'+C.ink+'" stroke-width="2.4" stroke-linecap="round"/>';
    return s;
  }
  /* 棒状（旗・笠・傘・棒） */
  var tip=offset(grip,a,len), butt=offset(grip,a+180,9);
  if(p.type==="flag"){
    var A=offset(grip,a,len*0.34), B=tip, n=(a+(p.side===-1?-90:90));
    var Cc=offset(B,n,16), D=offset(A,n,16);
    var M={x:(Cc.x+D.x)/2,y:(Cc.y+D.y)/2}; M=offset(M,n,7);
    s+='<path d="M'+A.x+','+A.y+' L'+B.x+','+B.y+' L'+Cc.x+','+Cc.y+' Q'+M.x+','+M.y+' '+D.x+','+D.y+' Z" fill="'+C.aka+'" fill-opacity=".7" stroke="'+C.aka+'" stroke-width="1"/>';
  }
  if(p.type==="kasa"){
    var k1=offset(tip,a+90,15), k2=offset(tip,a-90,15), kc=offset(tip,a,9);
    s+='<path d="M'+k1.x+','+k1.y+' Q'+kc.x+','+kc.y+' '+k2.x+','+k2.y+' Z" fill="'+C.aka+'" fill-opacity=".6" stroke="'+C.aka+'" stroke-width="1.2"/>';
    s+='<line x1="'+k1.x+'" y1="'+k1.y+'" x2="'+k2.x+'" y2="'+k2.y+'" stroke="'+C.aka+'" stroke-width="1.2"/>';
  }
  if(p.type==="umbrella"){
    var u1=offset(tip,a+90,19), u2=offset(tip,a-90,19), uc=offset(tip,a,15);
    s+='<path d="M'+u1.x+','+u1.y+' Q'+uc.x+','+uc.y+' '+u2.x+','+u2.y+'" fill="'+C.aka+'" fill-opacity=".45" stroke="'+C.aka+'" stroke-width="1.3"/>';
    s+='<line x1="'+u1.x+'" y1="'+u1.y+'" x2="'+u2.x+'" y2="'+u2.y+'" stroke="'+C.aka+'" stroke-width="1.1"/>';
  }
  if(p.type==="board"){
    var v1=offset(grip,a+90,13), v2=offset(grip,a-90,13);
    var v3=offset(v2,a,18), v4=offset(v1,a,18);
    s+='<path d="M'+v1.x+','+v1.y+' L'+v2.x+','+v2.y+' L'+v3.x+','+v3.y+' L'+v4.x+','+v4.y+' Z" fill="'+C.aka+'" fill-opacity=".6" stroke="'+C.aka+'" stroke-width="1.2"/>';
    return s;
  }
  s+='<line x1="'+butt.x+'" y1="'+butt.y+'" x2="'+tip.x+'" y2="'+tip.y+'" stroke="'+C.ink+'" stroke-width="2.2" stroke-linecap="round"/>';
  return s;
}

function figure(m){
  var p=m.pose, SR={x:60,y:33}, SL={x:40,y:33};
  var hR=p.hR||offset(SR, p.aR, p.lR===undefined?26:p.lR);
  var hL=p.hL||offset(SL, p.aL, p.lL===undefined?26:p.lL);
  var L='stroke="'+C.ink+'" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"';
  var s='<svg viewBox="0 0 100 100" role="img" aria-label="'+m.name+'の姿勢図">';
  s+='<line x1="6" y1="92" x2="94" y2="92" stroke="'+C.rule+'" stroke-width="1.5"/>';
  s+=prop(p.prop,hR,hL);
  s+='<circle cx="50" cy="20" r="7.5" fill="#fff" stroke="'+C.ink+'" stroke-width="2.4"/>';
  s+='<path d="M50,27.5 L50,60" '+L+'/>';
  s+=legs(p.stance);
  s+='<path d="M40,33 L'+hL.x+','+hL.y+'" '+L+'/>';
  s+='<path d="M60,33 L'+hR.x+','+hR.y+'" '+L+'/>';
  s+='<line x1="40" y1="33" x2="60" y2="33" '+L+'/>';
  [hL,hR].forEach(function(h){s+='<circle cx="'+h.x+'" cy="'+h.y+'" r="2.6" fill="'+C.ao+'"/>';});
  if(p.arc){
    s+='<path d="M22,26 A30,14 0 1 1 78,26" fill="none" stroke="'+C.ao+'" stroke-width="1.4" stroke-dasharray="4 3"/>'+
       '<path d="M74,22 L78,26 L73,29" fill="none" stroke="'+C.ao+'" stroke-width="1.4"/>';
  }
  s+='</svg>';
  return s;
}

/* ── グラウンド図 ── */
function dots(x0,y0,cols,rows,gx,gy,color){
  var s="";
  for(var r=0;r<rows;r++)for(var c=0;c<cols;c++)
    s+='<circle cx="'+(x0+c*gx)+'" cy="'+(y0+r*gy)+'" r="2.6" fill="'+(color||C.aka)+'"/>';
  return s;
}
function ring(cx,cy,rx,ry,n,color){
  var s="";
  for(var i=0;i<n;i++){var a=i/n*Math.PI*2;
    s+='<circle cx="'+(cx+rx*Math.sin(a)).toFixed(1)+'" cy="'+(cy-ry*Math.cos(a)).toFixed(1)+'" r="2.6" fill="'+(color||C.aka)+'"/>';}
  return s;
}
function arrow(x1,y1,x2,y2){
  var a=Math.atan2(y2-y1,x2-x1);
  var p=function(d,o){return (x2-Math.cos(a-o)*d).toFixed(1)+','+(y2-Math.sin(a-o)*d).toFixed(1);};
  return '<line x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'" stroke="'+C.ao+'" stroke-width="1.4" stroke-dasharray="4 3"/>'+
         '<path d="M'+p(7,0.45)+' L'+x2+','+y2+' L'+p(7,-0.45)+'" fill="none" stroke="'+C.ao+'" stroke-width="1.4"/>';
}
function label(x,y,t,col,size){
  return '<text x="'+x+'" y="'+y+'" font-size="'+(size||9)+'" fill="'+(col||C.soft)+'" text-anchor="middle">'+t+'</text>';
}
function ground(inner){
  var s='<svg viewBox="0 0 320 200" role="img"><rect width="320" height="200" fill="#fff"/>';
  s+='<rect x="26" y="30" width="268" height="150" rx="75" fill="none" stroke="'+C.rule+'" stroke-width="1.5" stroke-dasharray="5 4"/>';
  s+='<rect x="140" y="6" width="40" height="14" fill="none" stroke="'+C.soft+'" stroke-width="1.2"/>';
  s+=label(160,16,"朝礼台",C.soft,8);
  s+=label(160,196,"▼ 保護者テント（正面）",C.soft,8);
  s+='<text x="12" y="108" font-size="8" fill="'+C.soft+'" text-anchor="middle" transform="rotate(-90 12 108)">入場門</text>';
  s+='<text x="308" y="108" font-size="8" fill="'+C.soft+'" text-anchor="middle" transform="rotate(90 308 108)">退場門</text>';
  return s+inner+'</svg>';
}
function buildForm(f){
  var inner="";
  (f.groups||[]).forEach(function(g){inner+=dots(g[0],g[1],g[2],g[3],g[4],g[5],g[6]);});
  (f.rings||[]).forEach(function(g){inner+=ring(g[0],g[1],g[2],g[3],g[4],g[5]);});
  (f.arrows||[]).forEach(function(a){inner+=arrow(a[0],a[1],a[2],a[3]);});
  (f.labels||[]).forEach(function(l){inner+=label(l[0],l[1],l[2],l[3],l[4]);});
  return ground(inner);
}

/* ── 組み立て ── */
function el(id){return document.getElementById(id);}
function render(G){
  if(G.timeline) el("timeline").innerHTML=G.timeline.map(function(r){
    return '<div class="trow"><div class="tm">'+r[0]+'</div><div class="td"><b>'+r[1]+'</b>'+r[2]+
           (r[3]?'<br><span>'+r[3]+'</span>':'')+'</div></div>';}).join("");

  if(G.moves) el("moves").innerHTML=G.moves.items.map(function(m,i){
    var fig = m.pose ? figure(m) : "";
    return '<div class="move"><p class="num">'+(G.moves.label||"技")+' '+String(i+1).padStart(2,"0")+'</p>'+
           '<h4>'+m.name+'</h4>'+fig+'<p>'+m.desc+'</p>'+(m.cue?'<p class="cue">'+m.cue+'</p>':'')+'</div>';}).join("");

  if(G.blocks) el("blocks").innerHTML=G.blocks.map(function(b){
    var cells=b.rows.map(function(r){return '<div class="'+(r[2]||"")+'"><b>'+r[0]+'</b>'+r[1]+'</div>';}).join("");
    return '<div class="block"><h4>'+b.n+'　'+b.t+'</h4><p class="bnote">'+b.note+'</p><div class="counts">'+cells+'</div></div>';
  }).join("");

  if(G.forms) el("forms").innerHTML=G.forms.map(function(f){
    return '<div class="form"><p class="fno">'+f.n+'</p><h4>'+f.t+'</h4>'+buildForm(f)+'<p>'+f.p+'</p></div>';}).join("");

  if(G.gear) el("gear").innerHTML='<table>'+G.gear.map(function(r){
    return '<tr><th>'+r[0]+'</th><td>'+r[1]+'</td></tr>';}).join("")+'</table>';

  if(G.plan) el("plan").innerHTML='<tr><th>時</th><th>場所</th><th>内容</th><th>この時間で外せないこと</th></tr>'+
    G.plan.map(function(r){return '<tr><td class="n">'+r[0]+'</td><td class="n">'+r[1]+'</td><td>'+r[2]+'</td><td>'+r[3]+'</td></tr>';}).join("");

  if(G.music) el("music").innerHTML='<table>'+G.music.rows.map(function(r){
    return '<tr><th>'+r[0]+'</th><td>'+r[1]+'</td></tr>';}).join("")+'</table>';

  if(G.safety) el("safety").innerHTML=G.safety.map(function(t){
    return '<li><input type="checkbox"><span>'+t+'</span></li>';}).join("");
}
render(G);
"""

TPL = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} 指導資料｜運動会・表現運動</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{base}{id}.html">
<meta property="og:type" content="article">
<meta property="og:title" content="{name} 指導資料｜運動会・表現運動">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{base}{id}.html">
<meta property="og:site_name" content="せんせいの道具箱">
<style>{css}</style>
</head>
<body>
<div class="wrap">

<header>
  <p class="eyebrow">せんせいの道具箱 ／ 運動会・表現運動 ／ 指導資料</p>
  <h1>{name}</h1>
  <p class="sub">{sub}</p>
  <p class="specs">
    <span>おすすめ学年 <b>{grades}</b></span>
    <span>難易度 <b>{stars}</b></span>
    <span>持ち時間 <b>10分</b>／演技 <b>{main}</b></span>
    <span>練習時数 <b>{practice}</b></span>
  </p>
  <p class="backlink"><a href="../">せんせいの道具箱</a> ／ <a href="index.html">表現運動インデックス</a></p>
</header>

<section>
  <h2><small>01</small>この演目の考え方</h2>
  <p class="intro">{intro}</p>
</section>

<section>
  <h2><small>02</small>演技{main}の構成</h2>
  <p class="intro">{tl_intro}</p>
  <div class="timeline" id="timeline"></div>
</section>

{sec_moves}

{sec_blocks}

<section>
  <h2><small>{n_forms}</small>隊形案</h2>
  <p class="intro">{forms_intro}</p>
  <div class="forms" id="forms"></div>
  {forms_warn}
</section>

{sec_gear}

<section>
  <h2><small>{n_plan}</small>練習計画</h2>
  <table id="plan"></table>
  <p class="note">{plan_note}</p>
</section>

<section>
  <h2><small>{n_music}</small>選曲</h2>
  <p class="intro">{music_intro}</p>
  <div id="music"></div>
  {music_extra}
  <div class="warn">{music_warn}</div>
</section>

<section>
  <h2><small>{n_safety}</small>安全チェックリスト</h2>
  <ul class="check" id="safety"></ul>
</section>

<footer>
  <h2>この資料について</h2>
  <ul>{footer_notes}</ul>
</footer>

</div>
<script>
var G = {data};
{js}
</script>
</body>
</html>
"""

SEC_MOVES = """<section>
  <h2><small>{n}</small>{title}</h2>
  <p class="intro">{intro}</p>
  <div class="moves" id="moves"></div>
  {warn}
</section>"""

SEC_BLOCKS = """<section>
  <h2><small>{n}</small>振付ブロック</h2>
  <p class="intro">{intro}</p>
  <div id="blocks"></div>
  <div class="ckey">
    <span><i style="background:#fff"></i>動く</span>
    <span><i style="background:var(--ao-soft)"></i>静止して保つ</span>
    <span><i style="background:var(--aka-soft)"></i>キメ</span>
  </div>
</section>"""

SEC_GEAR = """<section>
  <h2><small>{n}</small>{title}</h2>
  <p class="intro">{intro}</p>
  {svg}
  <div id="gear"></div>
  <p class="note">{note}</p>
</section>"""

DEFAULT_FOOTER = [
  "掲載した動きと構成はこの資料のために作成したものです。そのまま使っても、組み替えても構いません。",
  "楽曲・既存の振付作品には権利者がいます。他校や動画で見た振付をそのまま使う場合は、出所と利用条件を確認してください。",
  "安全に関する記載は一般的な整理です。実施の可否は自治体・学校のガイドラインが優先します。",
  "オフラインで動作する単一HTMLファイルです。印刷するとA4に整います。"
]

DEFAULT_MUSIC_WARN = ("<b>当日、校庭で流すことは著作権法38条1項（非営利・無料・無報酬）により許諾不要です。</b>"
  "ただし演技を録画してDVDを配る・限定公開で配信する場合は複製権・公衆送信権の手続きが別に必要で、"
  "市販CD音源ならJASRAC等に加えてレコード会社（著作隣接権者）の了解も要ります。"
  "尺を合わせるカット編集も複製にあたるため、編集済みデータを校外に渡さないようにしてください。")


def build(g):
    n = 3
    sec_moves = ""
    if g.get("moves"):
        sec_moves = SEC_MOVES.format(
            n="%02d" % n,
            title=g["moves"].get("title", "基本の動き"),
            intro=g["moves"].get("intro", ""),
            warn=('<div class="warn">%s</div>' % g["moves"]["warn"]) if g["moves"].get("warn") else "")
        n += 1
    sec_blocks = ""
    if g.get("blocks"):
        sec_blocks = SEC_BLOCKS.format(n="%02d" % n, intro=g.get("blocks_intro", ""))
        n += 1
    n_forms = "%02d" % n; n += 1
    sec_gear = ""
    if g.get("gear"):
        sec_gear = SEC_GEAR.format(n="%02d" % n, title=g.get("gear_title", "用意するもの"),
                                   intro=g.get("gear_intro", ""), note=g.get("gear_note", ""),
                                   svg=('<div class="gearsvg">%s</div>' % g["gear_svg"]) if g.get("gear_svg") else "")
        n += 1
    n_plan = "%02d" % n; n += 1
    n_music = "%02d" % n; n += 1
    n_safety = "%02d" % n

    data = {k: g[k] for k in ("timeline", "moves", "blocks", "forms", "gear", "plan", "safety") if k in g}
    data["music"] = {"rows": g["music"]["rows"]}

    html = TPL.format(
        css=CSS, js=JS,
        id=g["id"], base=BASE,
        meta=(g["name"] + "｜" + g["sub"] + " おすすめ学年" + g["grades"] + "、演技" + g["main"] + "、練習" + g["practice"] + "。動きの図・隊形図・練習計画・選曲条件・安全チェックリスト。")[:150],
        name=g["name"], sub=g["sub"], grades=g["grades"],
        stars="★" * g["level"], main=g["main"], practice=g["practice"],
        intro=g["intro"],
        tl_intro=g.get("tl_intro", "入場1分30秒＋演技%s＋退場1分30秒＋予備で10分。演技部分の割り振りは次のとおりです。" % g["main"]),
        sec_moves=sec_moves, sec_blocks=sec_blocks,
        n_forms=n_forms, forms_intro=g.get("forms_intro", ""),
        forms_warn=('<div class="warn">%s</div>' % g["forms_warn"]) if g.get("forms_warn") else "",
        sec_gear=sec_gear,
        n_plan=n_plan, plan_note=g.get("plan_note", ""),
        n_music=n_music, music_intro=g.get("music_intro", "曲は毎年変わりますが、選ぶ条件は変わりません。まず条件で絞り、そのうえで候補を聴くのが早いです。"),
        music_extra=('<h3>候補としてよく挙がる曲</h3><p class="intro">%s</p>' % g["music"]["candidates"]) if g["music"].get("candidates") else "",
        music_warn=g["music"].get("warn", DEFAULT_MUSIC_WARN),
        n_safety=n_safety,
        footer_notes="".join("<li>%s</li>" % x for x in g.get("footer", DEFAULT_FOOTER)),
        data=json.dumps(data, ensure_ascii=False))
    return html


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "content/undokai"
    out = sys.argv[2] if len(sys.argv) > 2 else "undokai-hyogen"
    os.makedirs(out, exist_ok=True)

    guides = []
    for f in sorted(glob.glob(os.path.join(src, "*.json"))):
        guides.extend(json.load(open(f, encoding="utf-8")))

    ids = [g["id"] for g in guides]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        sys.exit("ERROR: id が重複しています: %s" % ", ".join(sorted(dup)))

    for g in guides:
        path = os.path.join(out, "%s.html" % g["id"])
        open(path, "w", encoding="utf-8").write(build(g))
        print("  %-22s %6.1f KB" % (g["id"] + ".html", os.path.getsize(path) / 1024))

    # インデックスの GUIDE 対応表を自動更新し、ずれがあれば失敗させる
    idx = os.path.join(out, "index.html")
    if os.path.exists(idx):
        h = open(idx, encoding="utf-8").read()
        names = re.findall(r'\n  name:"([^"]+)"', h)
        table = {g["name"]: g["id"] for g in guides}
        missing = [n for n in names if n not in table]
        orphan = [g["name"] for g in guides if g["name"] not in names]
        if missing or orphan:
            sys.exit("ERROR: インデックスと資料が一致しません\n  資料なし: %s\n  一覧なし: %s"
                     % (missing or "なし", orphan or "なし"))
        h = re.sub(r"var GUIDE = \{.*?\};",
                   "var GUIDE = " + json.dumps(table, ensure_ascii=False) + ";", h, count=1, flags=re.S)
        open(idx, "w", encoding="utf-8").write(h)
        print("  index.html             GUIDE %d件を更新" % len(table))

    # sitemap
    urls = [BASE] + ["%s%s.html" % (BASE, g["id"]) for g in guides]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append("  <url><loc>%s</loc></url>" % u)
    sm.append("</urlset>")
    open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))

    # 一式まとめてダウンロード用の zip
    zpath = os.path.join(out, "undokai-guides.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(out)):
            if not f.endswith(".html"):
                continue
            info = zipfile.ZipInfo("undokai-hyogen/" + f, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, open(os.path.join(out, f), "rb").read())
    print("  sitemap.xml / undokai-guides.zip (%.0f KB)" % (os.path.getsize(zpath) / 1024))
    print("--- %d guides" % len(guides))


if __name__ == "__main__":
    main()
