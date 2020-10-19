---
layout: page
title: Sobre el Proyecto
subtitle: Estimación Rt para República Dominicana

---
<p align="justify">
 La Tasa de Reproducción R<sub>0</sub> es la cantidad de personas que un individuo infectado por un virus contagia. Si se encuentra por encima de 1 quiere decir que el esparcimiento del virus se mantendrá en crecimiento, si se encuentra por debajo de 1 significa que el esparcimiento estará en disminución y eventualmente el virus desaparecerá.
 </p>
 
 <p align="justify">
 En esta página se presenta la Tasa de Reproducción Efectiva (R<sub>e(t)</sub>), la cual se define como una estimación instantánea <i>nowcast</i> de cómo se comporta la Tasa de Reproducción en el día <i>t</i>. Es decir, estima que si un individuo se infecta en el día <i>t</i> contagiará a R<sub>e(t)</sub> cantidad de personas.
  </p>
  
 <p align="justify">
Al tratarse de una estimación instantánea, existe una mayor probabilidad de error mientras <i>t</i> se encuentre más cerca de la fecha actual, mientras más se aleja y nuevos datos se publican, más precisa se vuelve la estimación. Por esta razón, el cambio entre los intervalos de confianza entre las figuras de la página principal. De igual forma, se debe tener en cuenta la sensabilidad de las últimas estimaciones ante las publicaciones más recientes de los boletines epidemiológicos del Ministerio de Salud. Para dudas de interpretación, los desarrolladores del modelo facilitan esta <a href="https://rt.live/faq">página de preguntas y respuestas</a>
 </p>

### Modelo Utilizado
<p align="justify">
Se utiliza el modelo generativo desarrollado por Kevin Systrom y Thomas Vladek que potencia <a href="https://rt.live">rt.live</a>. Utiliza el número de pruebas procesadas diarias y la cantidad de positivos para inferir la curva R<sub>e(t)</sub> que mejor se ajusta al comportamiento de los datos. El  <a href="https://github.com/rtcovidlive/covid-model/blob/master/tutorial.ipynb">tutorial</a> realizado por los autores explica la intuición y supuestos detrás del modelo. Los datos son extraídos de <a href="https://github.com/gcaff/COVID19-RD/tree/master/data">Gustavo Caffaro y Michell Payano</a>.
 </p>
 
 ## Referencias
 Caffaro, G. and Payano, M. (2020). Base de datos covid rd. https://github.com/gcaff/COVID19-RD

 Systrom, K., Vladek, T., and Krieger, M. (2020).   Rt live. https://github.com/rtcovidlive/covid-model.


 
