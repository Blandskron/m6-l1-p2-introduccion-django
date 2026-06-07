from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
import sys

def dashboard(request):
    """Vista del dashboard principal con descripción de Django y su utilidad empresarial."""
    context = {
        'title': 'Introducción a Django',
        'active_page': 'dashboard',
    }
    return render(request, 'leccion1/dashboard.html', context)

def python_vs_django(request):
    """Vista para comparar tareas web en Python puro vs Django."""
    context = {
        'title': 'Python Puro v/s Django',
        'active_page': 'python_vs_django',
    }
    return render(request, 'leccion1/python_vs_django.html', context)

def virtual_envs(request):
    """Vista para explicar entornos virtuales."""
    context = {
        'title': 'Entornos Virtuales',
        'active_page': 'virtual_envs',
        'python_version': sys.version,
    }
    return render(request, 'leccion1/virtual_env.html', context)

def mvc_dry(request):
    """Vista para explicar MVC (MVT), DRY y el motor de plantillas, con un playground interactivo."""
    # Valores por defecto para el playground
    nombre = 'Usuario'
    nota = '6.5'
    frameworks_str = 'Django, Flask, FastAPI, Python Sockets'
    template_code = """<h3>Hola {{ nombre }}!</h3>
{% if nota >= 4.0 %}
    <p class="badge-success">🎉 Has aprobado el módulo con nota {{ nota }}.</p>
{% else %}
    <p class="badge-danger">⚠️ Reprobado. Tu nota es {{ nota }}.</p>
{% endif %}

<p>Tus herramientas del ecosistema Python:</p>
<ul>
{% for fw in frameworks %}
    <li>🐍 {{ fw }}</li>
{% empty %}
    <li>No se ingresaron frameworks.</li>
{% endfor %}
</ul>"""
    rendered_output = ""
    error_message = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre', nombre)
        nota = request.POST.get('nota', nota)
        frameworks_str = request.POST.get('frameworks', frameworks_str)
        template_code = request.POST.get('template_code', template_code)
        
        # Intentamos renderizar usando el motor de plantillas de Django
        try:
            # Validamos y convertimos nota a float
            try:
                nota_val = float(nota)
            except ValueError:
                nota_val = 0.0

            frameworks_list = [f.strip() for f in frameworks_str.split(',') if f.strip()]
            
            t = Template(template_code)
            c = Context({
                'nombre': nombre,
                'nota': nota_val,
                'frameworks': frameworks_list,
            })
            rendered_output = t.render(c)
        except Exception as e:
            error_message = str(e)
            rendered_output = f"<div class='error-msg'><strong>Error de compilación de Django Template:</strong><br>{e}</div>"

    context = {
        'title': 'MVC/MTV, DRY y Templates',
        'active_page': 'mvc_dry',
        'nombre': nombre,
        'nota': nota,
        'frameworks': frameworks_str,
        'template_code': template_code,
        'rendered_output': rendered_output,
        'error_message': error_message,
    }
    return render(request, 'leccion1/mvc_dry.html', context)

def router_db(request):
    """Vista para explicar el enrutador de Django y soporte de base de datos."""
    context = {
        'title': 'Enrutador y Bases de Datos',
        'active_page': 'router_db',
    }
    return render(request, 'leccion1/router_db.html', context)

def dev_vs_prod(request):
    """Vista para explicar la diferencia de configuración entre desarrollo y producción."""
    context = {
        'title': 'Desarrollo v/s Producción',
        'active_page': 'dev_vs_prod',
    }
    return render(request, 'leccion1/dev_vs_prod.html', context)
