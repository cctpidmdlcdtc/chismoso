app.py
- falta el availability_percentage antes de insertar
- insertar
- comprobar si salen

SELECT 
    w.name AS worker,
    r.name AS role
FROM 
    Worker_Hours wh
JOIN 
    Workers w ON wh.worker_id = w.worker_id
JOIN 
    Roles r ON wh.role_id = r.role_id
WHERE 
    wh.date = "2024-11-11";


- mostrar workers añadidos dentro del proyecto









- sqlalchemy y wtforms

- add_project
    - faltan fechas

- list_projects
    - qué responsable y consultor tiene ahora

- adjuntar documentos a los comentarios de estado

```html
<!-- Formulario de Subida de Archivo -->
<form action="/upload-file" method="POST" enctype="multipart/form-data">
    <h2>Formulario de Subida de Archivo</h2>
    <label for="file">Sube tu archivo:</label>
    <input type="file" id="file" name="file">
    
    <button type="submit">Subir Archivo</button>
</form>
```


- Deslizar para elegir la duración del proyecto

```html
<!-- Formulario de Encuesta -->
<form action="/submit-survey" method="GET">

<label for="satisfaction">¿Qué tan satisfecho estás con el servicio?</label>
<div>
    <input type="range" id="satisfaction" name="satisfaction" min="1" max="100" value="50" oninput="syncNumberWithRange()">    
    <input type="number" id="range-number" min="1" max="100" value="50" oninput="syncRangeWithNumber()">
</div>

<button type="submit">Enviar Encuesta</button>
</form>

<script>
    const rangeInput = document.getElementById('satisfaction');
    const numberInput = document.getElementById('range-number');

    // Sincroniza el valor del número con el rango
    function syncNumberWithRange() {
        const value = rangeInput.value;
        numberInput.value = value;
    }

    // Sincroniza el valor del rango con el número
    function syncRangeWithNumber() {
        const value = numberInput.value;
        if (value >= 1 && value <= 100) { // Validación dentro de rango
            rangeInput.value = value;
        }
    }

</script>
```

De manera que el input y el slide queden a la misma altura:

```css
<style>
    form {
        border: 1px solid #ccc;
        padding: 15px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    label {
        display: block;
        margin-bottom: 5px;
    }
    input, select, button {
        margin-bottom: 10px;
    }
    div {
        display: flex;
        align-items: center; /* Alinea verticalmente los elementos */
        gap: 10px; /* Añade espacio entre los elementos */
    }

    input[type="range"] {
        vertical-align: middle; /* Ajusta su alineación */
        height: auto; /* Asegúrate de que no tenga un alto excesivo */
    }

    input[type="number"] {
        vertical-align: middle;
        height: auto; /* Opcional, ajusta según sea necesario */
    }
</style>
```