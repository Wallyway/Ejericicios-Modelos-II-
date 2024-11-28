from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyswip import Prolog

app = FastAPI()

# Cargar el archivo Prolog
prolog = Prolog()
prolog.consult("nomina.pl")

# Modelo de solicitud para agregar un nuevo docente
class NuevoDocente(BaseModel):
    nombre: str
    categoria: str

# Endpoint para agregar un nuevo docente
@app.post("/agregar_docente/")
def agregar_docente(docente: NuevoDocente):
    nombre_docente = docente.nombre.lower()
    categoria = docente.categoria.lower()

    # Verificamos que la categoría sea válida
    if categoria not in ["auxiliar", "asociado", "titular"]:
        raise HTTPException(status_code=400, detail="Categoría inválida. Debe ser 'auxiliar', 'asociado' o 'titular'.")

    # Agregar el docente a Prolog
    try:
        # Comprobamos si el docente ya existe para evitar duplicados
        consulta = f"docente({nombre_docente}, {categoria})".lower()  # Comprobamos por nombre y categoría
        existe = list(prolog.query(consulta))
        
        if existe:
            raise HTTPException(status_code=400, detail="El docente ya existe en la base de datos.")
        
        # Usamos assertz para agregar el hecho dinámico
        comando = f"assertz(docente({nombre_docente}, {categoria}))".lower()  # Solo se pasa nombre y categoría
        list(prolog.query(comando))
        
        return {"message": f"Docente {nombre_docente} agregado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Modelo de solicitud para cálculo de nómina
class Docente(BaseModel):
    nombre: str

# Endpoint para obtener el salario neto
@app.post("/calculo_nomina/")
def calculo_nomina(docente: Docente):
    nombre_docente = docente.nombre.lower()  # Convertir a minúsculas para coincidir
    try:
        # Consulta en Prolog para obtener el salario neto
        query = f"salario_neto({nombre_docente}, SalarioNeto)"
        result = list(prolog.query(query))
        
        if result:
            salario_neto = result[0]["SalarioNeto"]
            return {"nombre": nombre_docente, "salario_neto": salario_neto}
        else:
            raise HTTPException(status_code=404, detail="Docente no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ejemplo de inicialización
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
