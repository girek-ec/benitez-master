

def Attr(cls):
    """Extrae una lista de atributos desde la docstring del modelo.

    Formato esperado (ejemplo):
        "MyModel(id, nombre, activo)"

    Si no hay docstring, devuelve lista vacía para evitar excepciones.
    """
    model = cls.__name__
    doc = cls.__doc__ or ""
    # eliminar el nombre del modelo y paréntesis
    cleaned = doc.replace(model, "").replace("(", "").replace(")", "")
    # crear lista de campos, ignorando entradas vacías
    fields = [p.strip() for p in cleaned.split(',') if p.strip()]
    return fields
