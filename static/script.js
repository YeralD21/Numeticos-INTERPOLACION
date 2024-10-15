document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();

    var formData = new FormData();
    var fileInput = document.getElementById('fileInput').files[0];
    var method = document.getElementById('method').value;
    formData.append('file', fileInput);
    formData.append('method', method);  // Enviar el método seleccionado

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('area').textContent = 'Área: ' + data.area;
        document.getElementById('plot').src = 'data:image/png;base64,' + data.plot;
    })
    .catch(error => console.error('Error:', error));
});
