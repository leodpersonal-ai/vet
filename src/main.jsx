import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

const books = [
  {n:'01', title:'Atlas de Farmacología Veterinaria',detail:'24 fundamentos y 20 fichas de principios activos',pages:24,kit:'Esencial'},
  {n:'02', title:'Farmacología en 40 preguntas',detail:'40 ejercicios con soluciones razonadas',pages:30,kit:'Esencial'},
  {n:'03', title:'Laboratorio Veterinario',detail:'Muestra, hemograma, bioquímica y seis informes resueltos',pages:25,kit:'Profesional'},
  {n:'04', title:'Interpretación Clínica de Exámenes',detail:'Ocho rutas y cinco informes comentados',pages:17,kit:'Profesional'},
  {n:'05', title:'Casos Clínicos Razonados',detail:'Diez casos para practicar prioridades y decisiones',pages:24,kit:'Profesional'},
  {n:'06', title:'SOAP Veterinario',detail:'Seis notas resueltas y cuatro plantillas imprimibles',pages:18,kit:'Profesional'},
];
const checkout = { esencial: '', profesional: '' }; // Pegar aquí los enlaces finales de Hotmart.
const jump = id => document.getElementById(id)?.scrollIntoView({behavior:'smooth'});
function Arrow(){return <span aria-hidden="true">↗</span>}
function Brand(){return <a className="brand" href="#inicio" aria-label="Atlas Veterinario, inicio"><span className="brand-icon">✳</span><span>atlas<strong>veterinario</strong></span></a>}
function BuyButton({plan,children,light=false}){
  const url=checkout[plan];
  return url ? <a className={`button ${light?'button-light':''}`} href={url} target="_blank" rel="noopener noreferrer">{children}<Arrow/></a> : <span className={`button button-pending ${light?'button-light':''}`} aria-label="Enlace de compra en preparación">Acceso en preparación <Arrow/></span>;
}
function App(){
  const [preview,setPreview]=useState(0);
  const [faq,setFaq]=useState(null);
  return <>
    <header className="nav"><div className="nav-inner"><Brand/><nav aria-label="Navegación"><a href="#contenido">Contenido</a><a href="#por-dentro">Por dentro</a><a href="#kits">Kits</a></nav><button onClick={()=>jump('kits')} className="nav-cta">Ver los kits <Arrow/></button></div></header>
    <main>
      <section className="hero" id="inicio"><div className="hero-inner">
        <div className="hero-copy"><span className="eyebrow pale"><span className="eyebrow-rule"/> PARA ESTUDIANTES DE MEDICINA VETERINARIA</span>
          <h1>Estudia con una <em>biblioteca que puedes usar.</em></h1>
          <p>Farmacología, laboratorio y razonamiento clínico reunidos en seis e-books para perros y gatos. Lee un concepto, resuelve un caso y vuelve a consultar cuando lo necesites.</p>
          <div className="hero-actions"><button className="button button-cream" onClick={()=>jump('kits')}>Conocer los kits <Arrow/></button><button className="text-button" onClick={()=>jump('por-dentro')}>Ver páginas reales <span aria-hidden="true">↓</span></button></div>
          <div className="hero-facts"><div><strong>06</strong><span>e-books en PDF</span></div><div><strong>138</strong><span>páginas de estudio</span></div><div><strong>40</strong><span>preguntas comentadas</span></div></div>
        </div>
        <div className="hero-visual" aria-label="Portadas reales de los e-books"><div className="halo"/><img className="cover-stack cover-back" src="/images/03-cover.webp" alt="Portada del cuaderno de laboratorio"/><img className="cover-stack cover-mid" src="/images/05-cover.webp" alt="Portada de casos clínicos"/><img className="cover-stack cover-front" src="/images/01-cover.webp" alt="Portada del atlas de farmacología"/><div className="visual-note">Edición digital <span>2026</span></div></div>
      </div></section>
      <div className="ribbon"><div>FARMACOLOGÍA <span>✳</span> LABORATORIO <span>✳</span> CASOS CLÍNICOS <span>✳</span> MÉTODO SOAP <span>✳</span> FARMACOLOGÍA <span>✳</span> LABORATORIO</div></div>
      <section className="intro wrap"><div className="section-mark">01 / UNA FORMA DE ESTUDIAR</div><div><h2>Menos apuntes sueltos.<br/><em>Más práctica guiada.</em></h2><p>El atlas organiza los conceptos. El quiz ayuda a comprobar lo aprendido. Los cuadernos de laboratorio, los casos y SOAP muestran cómo ordenar la información sin confundir un hallazgo con un diagnóstico.</p></div></section>
      <section className="collection" id="contenido"><div className="wrap"><div className="section-heading"><div><span className="section-mark">02 / LA COLECCIÓN</span><h2>Qué recibes en los kits</h2></div><p>Seis archivos individuales, para consultar en el móvil, la computadora o imprimir.</p></div><div className="book-grid">{books.map(book=><article className="book" key={book.n}><div className="book-art"><img src={`/images/${book.n}-cover.webp`} alt={`Portada de ${book.title}`} loading="lazy"/></div><div className="book-text"><span>{book.n} / {book.kit.toUpperCase()}</span><h3>{book.title}</h3><p>{book.detail}</p><div className="book-foot">{book.pages} páginas <Arrow/></div></div></article>)}</div></div></section>
      <section className="inside wrap" id="por-dentro"><div className="inside-copy"><span className="section-mark">03 / PÁGINAS REALES</span><h2>Mira el material <em>por dentro.</em></h2><p>Estas imágenes son páginas de los PDF finales, con ejemplos, rutas de razonamiento y ejercicios. Puedes elegir un e-book para ver una muestra.</p><div className="inside-tabs" role="tablist" aria-label="Elegir muestra">{books.map((b,i)=><button key={b.n} role="tab" aria-selected={preview===i} className={preview===i?'selected':''} onClick={()=>setPreview(i)}>{b.n} <span>{b.title}</span></button>)}</div></div><div className="inside-view"><div className="paper-frame"><img src={`/images/${books[preview].n}-sample.webp`} alt={`Página interior de ${books[preview].title}`} loading="lazy"/></div><div className="view-caption"><span>VISTA PREVIA / {books[preview].n}</span><strong>{books[preview].title}</strong></div></div></section>
      <section className="method"><div className="wrap method-inner"><div><span className="section-mark light-mark">04 / HECHO PARA PRACTICAR</span><h2>De leer a <em>razonar.</em></h2></div><div className="method-steps"><div><span>01</span><h3>Consulta</h3><p>Encuentra un concepto, mecanismo o prueba sin navegar entre documentos dispersos.</p></div><div><span>02</span><h3>Resuelve</h3><p>Contesta preguntas y compara tu razonamiento con las explicaciones.</p></div><div><span>03</span><h3>Documenta</h3><p>Practica con casos, resultados simulados y notas SOAP completas.</p></div></div></div></section>
      <section className="offers wrap" id="kits"><div className="section-heading"><div><span className="section-mark">05 / ELIGE TU KIT</span><h2>Empieza por lo que necesitas.</h2></div><p>Entrega digital por Hotmart. Elige el contenido que quieres estudiar.</p></div><div className="offer-grid"><article className="offer"><span className="offer-tag">PARA EMPEZAR</span><h3>Kit Esencial</h3><p>La base de farmacología con práctica para reforzar lo aprendido.</p><div className="offer-number">2 <span>e-books · 54 páginas</span></div><ul><li>Atlas de Farmacología Veterinaria</li><li>Farmacología en 40 preguntas</li><li>Archivos PDF para consultar o imprimir</li></ul><BuyButton plan="esencial">Elegir Kit Esencial</BuyButton></article><article className="offer offer-featured"><span className="offer-tag">COLECCIÓN COMPLETA</span><h3>Kit Profesional</h3><p>El atlas, el quiz y cuatro cuadernos para practicar la lectura de casos y exámenes.</p><div className="offer-number">6 <span>e-books · 138 páginas</span></div><ul><li>Todo el Kit Esencial</li><li>Laboratorio y lectura de exámenes</li><li>Diez casos clínicos razonados</li><li>Ejemplos y plantillas SOAP</li></ul><BuyButton plan="profesional" light>Elegir Kit Profesional</BuyButton></article></div></section>
      <section className="faq wrap"><div><span className="section-mark">06 / PREGUNTAS FRECUENTES</span><h2>Antes de empezar.</h2></div><div className="faq-list">{[
        ['¿En qué formato recibo el material?','Son seis archivos PDF individuales. Puedes abrirlos en el móvil, la computadora o imprimir las páginas que quieras estudiar.'],
        ['¿Cuál es la diferencia entre los kits?','El Esencial incluye el Atlas y el Quiz. El Profesional incluye esos dos más Laboratorio, Interpretación de Exámenes, Casos Clínicos y SOAP.'],
        ['¿Incluyen dosis para prescribir?','No. Son materiales educativos de estudio y razonamiento. Toda prescripción requiere evaluación veterinaria y la ficha técnica vigente del producto en tu país.'],
        ['¿Los casos y los resultados son pacientes reales?','No. Los escenarios y los intervalos de referencia usados en ejercicios son simulados para practicar la interpretación.']
      ].map(([q,a],i)=><div className="faq-item" key={q}><button aria-expanded={faq===i} onClick={()=>setFaq(faq===i?null:i)}><span>{q}</span><b>{faq===i?'−':'+'}</b></button>{faq===i&&<p>{a}</p>}</div>)}</div></section>
    </main><footer><div className="wrap footer-inner"><Brand/><p>Material educativo para perros y gatos. No sustituye evaluación clínica ni protocolos locales.</p><span>© 2026 Atlas Veterinario</span></div></footer>
  </>;
}
createRoot(document.getElementById('root')).render(<App/>);
