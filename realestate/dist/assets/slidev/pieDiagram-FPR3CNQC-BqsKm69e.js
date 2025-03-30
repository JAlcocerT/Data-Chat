import{p as N}from"./chunk-K2ZEYYM2-CWZzPOjd.js";import{p as B}from"./radar-MK3ICKWK-55CS4JTO-CS2bQ9Uw.js";import{a as i,g as U,s as Q,b as V,c as Z,v as j,t as q,l as C,d as H,G as J,a7 as K,aQ as X,aR as z,aS as Y,f as tt,A as et,aT as at,I as rt}from"./Mermaid.vue_vue_type_script_setup_true_lang-O-OG6FSh.js";import"./chunk-TGZYFRKZ-C96ujDh1.js";import"../index-BFqmFe_P.js";import"../modules/vue-FEAcYnSf.js";import"../modules/shiki-DcSPNieh.js";import"./lz-string-DHa7ly0R.js";import"../modules/file-saver-C8BEGaqa.js";var it=rt.pie,D={sections:new Map,showData:!1},m=D.sections,w=D.showData,st=structuredClone(it),ot=i(()=>structuredClone(st),"getConfig"),nt=i(()=>{m=new Map,w=D.showData,et()},"clear"),lt=i(({label:t,value:a})=>{m.has(t)||(m.set(t,a),C.debug(`added new section: ${t}, with value: ${a}`))},"addSection"),ct=i(()=>m,"getSections"),pt=i(t=>{w=t},"setShowData"),dt=i(()=>w,"getShowData"),G={getConfig:ot,clear:nt,setDiagramTitle:q,getDiagramTitle:j,setAccTitle:Z,getAccTitle:V,setAccDescription:Q,getAccDescription:U,addSection:lt,getSections:ct,setShowData:pt,getShowData:dt},gt=i((t,a)=>{N(t,a),a.setShowData(t.showData),t.sections.map(a.addSection)},"populateDb"),ut={parse:i(async t=>{const a=await B("pie",t);C.debug(a),gt(a,G)},"parse")},ft=i(t=>`
  .pieCircle{
    stroke: ${t.pieStrokeColor};
    stroke-width : ${t.pieStrokeWidth};
    opacity : ${t.pieOpacity};
  }
  .pieOuterCircle{
    stroke: ${t.pieOuterStrokeColor};
    stroke-width: ${t.pieOuterStrokeWidth};
    fill: none;
  }
  .pieTitleText {
    text-anchor: middle;
    font-size: ${t.pieTitleTextSize};
    fill: ${t.pieTitleTextColor};
    font-family: ${t.fontFamily};
  }
  .slice {
    font-family: ${t.fontFamily};
    fill: ${t.pieSectionTextColor};
    font-size:${t.pieSectionTextSize};
    // fill: white;
  }
  .legend text {
    fill: ${t.pieLegendTextColor};
    font-family: ${t.fontFamily};
    font-size: ${t.pieLegendTextSize};
  }
`,"getStyles"),mt=ft,ht=i(t=>{const a=[...t.entries()].map(s=>({label:s[0],value:s[1]})).sort((s,n)=>n.value-s.value);return at().value(s=>s.value)(a)},"createPieArcs"),St=i((t,a,F,s)=>{C.debug(`rendering pie chart
`+t);const n=s.db,y=H(),T=J(n.getConfig(),y.pie),$=40,o=18,d=4,c=450,h=c,S=K(a),l=S.append("g");l.attr("transform","translate("+h/2+","+c/2+")");const{themeVariables:r}=y;let[A]=X(r.pieOuterStrokeWidth);A??(A=2);const _=T.textPosition,g=Math.min(h,c)/2-$,R=z().innerRadius(0).outerRadius(g),W=z().innerRadius(g*_).outerRadius(g*_);l.append("circle").attr("cx",0).attr("cy",0).attr("r",g+A/2).attr("class","pieOuterCircle");const b=n.getSections(),v=ht(b),I=[r.pie1,r.pie2,r.pie3,r.pie4,r.pie5,r.pie6,r.pie7,r.pie8,r.pie9,r.pie10,r.pie11,r.pie12],p=Y(I);l.selectAll("mySlices").data(v).enter().append("path").attr("d",R).attr("fill",e=>p(e.data.label)).attr("class","pieCircle");let E=0;b.forEach(e=>{E+=e}),l.selectAll("mySlices").data(v).enter().append("text").text(e=>(e.data.value/E*100).toFixed(0)+"%").attr("transform",e=>"translate("+W.centroid(e)+")").style("text-anchor","middle").attr("class","slice"),l.append("text").text(n.getDiagramTitle()).attr("x",0).attr("y",-400/2).attr("class","pieTitleText");const x=l.selectAll(".legend").data(p.domain()).enter().append("g").attr("class","legend").attr("transform",(e,u)=>{const f=o+d,O=f*p.domain().length/2,P=12*o,L=u*f-O;return"translate("+P+","+L+")"});x.append("rect").attr("width",o).attr("height",o).style("fill",p).style("stroke",p),x.data(v).append("text").attr("x",o+d).attr("y",o-d).text(e=>{const{label:u,value:f}=e.data;return n.getShowData()?`${u} [${f}]`:u});const M=Math.max(...x.selectAll("text").nodes().map(e=>(e==null?void 0:e.getBoundingClientRect().width)??0)),k=h+$+o+d+M;S.attr("viewBox",`0 0 ${k} ${c}`),tt(S,c,k,T.useMaxWidth)},"draw"),vt={draw:St},bt={parser:ut,db:G,renderer:vt,styles:mt};export{bt as diagram};
