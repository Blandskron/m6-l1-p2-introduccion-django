# 🐍 M6-L1 — Introducción a Django y Entorno de Desarrollo

¡Bienvenido a la plataforma educativa interactiva de **Django (Módulo 6 - Lección 1)**!

Este repositorio ha sido diseñado y transformado para servir como una guía teórico-práctica completa e interactiva. En lugar de ser un proyecto vacío, implementa una aplicación web Django con diseño premium que expone y demuestra en tiempo real todos los conceptos fundamentales del framework.

---

## 📚 Temas de la Lección 1 Cubiertos al 100%

1. **Introducción a Django:** Qué es, sus características fundamentales, utilidad en proyectos empresariales y flexibilidad de instalación.
2. **Entornos Virtuales en Python (`venv`):** Aislamiento de entornos, uso e inicio con el comando `venv`, activación/desactivación y manejo de librerías locales por proyecto.
3. **Python Puro v/s Django Integrado:** Comparativa detallada de sockets TCP frente a la abstracción de alto nivel de Django.
4. **Estructura Web y Bases de Datos:** El funcionamiento del ORM de Django, motores relacionales (SQLite en desarrollo vs PostgreSQL/MySQL en producción).
5. **El Enrutador de Django:** Mapeo de rutas dinámicas y estáticas mediante `urls.py`.
6. **Arquitectura MVC / MTV:** Modelo, Vista y Plantilla (Template), uso del principio **DRY (Don't Repeat Yourself)** y herencia de componentes HTML.
7. **Entornos de Desarrollo v/s Producción:** Configuración crítica de seguridad de variables como `DEBUG`, `ALLOWED_HOSTS`, `SECRET_KEY` y carga de archivos estáticos.

---

## 🎮 Características Interactivas de la Aplicación

La aplicación web cuenta con las siguientes herramientas dinámicas creadas en Javascript y Django Server-Side:
- **Simulador de Terminal de Entornos Virtuales:** Ejecuta comandos interactivos de `venv` paso a paso y visualiza gráficamente qué ocurre en los site-packages y variables del sistema.
- **Comparador de Código:** Visualiza de forma paralela la implementación de un socket HTTP en Python puro contra las vistas/rutas limpias de Django.
- **Simulador de Ciclo Request-Response:** Ejecuta una animación que ilustra cómo viaja una petición desde el navegador y cómo la procesa el enrutador y la vista de Django.
- **Visualizador del Enrutador (URL Resolver):** Introduce una URL y observa en tiempo real cómo Django busca coincidencias en `urls.py` hasta resolver qué vista llamar.
- **Playground de Plantillas Django (DTL):** Escribe código con sintaxis de plantillas (variables `{{ nombre }}`, condicionales `{% if %}`, bucles `{% for %}`) y observa el resultado HTML renderizado directamente por el motor del servidor Django.

---

## 🚀 Cómo Iniciar la Aplicación (Dos Métodos)

Elige el método que mejor se adapte a tu flujo de trabajo:

### 🔹 Método A — Uso Local con Entorno Virtual (Recomendado para estudiantes)

#### 1. Crear el entorno virtual en la raíz del proyecto
```bash
python -m venv venv
```

#### 2. Activar el entorno virtual
* **En Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **En macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 4. Ejecutar migraciones e iniciar el servidor
```bash
# Entrar a la carpeta del proyecto
cd djangotutorial

# Aplicar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```
Visita la aplicación en: 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 🔹 Método B — Despliegue Automatizado con Docker 🐳 (Recomendado para Producción/QA)

El proyecto cuenta con dockerización completa para que no necesites configurar Python de forma local.

#### 1. Requisitos previos
Asegúrate de tener instalado [Docker](https://www.docker.com/) y Docker Compose en tu máquina.

#### 2. Levantar el proyecto en un solo comando
Desde la carpeta raíz del proyecto, ejecuta:
```bash
docker-compose up --build
```

#### 3. Qué hace Docker automáticamente:
- Descarga una imagen ligera de Python 3.13.
- Instala todas las dependencias listadas en `requirements.txt`.
- Copia y monta los volúmenes para habilitar **Live Reload** (cualquier cambio en el código se reflejará instantáneamente dentro del contenedor).
- Ejecuta el script de entrada `docker-entrypoint.sh`, el cual aplica migraciones de base de datos, valida la integridad de Django y levanta el servidor web.

Visita la aplicación en: 👉 [http://localhost:8000/](http://localhost:8000/)

---

## 📂 Estructura de Directorios Clave

```
.
├── Dockerfile                  # Receta para construir la imagen del contenedor
├── docker-compose.yml          # Orquestación de contenedores y volúmenes
├── docker-entrypoint.sh        # Script automatizado de inicio para el contenedor
├── .dockerignore               # Evita copiar archivos innecesarios al contenedor
├── requirements.txt            # Dependencias oficiales de Python/Django
├── LICENSE                     # Licencia del proyecto (MIT)
└── djangotutorial/             # Directorio del proyecto Django
    ├── manage.py               # Script de control de Django
    ├── mysite/                 # Configuración del proyecto
    └── leccion1/               # Aplicación educativa interactiva
        ├── static/             # Archivos CSS y diseño premium
        └── templates/          # Vistas HTML con herencia base (DRY)
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo [LICENSE](file:///c:/Users/BlandskronNotebook/Documents/updatesGitHubs/Django/M6/M6-L1-D1-IntroduccionDjango/LICENSE) para más detalles.

---

Desarrollado como recurso educativo para el **Módulo de Desarrollo de Aplicaciones Web con Django**. ¡Éxito en tu aprendizaje! 🚀
