let checkedElements=[];
            function handleChange(checkbox) {
                if(checkbox.checked === true){
                    checkedElements.push(checkbox.value);
                }else{
                    checkedElements = checkedElements.filter(value => value != checkbox.value)
                }
                document.getElementById("search").value = checkedElements.join(", ");
            }


            $(document).ready(function() {
                $('.js-example-basic-multiple').select2();
            });
                    
                    function myFunction(){
                        let valores =$('#ingredientes').select2('data');
                        console.log(valores)
                        console.log(valores[0].id)
                        
                    }
    
                    
                    var formrecipe = document.getElementById('formrecipe');
                    formrecipe.onsubmit = function (event) {
                        
                        event.preventDefault();
                        
                    
                        var formulario = new FormData(formrecipe);
                    
                    
                        fetch("/create_recipe", { method: 'POST', body:  formulario})
                            .then(response => response.json())
                            .then(data => {
                                
                            window.location.href = "/dashboard/0";
                                
                            });
            }