from os import system
import math

def create_field(ancho_panel=400, alto_panel=50):
    print("Ingresar variable contenedora del campo:\n")
    content_varname = input("  []>_ ")

    print("Ingresar nombre del campo:\n")
    field_name = input("  []>_ ")

    print("Especificar width y height?")
    resp = input("  [](S/N)>_ ")

    if resp == "S" or resp == "s":
        ancho_panel = float(input("  [USUARIO](width)>_ "))
        alto_panel = float(input("  [USUARIO](height)>_ "))
    elif resp == "N" or resp == "n":
        print("Se procedera con valores default")
    else:
        print("Opcion no valida. Se procedera con valores default")

    x_label = int(math.ceil((1/20)*ancho_panel))
    y_label = int(math.ceil((alto_panel/3)+2))
    w_label = int(math.ceil(x_label+40))

    x_field = int(math.ceil(x_label+w_label+10))
    y_field = int(math.ceil(alto_panel/3))
    w_field = int(math.ceil((6/20)*ancho_panel))

    code_file = open(f"{field_name}_java_code.txt", "w")

    copy_string = f""">>>>> En el initComponents() >>>>>>
   // ----- Instanciar Campo {field_name}
    jPanel{field_name} = new javax.swing.JPanel();
    jLabel{field_name} = new javax.swing.JLabel();
    jField{field_name} = new javax.swing.JTextField();


   // ----------- Campo de {field_name} [Label + Field] BEGIN:
    // ----- Panel {field_name}
    jPanel{field_name}.setLayout(null); 
    jPanel{field_name}.setBorder(new javax.swing.border.EtchedBorder());
    jPanel{field_name}.setOpaque(false);
    jPanel{field_name}.setBounds(20, 175, {ancho_panel}, {alto_panel}); // Editar 20 (x), y 175 (y) a conveniencia

    // ----- Label {field_name}
    jPanel{field_name}.add(jLabel{field_name});
    jLabel{field_name}.setText("{field_name}");
    jLabel{field_name}.setFont(new java.awt.Font("Verdana", 0, 12));
    jLabel{field_name}.setBounds({x_label}, {y_label}, {w_label}, 14);

    // ----- Field {field_name}
    jPanel{field_name}.add(jField{field_name});
    jField{field_name}.setFont(new java.awt.Font("Verdana", 0, 12));
    jField{field_name}.setBounds({x_field}, {y_field}, {w_field}, 20);

    // ----- Agregar Todo el conjunto al container
    {content_varname}.add(jPanel{field_name});
   // END //

>>>> En la clase >>>>>
    // ----- Declarar variables campo {field_name}
    private javax.swing.JPanel jPanel{field_name};
    private javax.swing.JLabel jLabel{field_name};
    private javax.swing.JTextField jField{field_name};
    """
    code_file.write(copy_string)
    code_file.close()

def create_button():
    print("Ingresar variable contenedora del boton:\n")
    content_varname = input("  []>_ ")

    print("Ingresar nombre del boton:\n")
    field_name = input("  []>_ ")

    print("Ingresar nombre de la funcion del boton:\n")
    nombre_funcion = input("  []>_ ")

    code_file = open(f"{field_name}_java_code.txt", "w")

    copy_string = f""">>>>> En el initComponents() >>>>>>
    // ----- Instanciar Boton {field_name}
    jButton{field_name} = new javax.swing.JButton();

   // ----------- Boton de {field_name} BEGIN:
    // ----- Boton {field_name}
    jButton{field_name}.setText("{field_name}");
    jButton{field_name}.addActionListener(new java.awt.event.ActionListener(){{
        public void actionPerformed(java.awt.event.ActionEvent evt){{
            {nombre_funcion}(evt);
        }}
    }});

    // ----- Agregar boton al container
    {content_varname}.add(jButton{field_name});
    jButton{field_name}.setBounds(30, 30, 60, 40);
   // END //

>>>> En la clase >>>>>
    // ----- Declarar variable boton {field_name}
    private javax.swing.JButton jButton{field_name};

>>>> Funcion boton >>>>>
    private void {nombre_funcion}(java.awt.event.ActionEvent evt){{
        dispose();
    }}
    """
    code_file.write(copy_string)
    code_file.close()

def main():
    menu = {
        1: "create_field()",
        2: "create_button()",
        3: lambda: quit()
    }
    print("""
############################### FACTURACION AGT ###############################
#                                                                             #
#  Seleccionar opcion::                                                       #
#    1. agregar campo                                                         #
#    2. agregar boton                                                         #
#                                                                             #
#    3. salir                                                                 #
#                                                                             #
#                                                                             #""")
    print("#                                                                      ls-sys #")
    print("###############################################################################\n\n")
    opc = input("#  []>_ ")
    opc = int(opc)


    system("clear")
    exec(menu[opc])


if __name__ == "__main__":
    main()
    print("############### DONE ###############")
