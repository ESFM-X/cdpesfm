string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="description" content= "Página oficial de Club de Programación ESFM">
     
        <meta name="robots" content="index, follow">
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                margin: 0px;
                
                
                }
            a{
                text-decoration:none;
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

            .tpyt1{
                background:linear-gradient(0deg,#589db4 , #644598)!important;
                color: white;
            }
            .ting{
                background:linear-gradient(0deg,#633a93 , #c33c4b)!important;
                color: white;
            }
            .tmat{
                background:linear-gradient(0deg,#644598 , #589db4)!important;
                color: white;
            }
            .twol{
                background:linear-gradient(0deg,#bc01aa , #53ac8f)!important;
                color: white;
            }
            .tpyt2{
                background:linear-gradient(0deg,#633a93 , #c33c4b)!important;
                color: white;
            }
            .tcrip{
                background:linear-gradient(0deg,#ff7100 , #33005a)!important;
                color: white;
            }
            .bg-danger{
                background:linear-gradient(0deg,#7b1448, #40122A)!important;
                color: white;
               
            }


            .btn-outline-success{
                color:#28a745;
                border-color:#28a745
            }
            .btn-outline-success:hover{
                color:#fff;
                background-color:#28a745;
                border-color:#28a745}
            .btn-outline-success.focus,.btn-outline-success:focus{
                box-shadow:0 0 0 .2rem rgba(40,167,69,.5)
            }
            .btn-outline-success.disabled,.btn-outline-success:disabled{
                color:#28a745;
                background-color:transparent
            }
            .btn-outline-success:not(:disabled):not(.disabled).active,.btn-outline-success:not(:disabled):not(.disabled):active,.show>.btn-outline-success.dropdown-toggle{
                color:#fff;
                background-color:#28a745;
                border-color:#28a745
            }
            .btn-outline-success:not(:disabled):not(.disabled).active:focus,.btn-outline-success:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-success.dropdown-toggle:focus{
                box-shadow:0 0 0 .2rem rgba(40,167,69,.5)
            }
            .custom-control-input:checked~.custom-control-label::before {
                background-color:#7b1448!important;
                border-color: #7b1448!important;
            }
            .custom-control-input:focus~.custom-control-label::before{
                box-shadow:0 0 0 .2rem #7b1448;
            }
            .custom-control-label:hover{
                cursor:pointer;
            }
            .rc-slider-track{
                background-color:#7b1448!important;
            }
            .rc-slider-dot-active {
                border-color: #7b1448!important;
            }
            .rc-slider-handle{
                border: solid 2px #7b1448;
            }
            .rc-slider-handle:hover{
                border: solid 2px #7b1448;
            }
            .rc-slider-handle-click-focused{
                border-color: #7b1448!important;
            }
            .is-focused,.is-pseudo-focused{
                border-color: #7b1448!important;
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