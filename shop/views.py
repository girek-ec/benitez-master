from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from shop.models import (
    BlogColexin,
    CategoriaBlogColexin,
    Category,
    Marca,
    Product,
)
def index_colexin(request):
    contexto ={
        'marca': Marca.objects.all().first(),
        'categories': Category.objects.all(),
        'products': Product.objects.all().order_by('-id'),
    }
    return render(request, 'colexin/demo-decor-store.html', contexto)

def productos_colexin(request):
    products = Product.objects.all() # Filtra productos por categoría

    query = request.GET.get('q')  # Obtiene el término de búsqueda de la URL
    if query:
        products = products.filter(name__icontains=query)  #  productos que contengan el término de búsqueda

    contexto = {
        'marca': Marca.objects.all().first(),
        'categories': Category.objects.all(),
        'products': products,
        'query': query,  # Para mantener el valor en la barra de búsqueda
    }
    return render(request, 'colexin/demo-decor-store-products.html', contexto)




def productos_cate_colexin(request, cate):
    category = get_object_or_404(Category, name=cate)  # Obtiene la categoría o muestra 404 si no existe
    products = Product.objects.filter(category=category)  # Filtra productos por categoría

    query = request.GET.get('q')  # Obtiene el término de búsqueda de la URL
    if query:
        products = products.filter(name__icontains=query)  # Filtra productos que contengan el término de búsqueda

    contexto = {
        'marca': Marca.objects.all().first(),
        'categories': Category.objects.all(),
        'category': category,
        'products': products,
        'query': query,  # Para mantener el valor en la barra de búsqueda
    }
    return render(request, 'colexin/demo-decor-store-products_cate.html', contexto)

def producto_id_colexin(request, n):
    product = Product.objects.get(id=n)
    contexto = {
        'marca': Marca.objects.all().first(),
        'categorias': Category.objects.all(),
        'categories': Category.objects.all(),
        'product': Product.objects.get(id=n),
    }
    return render(request, 'colexin/demo-decor-store-single-product.html', contexto)
def blog_colexin(request, categoria_slug=None):
    fecha_actual = timezone.now()

    publicaciones = (
        BlogColexin.objects.filter(
            activo=True,
            categoria__activo=True,
            fecha_publicacion__lte=fecha_actual,
        )
        .select_related("categoria")
        .order_by("-fecha_publicacion")
    )

    categoria_actual = None

    if categoria_slug:
        categoria_actual = get_object_or_404(
            CategoriaBlogColexin,
            slug=categoria_slug,
            activo=True,
        )

        publicaciones = publicaciones.filter(
            categoria=categoria_actual
        )

    categorias_blog = (
        CategoriaBlogColexin.objects.filter(activo=True)
        .annotate(
            total_publicaciones=Count(
                "publicaciones_colexin",
                filter=Q(
                    publicaciones_colexin__activo=True,
                    publicaciones_colexin__fecha_publicacion__lte=fecha_actual,
                ),
            )
        )
        .filter(total_publicaciones__gt=0)
        .order_by("nombre")
    )

    pagina = Paginator(publicaciones, 8).get_page(
        request.GET.get("page")
    )

    contexto = {
        "marca": Marca.objects.first(),
        "categories": Category.objects.all(),
        "publicaciones": pagina,
        "categorias_blog": categorias_blog,
        "categoria_actual": categoria_actual,
    }

    return render(
        request,
        "colexin/blog_lista_colexin.html",
        contexto,
    )


def blog_detalle_colexin(request, slug):
    fecha_actual = timezone.now()

    publicacion = get_object_or_404(
        BlogColexin.objects
        .select_related("categoria")
        .prefetch_related("galeria"),
        slug=slug,
        activo=True,
        categoria__activo=True,
        fecha_publicacion__lte=fecha_actual,
    )

    relacionados = (
        BlogColexin.objects.filter(
            activo=True,
            categoria__activo=True,
            categoria=publicacion.categoria,
            fecha_publicacion__lte=fecha_actual,
        )
        .exclude(pk=publicacion.pk)
        .select_related("categoria")
        .order_by("-fecha_publicacion")[:3]
    )

    contexto = {
        "marca": Marca.objects.first(),
        "categories": Category.objects.all(),
        "publicacion": publicacion,
        "relacionados": relacionados,
    }

    return render(
        request,
        "colexin/blog_detalle_colexin.html",
        contexto,
    )