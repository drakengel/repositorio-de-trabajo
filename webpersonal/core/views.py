from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<url>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</url>
"""


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return HttpResponse(html_base + """
                        <h1>Mi Persona</h1>
                        <h2>Acerca de</h2>
                        <p>Me llamo William y Soy Programador Backend</p>""")

def portafolio(request):
    return HttpResponse(html_base + """
                        <h1>Trabajos</h1>
                        <h2>Mis trabajos Realizados</h2>
                        <p>Aqui puedes ver mis trabajos Realizados</p>""")

def contact(request):
    return HttpResponse(html_base + """
                        <h1> Contacto Personal </h1>
                        <h2> Correo para Consultas y Dudas </h2> 
                        <p> Puedes contactarme al correo: <a href="mailto:william.jesus.leo@gmail.com">Contactame</a> </p>""" 
                        )
#mailto: Sirve para crear un enlace de correo electrónico