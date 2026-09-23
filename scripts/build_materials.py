from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from xml.sax.saxutils import escape
import os

OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','public','materiales'))
os.makedirs(OUT,exist_ok=True)
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
GREEN=colors.HexColor('#153D38'); TEAL=colors.HexColor('#33786A'); CREAM=colors.HexColor('#F8F5EA'); GOLD=colors.HexColor('#C79553'); INK=colors.HexColor('#263B3A'); GREY=colors.HexColor('#596A68')
ST={
 'cover':ParagraphStyle('cover',fontName='DejaVuBold',fontSize=31,leading=39,textColor=GREEN,spaceAfter=16),
 'subtitle':ParagraphStyle('subtitle',fontName='DejaVu',fontSize=12,leading=19,textColor=GREY,spaceAfter=10),
 'h1':ParagraphStyle('h1',fontName='DejaVuBold',fontSize=19,leading=25,textColor=GREEN,spaceAfter=14),
 'h2':ParagraphStyle('h2',fontName='DejaVuBold',fontSize=12,leading=17,textColor=TEAL,spaceBefore=13,spaceAfter=5),
 'body':ParagraphStyle('body',fontName='DejaVu',fontSize=9.5,leading=15,textColor=INK,spaceAfter=7),
 'small':ParagraphStyle('small',fontName='DejaVu',fontSize=8,leading=12,textColor=GREY,spaceAfter=5),
 'box':ParagraphStyle('box',fontName='DejaVu',fontSize=9.5,leading=15,textColor=INK),
 'label':ParagraphStyle('label',fontName='DejaVuBold',fontSize=8.5,leading=13,textColor=GREEN),
}
SOURCES={
 'M1':('Merck Veterinary Manual, Pharmacokinetics','https://www.merckvetmanual.com/pharmacology/pharmacology-introduction/pharmacokinetics'),
 'M2':('Merck Veterinary Manual, Drug Action in Animals: Pharmacodynamics','https://www.merckvetmanual.com/pharmacology/pharmacology-introduction/drug-action-in-animals-pharmacodynamics'),
 'M3':('Merck Veterinary Manual, Antimicrobial Drug Factors for Animals','https://www.merckvetmanual.com/pharmacology/antimicrobials/antimicrobial-drug-factors-for-animals'),
 'M4':('Merck Veterinary Manual, Clinical Hematology','https://www.merckvetmanual.com/clinical-pathology-and-procedures/diagnostic-procedures-for-the-private-practice-laboratory/clinical-hematology'),
 'M5':('Merck Veterinary Manual, Clinical Biochemistry','https://www.merckvetmanual.com/clinical-pathology-and-procedures/diagnostic-procedures-for-the-private-practice-laboratory/clinical-biochemistry'),
 'M6':('Merck Veterinary Manual, Urinalysis','https://www.merckvetmanual.com/clinical-pathology-and-procedures/diagnostic-procedures-for-the-private-practice-laboratory/urinalysis'),
 'M7':('Merck Veterinary Manual, Overview of Antifungal Agents for Use in Animals','https://www.merckvetmanual.com/pharmacology/antifungal-agents/overview-of-antifungal-agents-for-use-in-animals'),
 'M8':('Merck Veterinary Manual, Ectoparasiticides Used in Small Animals','https://www.merckvetmanual.com/pharmacology/ectoparasiticides/ectoparasiticides-used-in-small-animals'),
 'F1':('FDA, Controlling Pain and Inflammation in Your Dog with NSAIDs','https://www.fda.gov/animal-veterinary/animal-health-literacy/controlling-pain-and-inflammation-your-dog-nonsteroidal-anti-inflammatory-drugs'),
 'F2':('FDA, Information About Boxed Warning on Meloxicam Labels Regarding Safety Risks to Cats','https://www.fda.gov/animal-veterinary/product-safety-information/information-about-boxed-warning-meloxicam-labels-regarding-safety-risks-cats'),
 'A1':('AVMA, Judicious Therapeutic Use of Antimicrobials','https://www.avma.org/resources-tools/avma-policies/judicious-therapeutic-use-antimicrobials'),
 'W1':('WSAVA, Global Pain Guidelines','https://wsava.org/global-guidelines/pain-guidelines/'),
}
NOTICE='Material educativo para estudiantes y profesionales. Enfocado en perros y gatos. No sustituye la evaluación clínica, el prospecto autorizado ni los protocolos locales. La prescripción, elección de especie, vía, dosis y seguimiento corresponden al médico veterinario responsable.'

def p(s,style='body'): return Paragraph(escape(s).replace('\n','<br/>'),ST[style])
def rich(s,style='body'): return Paragraph(s,ST[style])
def box(text,bg=CREAM):
 t=Table([[p(text,'box')]],colWidths=[172*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),('BOX',(0,0),(-1,-1),0.6,colors.HexColor('#D6E1DA')),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]));return t
def bullet(s):return rich('<font color="#33786A">•</font> '+escape(s))
def section(title,items):
 out=[p(title,'h2')]
 out += [bullet(x) for x in items]
 return out
def refs(keys):
 a=[p('Fuentes para ampliar y verificar','h2')]
 for k in dict.fromkeys(keys):
  title,url=SOURCES[k];a.append(rich('<b>'+k+'</b>  '+escape(title)+'<br/><link href="'+url+'" color="#33786A">'+escape(url)+'</link>','small'))
 return a
ACCENTS=[colors.HexColor(x) for x in ('#24594e','#839d82','#456b75','#bb835b','#736d86','#5d8f82')]
def footer(canv,doc):
 w,h=A4;canv.saveState();canv.setFillColor(GREEN);canv.rect(0,h-6*mm,w,6*mm,fill=1,stroke=0);canv.setStrokeColor(colors.HexColor('#DDE6DF'));canv.line(19*mm,17*mm,w-19*mm,17*mm);canv.setFont('DejaVu',7.5);canv.setFillColor(GREY);canv.drawString(19*mm,12*mm,'✳  ATLAS VETERINARIO  /  Edición educativa 2026');canv.drawRightString(w-19*mm,12*mm,str(doc.page));canv.restoreState()
def front(canv,doc,accent):
 w,h=A4;canv.saveState();canv.setFillColor(colors.HexColor('#F3F5EE'));canv.rect(0,0,w,h,fill=1,stroke=0)
 canv.setFillColor(accent);canv.rect(0,0,w,94*mm,fill=1,stroke=0)
 canv.setStrokeColor(colors.HexColor('#FFFFFF'));canv.setLineWidth(.8)
 for offset,scale in [(-26,1),(-6,.72),(19,.48)]:
  canv.saveState();canv.translate(w/2+offset*mm,47*mm);canv.rotate(27+offset/2);canv.scale(scale,1);canv.circle(0,0,42*mm,fill=0,stroke=1);canv.restoreState()
 canv.setFont('DejaVuBold',9);canv.setFillColor(GREEN);canv.drawString(19*mm,h-21*mm,'✳  ATLAS VETERINARIO')
 canv.setFont('DejaVu',7);canv.drawRightString(w-19*mm,h-21*mm,'BIBLIOTECA DE ESTUDIO · 2026')
 canv.setFillColor(colors.white);canv.setFont('DejaVuBold',8);canv.drawString(19*mm,25*mm,'FARMACOLOGÍA VETERINARIA')
 canv.drawRightString(w-19*mm,25*mm,'EDICIÓN DIGITAL')
 canv.restoreState()
def build(name,story):
 path=os.path.join(OUT,name+'.pdf');accent=ACCENTS[int(name[:2])-1];SimpleDocTemplate(path,pagesize=A4,rightMargin=19*mm,leftMargin=19*mm,topMargin=26*mm,bottomMargin=21*mm,title=name.replace('_',' '),author='Atlas Veterinario').build(story,onFirstPage=lambda c,d:front(c,d,accent),onLaterPages=footer);print(path)
def cover(title,sub,tag):
 return [Spacer(1,20*mm),p(tag.upper(),'h2'),p(title,'cover'),p(sub,'subtitle'),Spacer(1,8*mm),box(NOTICE),PageBreak()]

atlas=[
 ('01','Farmacocinética: ADME','Qué ocurre','Absorción, distribución, metabolismo y excreción describen el recorrido temporal de un fármaco en el organismo.','Aplicación','La vía, la formulación, la perfusión, la edad y la función orgánica pueden cambiar la exposición.','Verificar','Especie, estado de hidratación, función hepática y renal, interacciones y ficha del producto.','M1'),
 ('02','Farmacodinámica','Qué ocurre','Relaciona concentración y efecto: receptores, enzimas, canales y mediadores determinan respuesta terapéutica y toxicidad.','Aplicación','La misma exposición puede generar efectos distintos según especie, sensibilidad y enfermedad.','Verificar','Objetivo clínico, respuesta, margen de seguridad y eventos adversos.','M2'),
 ('03','Biodisponibilidad y vías','Qué ocurre','La fracción que alcanza la circulación depende de la vía y de la formulación. La administración oral puede sufrir metabolismo de primer paso.','Aplicación','No intercambiar formulaciones oral, tópica o inyectable suponiendo equivalencia.','Verificar','Vía autorizada, posibilidad de ingestión por lamido, técnica y adherencia.','M1'),
 ('04','Vida media y estado estable','Qué ocurre','La vida media describe la caída de concentración; el estado estable surge cuando entrada y eliminación se equilibran en dosis repetidas.','Aplicación','El momento de toma de muestras y la duración del efecto dependen del medicamento.','Verificar','Intervalo validado, función eliminadora y objetivo de monitoreo.','M1'),
 ('05','Unión a proteínas y distribución','Qué ocurre','La fracción libre atraviesa tejidos y ejerce efecto; cambios en proteínas plasmáticas pueden alterar la exposición libre.','Aplicación','Interpretar albúmina y condiciones críticas al evaluar medicamentos de alta unión proteica.','Verificar','Enfermedad concomitante y fármacos administrados al mismo tiempo.','M1'),
 ('06','Selección responsable de antimicrobianos','Qué ocurre','Un antibiótico se selecciona según diagnóstico, patógeno probable, sitio de infección, resultados de cultivo cuando corresponda y susceptibilidad.','Aplicación','Evitar antibióticos para cuadros sin evidencia de infección bacteriana. Reevaluar el plan con resultados y evolución.','Verificar','Necesidad real, toma de muestras, espectro, duración e impacto sobre resistencia.','A1'),
 ('07','Betalactámicos','Qué ocurre','Penicilinas y cefalosporinas actúan sobre la síntesis de pared bacteriana.','Aplicación','El espectro varía por molécula; no todos cubren el mismo patógeno ni alcanzan el mismo sitio.','Verificar','Antecedente de hipersensibilidad, cultivo cuando proceda y función renal según producto.','M3'),
 ('08','Tetraciclinas','Qué ocurre','Inhiben síntesis proteica bacteriana. Doxiciclina es un ejemplo conocido.','Aplicación','La indicación depende del agente y del paciente; la administración oral requiere atención específica en gatos.','Verificar','Formulación, instrucciones de administración, tolerancia gastrointestinal e interacciones.','M3'),
 ('09','Fluoroquinolonas','Qué ocurre','Interfieren en la replicación del ADN bacteriano.','Aplicación','Reservar su uso conforme a indicación y criterios de prudencia antimicrobiana.','Verificar','Especie, edad, comorbilidades, resistencia local y ficha técnica.','M3'),
 ('10','Aminoglucósidos','Qué ocurre','Actúan sobre el ribosoma y son especialmente relevantes frente a determinadas bacterias aerobias gramnegativas.','Aplicación','Su empleo exige considerar acceso al tejido y monitorización del paciente.','Verificar','Función renal, hidratación, riesgo de toxicidad y cultivo.','M3'),
 ('11','Sulfonamidas potenciadas','Qué ocurre','Bloquean pasos secuenciales de la síntesis de folato bacteriano.','Aplicación','La cobertura y la tolerancia dependen del producto y del paciente.','Verificar','Antecedentes de reacciones, hidratación, enfermedades concomitantes y seguimiento.','M3'),
 ('12','Antiinflamatorios no esteroideos','Qué ocurre','Los AINE reducen mediadores de inflamación y dolor. Sus beneficios deben sopesarse frente a riesgos digestivos, renales y hepáticos.','Aplicación','Evaluar historia, exploración y pruebas pertinentes; vigilar vómitos, diarrea, inapetencia y letargo.','Verificar','No combinar con otro AINE ni con corticoide sin un plan veterinario específico.','F1'),
 ('13','AINE en gatos','Qué ocurre','La seguridad depende de molécula, formulación y país. La etiqueta estadounidense de meloxicam advierte contra dosis repetidas en gatos.','Aplicación','No extrapolar aprobación canina a felina ni entre países.','Verificar','Registro local, indicación precisa, hidratación y seguimiento.','F2'),
 ('14','Glucocorticoides','Qué ocurre','Modulan múltiples vías inflamatorias e inmunitarias. Su perfil de riesgo depende de exposición y enfermedad.','Aplicación','Diferenciar objetivo antiinflamatorio de inmunosupresor y planificar seguimiento.','Verificar','Infección, diabetes, comorbilidades y uso simultáneo de AINE.','F1'),
 ('15','Analgesia multimodal','Qué ocurre','Combina enfoques que actúan sobre distintos mecanismos del dolor, con evaluación repetida de la respuesta.','Aplicación','El dolor se reconoce mediante comportamiento, examen y escalas apropiadas a la especie.','Verificar','Tipo de dolor, sedación, función orgánica y monitorización.','W1'),
 ('16','Anestésicos y sedantes','Qué ocurre','Sedación, analgesia y anestesia son objetivos diferentes; cada fármaco aporta perfiles distintos.','Aplicación','El protocolo se ajusta a paciente, procedimiento, vía aérea y recursos de monitorización.','Verificar','Evaluación preanestésica, monitoreo, recuperación y preparación ante complicaciones.','W1'),
 ('17','Antiparasitarios externos','Qué ocurre','Las familias incluyen lactonas macrocíclicas e isoxazolinas, entre otras; la selección depende del parásito y de la especie.','Aplicación','Confirmar diagnóstico y utilizar formulación indicada para el animal concreto.','Verificar','Especie, peso, edad, historial neurológico, exposición ambiental y etiqueta.','M8'),
 ('18','Antihelmínticos','Qué ocurre','Los fármacos pueden afectar estructura, metabolismo o función neuromuscular del parásito.','Aplicación','El diagnóstico coproparasitario y ciclo biológico orientan la selección y el control ambiental.','Verificar','Parásito diana, gestación, especie y producto registrado.','M8'),
 ('19','Antifúngicos','Qué ocurre','Las familias sistémicas incluyen azoles y polienos; las indicaciones cambian según hongo y sitio de infección.','Aplicación','Distinguir manejo tópico y sistémico; confirmar diagnóstico cuando sea posible.','Verificar','Función hepática, interacciones, duración y seguimiento.','M7'),
 ('20','Medicamentos gastrointestinales','Qué ocurre','Antieméticos, protectores y moduladores de motilidad tienen objetivos diferentes.','Aplicación','Identificar primero causa de vómitos o diarrea, hidratación y signos de obstrucción.','Verificar','Indicación exacta, interacción con absorción de otros fármacos y reevaluación.','M1'),
 ('21','Cardiovasculares','Qué ocurre','Diuréticos, moduladores neurohormonales e inotrópicos tienen acciones diferentes.','Aplicación','La elección se apoya en diagnóstico cardiovascular y evaluación seriada.','Verificar','Presión arterial, hidratación, electrolitos y función renal.','M5'),
 ('22','Endocrinos','Qué ocurre','Insulina y tratamientos tiroideos modifican sistemas de regulación con estrechos objetivos de seguimiento.','Aplicación','El monitoreo y la técnica de administración forman parte del tratamiento.','Verificar','Diagnóstico confirmado, alimentación, efectos adversos y datos de control.','M5'),
 ('23','Interacciones medicamentosas','Qué ocurre','Dos fármacos pueden alterar su exposición o sus efectos. También hay interacciones con alimentos y suplementos.','Aplicación','Conciliar todo lo que recibe el paciente antes de indicar nuevos tratamientos.','Verificar','Combinaciones de AINE y corticoides, duplicidad terapéutica y ficha técnica.','F1'),
 ('24','Seguridad entre especies','Qué ocurre','Un mismo principio activo puede tener registro, metabolismo y margen de seguridad diferentes en perro y gato.','Aplicación','Nunca convertir una indicación humana o canina en felina por simple cálculo de peso.','Verificar','Producto, especie, concentración, excipientes y regulaciones locales.','F2'),
]
story=cover('Atlas Visual de Farmacología Veterinaria','24 fichas de consulta conceptual para perros y gatos. Clases, mecanismos, aplicaciones y precauciones.','Kit Esencial · Material principal')
story += [p('Mapa de lectura','h1'),box('Fundamentos 01–05  |  Antimicrobianos 06–11  |  Dolor y anestesia 12–16  |  Parasitosis y hongos 17–19  |  Sistemas y seguridad 20–24'),Spacer(1,6*mm),p('Leyenda de la ficha','h2'),bullet('Qué ocurre: mecanismo o principio general.'),bullet('Aplicación: forma de pensar la elección clínica.'),bullet('Verificar: riesgos y datos que hay que confirmar.'),PageBreak()]
for n,title,a,b,c,d,e,f,key in atlas:
 story += [p(n+'  '+title,'h1'),box(b),*section(c,[d]),*section(e,[f]),Spacer(1,7*mm),p('Idea clave','h2'),box({'M1':'La exposición depende del paciente y de la formulación.','A1':'Primero confirmar que un antimicrobiano está indicado.','F1':'La vigilancia de eventos adversos forma parte de la analgesia.','F2':'La seguridad felina exige verificar la etiqueta específica.','W1':'Evaluar dolor y respuesta a lo largo del tiempo.'}.get(key,'Relaciona mecanismo, paciente y objetivo antes de elegir un fármaco.')),Spacer(1,8*mm),p('Lectura sugerida: '+key+' (referencia completa al final).','small'),PageBreak()]
story += [p('Lista de verificación antes de prescribir','h1'),*section('Paciente',['Especie, edad, peso actual, gestación, hidratación y comorbilidades.','Historia de alergias, tratamientos actuales y respuesta previa.']),*section('Producto',['Principio activo, formulación, concentración, vía y aprobación local.','Indicación, contraindicaciones, ajustes y plan de seguimiento.']),*section('Seguimiento',['Criterios de respuesta, señales de alarma y fecha de reevaluación.']),*refs(['M1','M2','M3','M7','M8','F1','F2','A1','W1'])]
build('01_Atlas_Visual_Farmacologia_Veterinaria',story)

questions=[
('¿Qué cuatro procesos resume ADME?',['Absorción, distribución, metabolismo y excreción','Acción, dosis, mecanismo y efecto','Análisis, diagnóstico, medicina y evolución'],'A','Describe farmacocinética, es decir, el recorrido del fármaco.','M1'),
('¿Qué estudia la farmacodinámica?',['El transporte del medicamento','La relación entre medicamento y efecto biológico','Solo la eliminación renal'],'B','Relaciona mecanismos, concentraciones y respuestas.','M2'),
('¿Qué debe verificarse antes de cambiar la vía de un producto?',['Solo el tamaño del envase','La equivalencia de etiqueta, formulación y biodisponibilidad','Solo el color de la solución'],'B','Las vías no son intercambiables por su nombre.','M1'),
('¿Qué acción favorece el uso prudente de antibióticos?',['Tratar cualquier fiebre sin investigar','Confirmar necesidad y obtener cultivo cuando corresponda','Elegir siempre el mayor espectro'],'B','Diagnóstico y cultivo orientan la selección.','A1'),
('¿Qué clase inhibe la síntesis de pared bacteriana?',['Betalactámicos','Azoles','AINE'],'A','Penicilinas y cefalosporinas son betalactámicos.','M3'),
('¿Qué clase interfiere con la replicación del ADN bacteriano?',['Fluoroquinolonas','Glucocorticoides','Polienos'],'A','Es una propiedad de las fluoroquinolonas.','M3'),
('¿Qué prueba resulta especialmente útil al investigar infección bacteriana seleccionada?',['Solo el peso','Cultivo y susceptibilidad, si están indicados','Solo el color del pelaje'],'B','La prueba ayuda a dirigir terapia.','A1'),
('Ante vómitos durante un AINE, ¿qué corresponde?',['Ignorarlos','Interrumpir y contactar al veterinario responsable','Añadir otro AINE'],'B','Los signos digestivos requieren reevaluación.','F1'),
('¿Cuál combinación exige evitar uso simultáneo sin plan veterinario?',['AINE y corticoide','Agua y alimento','Exploración y anamnesis'],'A','Aumenta el riesgo de daño.','F1'),
('¿Puede extrapolarse la pauta de un AINE canino a gatos?',['Sí, ajustando solo el peso','No, se verifica etiqueta específica y contexto','Sí, si el perro es pequeño'],'B','La aprobación y seguridad varían por especie.','F2'),
('¿Qué caracteriza la analgesia multimodal?',['Una única vía de acción','Combinación razonada de mecanismos y seguimiento','Evitar evaluación del dolor'],'B','La respuesta se reevalúa con instrumentos apropiados.','W1'),
('¿Qué diferencia sedación de analgesia?',['Son sinónimos','La sedación reduce alerta; analgesia aborda dolor','Analgesia significa inmovilidad'],'B','Sus objetivos clínicos son distintos.','W1'),
('¿Qué familia incluye algunos fármacos antiparasitarios externos?',['Lactonas macrocíclicas','Betalactámicos','Diuréticos'],'A','La elección depende de especie y producto.','M8'),
('¿Qué debe verificarse en un antiparasitario tópico?',['Especie autorizada y posible exposición por lamido','Solo precio','Solo olor'],'A','Formulación y especie importan.','M8'),
('¿Qué familia incluye fármacos antifúngicos sistémicos?',['Azoles','AINE','Fluoroquinolonas'],'A','Los azoles son una de las familias.','M7'),
('¿Por qué conciliar medicación actual?',['Para detectar duplicidades e interacciones','Para omitir la anamnesis','Para evitar seguimiento'],'A','Los otros tratamientos modifican riesgo y respuesta.','F1'),
('¿Qué se considera antes de interpretar un valor de laboratorio?',['Intervalo de referencia del laboratorio, especie y contexto','Un valor aislado sin historia','Solo el nombre del analito'],'A','Los resultados no se interpretan aislados.','M5'),
('¿Cuál es una función del urianálisis?',['Apoyar la evaluación urinaria','Confirmar por sí solo toda enfermedad','Sustituir la exploración'],'A','Se integra con examen y otras pruebas.','M6'),
('¿Cuál parámetro acompaña la evaluación de un fármaco con riesgo renal?',['Hidratación y función renal','Color de collar','Longitud del nombre'],'A','Factores del paciente modifican seguridad.','F1'),
('¿Qué se hace si el paciente no responde como se esperaba?',['Reevaluar diagnóstico, adherencia y plan','Aumentar dosis sin revisar','Mantener indefinidamente sin consulta'],'A','La respuesta guía la reevaluación clínica.','A1'),
]
story=cover('Quiz de Farmacología Veterinaria','20 preguntas de revisión con respuestas comentadas y fuentes.','Kit Esencial · Material de práctica')
for start in (0,10):
 story += [p('Preguntas '+str(start+1)+' a '+str(start+10),'h1')]
 for i,(q,opts,ans,why,key) in enumerate(questions[start:start+10],start+1):
  story += [p(str(i)+'. '+q,'h2')]+[p(chr(65+j)+'. '+o,'body') for j,o in enumerate(opts)]
 story += [PageBreak()]
for start in (0,10):
 story += [p('Respuestas '+str(start+1)+' a '+str(start+10),'h1')]
 for i,(q,opts,ans,why,key) in enumerate(questions[start:start+10],start+1):story += [rich('<b>'+str(i)+'. '+ans+'</b>  '+escape(why)+' <font color="#33786A">['+key+']</font>')]
 story += [PageBreak()]
story+=refs(['M1','M2','M3','M5','M6','M7','M8','F1','F2','A1','W1'])
build('02_Quiz_Farmacologia_Veterinaria',story)

lab=[
('Muestra y contexto','Antes de interpretar',['Identificar paciente, especie, fecha, hora, ayuno, tratamientos y motivo de solicitud.','Confirmar tubo, anticoagulante, técnica de recolección y condiciones de transporte.','Registrar hemólisis, lipemia, coágulos o demora de procesamiento como posibles fuentes de error.'],'Una anomalía preanalítica puede distorsionar la interpretación.'),
('Hemograma','Tres compartimentos',['Serie roja: hematocrito, hemoglobina, eritrocitos, índices y morfología.','Serie blanca: recuento total, diferencial, cambios morfológicos y correlación con clínica.','Plaquetas: recuento, estimación en frotis y agregación, particularmente importante en gatos.'],'Nunca interpretarlo solo por una cifra aislada.'),
('Serie roja','Preguntas clave',['¿Existe anemia o eritrocitosis frente al intervalo local?','Si hay anemia: ¿hay respuesta regenerativa? Solicitar o revisar reticulocitos según especie y laboratorio.','Comparar índices y frotis con sangrado, hemólisis y enfermedad crónica como hipótesis.'],'La interpretación requiere cronología y examen físico.'),
('Serie blanca','Patrones antes que etiquetas',['Revisar neutrófilos, linfocitos, monocitos, eosinófilos y basófilos, incluyendo cambios tóxicos.','Estrés, inflamación, infección y medicamentos pueden influir en el patrón.','Un patrón sugiere diferenciales; no identifica por sí solo un patógeno.'],'Evitar convertir leucocitosis en diagnóstico automático de infección.'),
('Plaquetas','Recuento y frotis',['Confirmar agregados plaquetarios en el frotis cuando el analizador informa valor bajo.','Relacionar recuento con sangrado, medicamentos y enfermedades concomitantes.','Considerar repetición de muestra si hay problema preanalítico.'],'La agregación puede simular trombocitopenia.'),
('Bioquímica','Órganos y función',['Agrupar analitos por procesos: riñón, hígado, proteínas, metabolismo y electrolitos.','Distinguir lesión celular, colestasis y función; un marcador aislado rara vez determina causa.','Revisar tendencias y coherencia con historia, examen y urianálisis.'],'Los intervalos de referencia cambian con laboratorio y método.'),
('Urianálisis','Cuatro capas',['Método de obtención y tiempo hasta procesar.','Aspecto y densidad urinaria según contexto.','Tira química interpretada junto con sedimento y, cuando proceda, cultivo.','Comparar con bioquímica y estado de hidratación.'],'La contaminación depende del método de toma y altera conclusiones.'),
('Integración clínica','Cerrar el ciclo',['Escribir hallazgos confirmados, diferenciales y vacíos de información.','Priorizar pruebas adicionales solo si pueden cambiar decisiones.','Definir comunicación de resultados y fecha de reevaluación.'],'Documentar incertidumbre es parte de una interpretación responsable.'),
]
story=cover('Guía Visual de Laboratorio Veterinario','Ruta de lectura para hemograma, bioquímica y urianálisis en perros y gatos.','Kit Profesional · Material principal')
for title,sub,items,key in lab:story += [p(title,'h1'),p(sub,'subtitle'),*map(bullet,items),Spacer(1,6*mm),box('Recuerda: '+key),PageBreak()]
story+=refs(['M4','M5','M6']);build('03_Guia_Visual_Laboratorio_Veterinario',story)

interpret=[
('Hematocrito bajo','Confirmar muestra y comparar con hemoglobina y recuento; evaluar hidratación, reticulocitos y frotis.','Preguntar por signos de sangrado, pigmenturia, ictericia y enfermedades crónicas.','Anemia es un hallazgo; la causa exige investigación.'),
('Leucocitos alterados','Revisar diferencial absoluto, frotis y cambios tóxicos; relacionar con fiebre, estrés y medicamentos.','Considerar repetición si calidad de muestra o patrón no concuerdan.','Un aumento no confirma por sí solo infección bacteriana.'),
('Plaquetas bajas','Inspeccionar frotis por agregados, especialmente en gatos; correlacionar con sangrado clínico.','Confirmar el resultado antes de atribuir trombocitopenia verdadera.','La cifra automatizada puede ser falsamente baja.'),
('Urea y creatinina elevadas','Integrar hidratación, densidad urinaria, historia, masa muscular y evolución temporal.','Buscar signos urinarios y evaluar necesidad de imágenes u otras pruebas.','Un analito elevado aislado no clasifica enfermedad renal.'),
('Enzimas hepáticas alteradas','Distinguir indicadores de lesión y colestasis de pruebas de función; revisar fármacos y patrón de otros analitos.','Comparar con signos, imagen y evolución.','No atribuir una causa específica solo por una enzima.'),
('Albúmina baja','Valorar pérdidas, síntesis, dilución e inflamación según historia y pruebas complementarias.','Cruzar con proteínas totales, urianálisis y aparato digestivo.','Puede modificar interpretación de ciertos fármacos.'),
('Glucosa alterada','Verificar estrés, ayuno, tratamiento y procesamiento de la muestra.','Relacionar con signos clínicos y análisis repetidos según criterio profesional.','Especial atención a cambios por estrés en gatos.'),
('Densidad y sedimento urinario','Considerar método de toma, hidratación y tiempo de procesamiento.','Integrar densidad, tira y microscopia; indicar cultivo cuando sea pertinente.','La interpretación de proteína requiere contexto del sedimento.'),
]
story=cover('Guía de Interpretación de Exámenes','Ocho rutas de razonamiento: del resultado alterado a las preguntas clínicas.','Kit Profesional · Material principal')
for title,first,second,tip in interpret:story += [p(title,'h1'),*section('Paso 1 · Confirmar',[first]),*section('Paso 2 · Contextualizar',[second]),Spacer(1,7*mm),box('Evita este salto: '+tip),PageBreak()]
story += [p('Plantilla de interpretación','h1'),*section('Registrar',['Hallazgo y unidades: ________________________________','Intervalo de referencia del laboratorio: __________________','Calidad de muestra y método: __________________________','Hallazgos clínicos compatibles o discordantes: __________','Diferenciales priorizados: _____________________________','Próximo dato que puede cambiar la decisión: ___________']),*refs(['M4','M5','M6'])]
build('04_Guia_Interpretacion_Examenes_Veterinarios',story)

cases=[
('Perro con cojera y dolor','Exploración, localización del dolor, capacidad para apoyar, trauma y signos sistémicos.','Analgesia individualizada; verificar hidratación, medicación previa y factores de riesgo antes de considerar AINE.','¿Qué criterios exigen imagen o derivación? ¿Qué escala de dolor y fecha de control registrar?','W1','F1'),
('Gato con vómitos','Cronología, frecuencia, ingestión posible, hidratación, dolor, micción y medicación.','Priorizar valoración de obstrucción, toxinas y estado de hidratación antes de medicación sintomática.','¿Qué hallazgos obligan a atención urgente? ¿Qué muestras o imagen cambiarían conducta?','M5','M6'),
('Perro con prurito y lesiones cutáneas','Distribución, pulgas, estacionalidad, citología, raspado y exposiciones.','Identificar causa antes de antimicrobianos; antiparasitarios dependen del diagnóstico y producto específico.','¿Hay infección secundaria documentada? ¿Se necesita cultivo?','A1','M8'),
('Gato con signos urinarios','Frecuencia, esfuerzo, dolor, producción de orina, vejiga palpable y estado general.','La imposibilidad de orinar exige evaluación veterinaria urgente. Interpretar urianálisis según toma y sedimento.','¿Existe obstrucción? ¿Cuándo corresponde cultivo?','M6','M5'),
('Perro con fiebre y lesión infectada sospechada','Examen, citología o muestra apropiada, antecedentes de tratamientos y evolución.','Valorar control de foco y necesidad real de antibiótico; considerar cultivo antes de tratamiento en casos indicados.','¿Qué signos indican urgencia? ¿Cómo se documentará respuesta?','A1','M3'),
('Paciente con enzimas hepáticas elevadas','Historia, síntomas, medicamentos, patrón bioquímico y evolución.','Revisar si el tratamiento actual puede influir y qué pruebas distinguen lesión de disfunción.','¿Es alteración persistente? ¿Qué criterio exige imagen o prueba adicional?','M5','M7'),
('Perro con poliuria y polidipsia','Ingesta, micción, peso, apetito, examen y tratamientos actuales.','Combinar bioquímica, urianálisis y hallazgos clínicos para orientar diferenciales.','¿Qué patrones apoyan causa renal o endocrina?','M5','M6'),
('Gato que recibía AINE y deja de comer','Producto, concentración, dosis realmente administrada, cronología, vómitos y estado general.','Suspender nuevas administraciones y contactar de inmediato con el veterinario; evaluar riesgos conforme al producto.','¿Qué etiqueta local corresponde? ¿Qué plan de monitorización se indica?','F2','F1'),
]
story=cover('Fichas Clínicas Veterinarias','Ocho escenarios de discusión guiada. Preguntas, prioridades y seguimiento, sin pautas de prescripción.','Kit Profesional · Material principal')
for i,(title,assess,priority,qs,k1,k2) in enumerate(cases,1):story += [p(str(i).zfill(2)+'  '+title,'h1'),*section('Datos a reunir',[assess]),*section('Prioridad de razonamiento',[priority]),*section('Preguntas para discusión',[qs]),Spacer(1,6*mm),box('Ficha para estudiante: escribe 3 diferenciales, 1 dato decisivo y 1 criterio de reevaluación.'),Spacer(1,8*mm),p('Referencias: '+k1+', '+k2+'.','small'),PageBreak()]
story+=refs(['W1','F1','F2','M3','M5','M6','M7','M8','A1']);build('05_Fichas_Clinicas_Veterinarias',story)

story=cover('Método SOAP Veterinario','Guía y plantillas para documentar anamnesis, hallazgos, evaluación y plan.','Kit Profesional · Material principal')
story += [p('La estructura SOAP','h1'),*section('S · Subjetivo',['Motivo de consulta y relato del tutor; cronología, apetito, ingesta de agua, eliminación, comportamiento y tratamientos previos.','Separar lo informado por el tutor de lo observado en consulta.']),*section('O · Objetivo',['Constantes, peso, exploración, pruebas y observaciones verificables.','Anotar unidades, intervalos y calidad de muestras cuando proceda.']),*section('A · Análisis',['Lista de problemas, diferenciales, grado de certeza y relación entre datos.','No escribir un diagnóstico definitivo cuando faltan pruebas.']),*section('P · Plan',['Pruebas, tratamiento definido por el veterinario, comunicación con tutor, seguimiento y señales de alarma.','Registrar instrucciones reales y responsable de cada paso.']),PageBreak()]
for i,(species,reason) in enumerate([('Perro','Dolor musculoesquelético'),('Gato','Signos urinarios'),('Perro','Prurito'),('Gato','Vómitos')],1):
 story += [p('Ejercicio '+str(i)+' · '+reason,'h1'),p('Paciente: '+species+' | Situación simulada para práctica documental.','subtitle'),*section('S · Escribe el relato',['Motivo y cronología: ____________________________________________','Información adicional a preguntar: ____________________________']),*section('O · Registra datos medidos',['Exploración: _________________________________________________','Pruebas y unidades: ___________________________________________']),*section('A · Sintetiza',['Problemas: __________________________________________________','Diferenciales y grado de certeza: _____________________________']),*section('P · Define seguimiento',['Prueba que puede cambiar la decisión: _______________________','Responsable y fecha de reevaluación: __________________________','Señales de alarma comunicadas al tutor: ______________________']),PageBreak()]
story += [p('Ejemplo breve: documentación sin suposiciones','h1'),box('S: Tutor informa que el perro cojea desde ayer tras paseo. O: No se registran aún examen ortopédico ni constantes. A: Cojera aguda; origen no determinado. P: Completar examen y valorar analgesia individualizada después de revisar antecedentes y riesgos. Registrar instrucciones y control.'),Spacer(1,8*mm),p('Antes de cerrar la nota','h2'),*map(bullet,['¿La especie, el peso y la fecha son correctos?','¿Se distingue dato reportado de dato observado?','¿Hay unidades y fuente de cada resultado?','¿El plan incluye seguimiento y señales para consultar?']),*refs(['M4','M5','M6','W1'])]
build('06_Metodo_SOAP_Veterinario',story)
