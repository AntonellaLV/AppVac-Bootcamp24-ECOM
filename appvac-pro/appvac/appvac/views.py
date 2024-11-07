from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Proyecto
from .forms import ContactForm

def index(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda de los parámetros GET
    if query:
        # Filtrar proyectos por título que contengan el término de búsqueda (no distingue entre mayúsculas y minúsculas)
        proyectos_list = Proyecto.objects.filter(titulo__icontains=query)
    else:
        # Obtener todos los proyectos si no hay término de búsqueda
        proyectos_list = Proyecto.objects.all()

    paginator = Paginator(proyectos_list, 10)  # Paginación, 10 proyectos por página
    page_number = request.GET.get('page')  # Obtener el número de página actual de los parámetros GET
    proyectos = paginator.get_page(page_number)  # Obtener la página actual de proyectos
    return render(request, 'portafolio/index.html', {'proyectos': proyectos})  # Renderizar la plantilla con los proyectos

def contacto(request):
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos enviados
        form = ContactForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            # Enviar correo electrónico usando send_mail
            send_mail(
                f"Mensaje de {nombre}",
                mensaje,
                email,
                ['tuemail@example.com'],  # Cambia esto a tu dirección de correo
                fail_silently=False,
            )
            # Mostrar mensaje de éxito
            messages.success(request, '¡Mensaje enviado exitosamente!')
            # Redirigir a la misma página de contacto
            return redirect('contacto')
    else:
        # Crear una instancia vacía del formulario si no se ha enviado un formulario
        form = ContactForm()

    # Renderizar la plantilla contacto.html con el formulario
    return render(request, 'portafolio/contacto.html', {'form': form})
