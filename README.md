# 🐍 M6-L1 — Introducción a Django

## Guía paso a paso: Primera ejecución de Django

Este tutorial explica **cómo crear y ejecutar un proyecto Django desde cero**, usando distintas formas válidas de inicializar el proyecto.
Sigue los pasos **en orden**.

Repositorio base:
👉 [https://github.com/Blandskron/M6-L1-IntroduccionDjango](https://github.com/Blandskron/M6-L1-IntroduccionDjango)

---

## 1️⃣ Crear un entorno virtual (recomendado)

Desde la carpeta raíz del proyecto:

```bash
python -m venv venv
```

### Activar el entorno virtual

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

Si todo está correcto, verás `(venv)` al inicio de la consola.

---

## 2️⃣ Instalar Django

Con el entorno virtual activo:

```bash
pip install django
```

Verifica la instalación:

```bash
django-admin --version
```

---

## 3️⃣ Crear el proyecto Django

Existen **3 formas correctas** de crear un proyecto Django.
⚠️ **Solo debes usar UNA**, no todas.

---

### 🔹 Opción 1 — Crear el proyecto dentro de una carpeta nueva (recomendado para principiantes)

```bash
django-admin startproject mysite djangotutorial
```

Estructura generada:

```
djangotutorial/
├── manage.py
└── mysite/
```

Luego entra a la carpeta:

```bash
cd djangotutorial
```

---

### 🔹 Opción 2 — Crear el proyecto en una carpeta existente

```bash
django-admin startproject mysite
```

Estructura:

```
mysite/
├── manage.py
└── mysite/
```

Luego entra a la carpeta:

```bash
cd mysite
```

---

### 🔹 Opción 3 — Crear el proyecto en la carpeta actual

⚠️ Usa esta opción **solo si estás seguro** de que la carpeta está vacía.

```bash
django-admin startproject mysite .
```

Estructura:

```
.
├── manage.py
└── mysite/
```

👉 En esta opción **NO es necesario hacer `cd`**, ya estás en la carpeta correcta.

---

## 4️⃣ Ejecutar el servidor por primera vez

Independiente de la opción usada, debes estar en la carpeta donde está **`manage.py`**.

Ejecuta:

```bash
python manage.py runserver
```

Salida esperada:

```
Starting development server at http://127.0.0.1:8000/
```

---

## 5️⃣ Verificar en el navegador

Abre tu navegador y visita:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Si ves la página de bienvenida de Django 🎉
**¡Tu proyecto está funcionando correctamente!**

---

## 6️⃣ Errores comunes

❌ **`'django-admin' no se reconoce`**
➡️ El entorno virtual no está activado.

❌ **`manage.py no existe`**
➡️ Estás en la carpeta incorrecta.

❌ **Puerto ocupado**
➡️ Usa otro puerto:

```bash
python manage.py runserver 8080
```

---

## ✅ Conclusión

En esta actividad aprendiste a:

* Crear un entorno virtual
* Instalar Django
* Crear un proyecto Django de 3 formas distintas
* Ejecutar el servidor de desarrollo
* Verificar que Django funciona correctamente

Este es el **primer paso obligatorio** antes de crear aplicaciones, modelos o vistas.

🚀 ¡Listo para continuar con Django!
