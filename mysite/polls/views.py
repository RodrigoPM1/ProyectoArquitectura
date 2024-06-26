from django.shortcuts import render, get_object_or_404, redirect
from .models import Biblioteca, Libro
from .forms import BibliotecaForm, LibroForm

# Listar bibliotecas
def listar_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, "listar_bibliotecas.html", {"bibliotecas": bibliotecas})

# Buscar biblioteca por nombre
def buscar_biblioteca_por_nombre(request, nombre):
    bibliotecas = Biblioteca.objects.filter(nombre__icontains=nombre)
    return render(request, "listar_bibliotecas.html", {'bibliotecas': bibliotecas})

# Buscar bibliotecas por ciudad
def buscar_bibliotecas_por_ciudad(request, ciudad):
    bibliotecas = Biblioteca.objects.filter(ciudad__icontains=ciudad)
    return render(request, 'listar_bibliotecas.html', {'bibliotecas': bibliotecas})

# Listar libros de una biblioteca
def listar_libros_de_biblioteca(request, nombre):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    libros = Libro.objects.filter(biblioteca=biblioteca)
    return render(request, 'listar_libros.html', {'libros': libros, 'biblioteca': biblioteca})

# Buscar libro por título y nombre de una biblioteca
def buscar_libro_por_titulo_en_biblioteca(request, nombre, titulo):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    libros = Libro.objects.filter(titulo__icontains=titulo, biblioteca=biblioteca)
    return render(request, 'listar_libros.html', {'libros': libros, 'biblioteca': biblioteca})

# Buscar libro por autor y nombre de una biblioteca
def buscar_libro_por_autor_en_biblioteca(request, nombre, autor):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    libros = Libro.objects.filter(autor__icontains=autor, biblioteca=biblioteca)
    return render(request, 'listar_libros.html', {'libros': libros, 'biblioteca': biblioteca})

# Buscar libro por editorial y nombre de una biblioteca
def buscar_libro_por_editorial_en_biblioteca(request, editorial, nombre):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    libros = Libro.objects.filter(editorial__icontains=editorial, biblioteca=biblioteca)
    return render(request, 'listar_libros.html', {'libros': libros, 'biblioteca': biblioteca})

# Buscar libro por título
def buscar_libro_por_titulo(request, titulo):
    libros = Libro.objects.filter(titulo__icontains=titulo)
    return render(request, 'listar_libros.html', {'libros': libros})

# Buscar libro por título y disponibilidad
def buscar_libro_por_titulo_y_disponibilidad(request, titulo):
    libros = Libro.objects.filter(titulo__icontains=titulo, num_ejemplares__gt=0)
    bibliotecas_disponibles = {libro.biblioteca for libro in libros}
    return render(request, 'listar_libros.html', {'libros': libros, 'bibliotecas_disponibles': bibliotecas_disponibles})

# Añadir nueva biblioteca
def nueva_biblioteca(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = BibliotecaForm()
    return render(request, 'nueva_biblioteca.html', {'form': form})

# Añadir nuevo libro
def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros_de_biblioteca', nombre=form.cleaned_data['biblioteca'].nombre)
    else:
        form = LibroForm()
    return render(request, 'nuevo_libro.html', {'form': form})

# Editar biblioteca
def editar_biblioteca(request, nombre):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, request.FILES, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = BibliotecaForm(instance=biblioteca)
    return render(request, 'editar_biblioteca.html', {'form': form, 'biblioteca': biblioteca})

# Editar libro
def editar_libro(request, titulo):
    libro = get_object_or_404(Libro, titulo=titulo)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros_de_biblioteca', nombre=libro.biblioteca.nombre)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form, 'libro': libro})

# Borrar biblioteca
def eliminar_biblioteca(request, nombre):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    if request.method == 'POST':
        biblioteca.delete()
        return redirect('listar_bibliotecas')
    return render(request, 'eliminar_biblioteca.html', {'biblioteca': biblioteca})

# Borrar libro
def eliminar_libro(request, nombre, titulo):
    biblioteca = get_object_or_404(Biblioteca, nombre=nombre)
    libro = get_object_or_404(Libro, titulo=titulo, biblioteca=biblioteca)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros_de_biblioteca', nombre=nombre)
    return render(request, 'eliminar_libro.html', {'libro': libro, 'biblioteca': biblioteca})
