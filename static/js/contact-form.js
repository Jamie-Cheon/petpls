function formValidation() {

    /* ------------------------------------------------
        Init Contact Form
    --------------------------------------------------- */

    $('#contact-form').formValidation({
        framework: 'bootstrap',

        /*---- Feedback Icons ----*/

        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },

        /*---- Fields to be Validated ----*/

        fields: {
            fname: {
                validators: {
                    notEmpty: {
                        message: 'The name is required'
                    }
                }
            },
            phone: {
                validators: {
                    notEmpty: {
                        message: 'The phone number is required'
                    },
                    regexp: {
                        message: 'The phone number can only contain the digits, - and .',
                        regexp: /^(?:(1\-?)|(\+1 ?))?\(?(\d{3})[\)\-\.]?(\d{3})[\-\.]?(\d{4})$/
                        // message: 'The phone number can only contain the digits, spaces, -, (, ), + and .',
                        // regexp: /^[0-9\s\-()+\.]+$/
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required'
                    },
                    emailAddress: {
                        message: 'The input is not a valid email address'
                    }
                }
            },
            msg: {
                validators: {
                    notEmpty: {
                        message: 'The message is required'
                    },
                    stringLength: {
                        max: 700,
                        message: 'The message must be less than 700 characters long'
                    }
                }
            },
        },
    })
        .on('err.form.fv', function (e) {
        })
        .on('success.form.fv', function (e) {
            /*---- Ajax Code for Submitting Form ----*/
            e.preventDefault();
            var $form = $(e.target),
                id = $form.attr('id'),
                thisForm = '#' + id;

            $('.form-loader', thisForm).fadeIn();

            // var form = $("#contact-form").closest("form");
            var jform = new FormData();
            // jform.append('user',$('#user').val());

            jform.append('fname',$('#fname').val());
            jform.append('phone',$('#phone').val());
            jform.append('email',$('#email').val());
            jform.append('msg',$('#msg').val());



            $.ajax({
                method: 'post',
                url: $form.attr('action'),
                data: jform,
                mimeType: 'multipart/form-data', // this too
                contentType: false,
                cache: false,
                processData: false,
                dataType: "json",
                success: function (res) {
                    $('.form-loader', thisForm).fadeOut();
                    var output = document.getElementById('formResponse');
                    output.innerHTML = 'Thank you for your message. We will get back to you shortly';
                    $('#formResponse').addClass('alert-theme-success').fadeIn();
                }, error: function (err) {
                    $('.form-loader', thisForm).fadeOut();
                    var output = document.getElementById('formResponse');
                    output.innerHTML = 'We are experiencing some problems. Please try again later'
                    $('#formResponse').addClass('alert-theme-danger').fadeIn();
                }
            })
        });

}

var $win = $(window);

$win.on('load', function() {
    formValidation();
});