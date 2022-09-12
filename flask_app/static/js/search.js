let checkedElements=[];
            function handleChange(checkbox) {
                if(checkbox.checked === true){
                    checkedElements.push(checkbox.value);
                }else{
                    checkedElements = checkedElements.filter(value => value != checkbox.value)
                }
                document.getElementById("search").value = checkedElements.join(", ");
            }