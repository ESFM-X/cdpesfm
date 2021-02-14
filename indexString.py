string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                margin: 0px;
                
                }
            button{
                color: #ffffff;
                }
            
            .nav-link:hover{
                color:#f9aa3a;
                }
            .nav-link{
                color:#7b1448;
                }
            .btn-primary{
                background-color:#9B84EE;
                border-color:#9B84EE;
            }
            .btn-primary:HOVER{
                background-color:#7289DA;
                border-color:#7289DA;
            }
            .jumbotron{
                border-radius:0rem;
            }
            .btn-danger:HOVER{
                background-color:#000000;
                border-color:#000000;
                color: #FFFFFF;
            }
            .btn-danger{
                background-color:#FFFFFF;
                border-color:#000000;
                color: #000000;
            }
            .btn-danger:not(:disabled):not(.disabled).active, .btn-danger:not(:disabled):not(.disabled):active, .show>.btn-danger.dropdown-toggle{
                background-color:#FFFFFF;
                border-color:#000000;
                color: #000000;
            }
            .cripto{
                background:linear-gradient(0deg,#ff7100 , #33005a)!important;
            }
            .bg-primary{
                background:linear-gradient(0deg,#589db4 , #644598)!important;
            }
            .bg-dark{
                background:linear-gradient(0deg,#633a93 , #c33c4b)!important;
            }
            .bg-warning{
                background:linear-gradient(0deg,#c33c4b , #633a93)!important;;
            }
            .bg-info{
                background:linear-gradient(0deg,#644598 , #589db4)!important;
            }
            .bg-success{
                background:linear-gradient(0deg,#bc01aa , #53ac8f)!important;
            }


            .btn-danger.focus,.btn-danger:focus{
                background-color:#FFFFFF;
                border-color:#000000;
                color: #000000;
                box-shadow:0 0 0 .2rem rgba(0,0,0,0)
            }
            .btn-danger.disabled,.btn-danger:disabled{
                background-color:#FFFFFF;
                border-color:#000000;
                color: #000000;
            }
            .btn-danger:not(:disabled):not(.disabled).active,.btn-danger:not(:disabled):not(.disabled):active,.show>.btn-danger.dropdown-toggle{
                background-color:#FFFFFF;
                border-color:#000000;
                color: #000000;
            }
            .btn-danger:not(:disabled):not(.disabled).active:focus,.btn-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-danger.dropdown-toggle:focus{
                box-shadow:0 0 0 .2rem rgba(0,0,0,0)
            }

            .modal-content{
                background:linear-gradient(0deg,#589db4 , #644598)!important;
                color: white;
            }

        </style>
    </head>
    <body style = "margin: 0!important;" >
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""