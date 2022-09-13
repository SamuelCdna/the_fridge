var formLogin = document.getElementById('formLogin');
formLogin.onsubmit = function (event) {
    
    event.preventDefault();
    

    var formulario = new FormData(formLogin);


    fetch("/create_recipe", { method: 'POST', body:  formulario})
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if(data.message == "correcto") {
                window.location.href = "/dashboard";
            } else {
                var mensajeAlerta = document.getElementById('mensajeAlerta');
                mensajeAlerta.innerHTML = data.message;
                mensajeAlerta.classList.add("alert");
                mensajeAlerta.classList.add("alert-danger");
            }
        });