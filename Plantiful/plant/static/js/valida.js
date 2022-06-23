$(function () {
    $("#miform").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            nombre: "required",
            fono: "required",
            texto: "required",

        }, //rules
        messages: {
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            nombre: {
                required: 'Ingrese el nombre',
            },
            fono: {
                required: 'Ingrese un número de celular',
                minlength: 'Debe contener 9 dígitos',
                maxlength: 'Debe contener 9 dígitos'
            },
            texto: {
                required: 'Ingrese el comentario'
            }
        }//messages
    }); //$('#miform').validate
}); //function


$(function () {
    $("#miform-registro").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            nombre: "required",
            apellido: "required",
            fecha: "required",
            password2: {
                required: true,
                equalTo: "#password"
            }

        }, //rules
        messages: {
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            nombre: {
                required: 'Ingrese el nombre',
            },
            apellido: {
                required: 'Ingrese el apellido',
            },
            fecha: {
                required: 'Seleccione una fecha',
                min: 'Fecha no corresponde',
                max: 'Debes ser mayor de edad'
            },
            password: {
                required: 'Ingresa una contraseña',
                minlength: 'Caracteres insuficientes'
            },
            password2: {
                required: 'Reingresa la contraseña',
                equalTo: 'Las contraseñas ingresadas no coinciden',
                minlength: 'Caracteres insuficientes'

            }
        }//messages
    }); //$('#miform').validate
}); //function

$(function () {
    $('#float-nombre').validCampoFranz(' abcdefghijklmnñopqrstuvwxyzáéíóú');
    $('#float-apellido').validCampoFranz(' abcdefghijklmnñopqrstuvwxyzáéíóú');
});

function Mover(obj) {
    obj.style.background = "#B87247";
}
function MoverFuera(obj) {
    obj.style.background = "#2B7929";

}

function Mayus() {
    var x = document.getElementById('float-nombre');
    x.value = x.value.toUpperCase();
}
//    <script type="text/javascript" src="https://rawcdn.githack.com/franz1628/validacionKeyCampo/bce0e442ee71a4cf8e5954c27b44bc88ff0a8eeb/validCampoFranz.js"></script>