# Método del punto fijo 🔢

    Bryan David Álvarez Galvis 192096

## Descripción del proyecto 👀

El método de punto fijo es un método iterativo de carácter abierto, usado en análisis numérico para encontrar una solución aproximada a una ecuación f(x)=0. Este proyecto busca dar solución a este tipo de ejercicios mediante una calculadora amigable con el usuario, mostrando paso a paso cada iteración y generando la gráfica respectiva

## Instalar el proyecto 🚀

1. Clona o descarga el repositorio

```bash
git clone https://github.com/BryanAG-Kcts/punto-fijo.git
```

2. Cambia al directorio raíz de la aplicación

```bash
cd punto-fijo
```

3. Instala las dependencias

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación

```bash
python index.py
```

## ¿Como contribuir? 🛠

El proyecto se divide en distintos directorios y módulos

- **components**

Dentro de components se crean los distintos widgets que serán insertados en el flujo de la vista. Para poder separar la parte lógica de la renderización de componentes se optó por usar clases con atributos y métodos estáticos. Con la finalidad de importar únicamente la clase cuando sea necesario y de mantener un estado global para la aplicación

- **documentation**

Cada vez que se agregue una funcionalidad nueva, si esta va a hacer usada por el usuario se le debe crear una guía de uso. Para ello, se crean clases con atributos estáticos y se renderiza el texto por secciones. Todo componente que esté dirigido a dar explicaciones o guías al usuario final debe ir en este directorio

- **services**

Para separar grandes segmentos de lógica se optó por usar clases con atributos y métodos estáticos cuya función sea resolver problemas más no interferir con el flujo de componentes en la aplicación. Es decir, toda abstracción del problema que no involucre renderizar componentes en la aplicación debe ir en este directorio
