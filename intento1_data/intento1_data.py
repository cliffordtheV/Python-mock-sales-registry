import os
import csv
import sys

sales=[]
break_midname = False
#Directorio madre donde esta el archivo .py (creo que es necesario para que funcione en otros computadores)
if getattr(sys, "frozen", False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

#Esto es para definir el nombre y ruta del archivo de los datos
csv_filename = "archivo_ventas.csv"
csv_filepath = os.path.join(base_dir, "csv_data")
path_to_csv = os.path.join(csv_filepath, csv_filename)
#Esto verifica si existe el folder csv_data
verify_csvfolder = os.makedirs(csv_filepath, exist_ok=True)

#Estos son los encabezados globales de la lista csv, si quiero añadir algo mas puedo empezar aqui
global_field_names = ['id', 'producto', 'precio', 'cantidad', 'subtotal']

#Definiendo las IDs de las ventas, necesario para la edicion
current_id_global = 100

verify_csvfile_id = os.path.isfile(path_to_csv)
if verify_csvfile_id:
    with open(path_to_csv, "r", newline= '') as r_csv_id:
        id_read = csv.DictReader(r_csv_id)
        id_read_list = list(id_read)
        if len(id_read_list) > 0:
            last_row_id = int(id_read_list[-1]["id"])
            last_row_id+=1
            current_id_global = last_row_id
else:
    print("No se encontro el archivo de ventas.")

#Funciones

#Para reportar una nueva venta 
def new_sale():
    global current_id_global
    name_product = input("Nombre del producto (o 'cancelar' para cancelar): ")
    if name_product.lower() in ("fin", "no", "cancel", "cancelar", ""):
        return True
    try:
        price = float(input(f"Precio de {name_product}: "))
    except ValueError:
        print("El precio debe escribirse como numero.")
        return
    try:
        cuantity = int(input(f"Cantidad vendida: "))
    except ValueError:
        print("La cantidad debe escribirse como numero sin decimales.")
        return
    
    sale_id = current_id_global
    
    #Se pasa todos los datos a una variable para guardar los datos mas recientes, esta tambien es un parametro de la funcion de guardar datos
    recent_dict = {"id": sale_id, "producto": name_product, "precio": price, "cantidad": cuantity, "subtotal": price*cuantity}
    current_id_global+=1
    
    sales.append(recent_dict)
    
    save_data(recent_dict)

#Para ver un reporte de todas las ventas registradas
def report ():
    verify_csvfile = os.path.isfile(path_to_csv)
    if verify_csvfile:
        gen_total = 0
        sales_quantity = 0
        with open(path_to_csv, mode = "r") as read_csv:
            csv_file_read = csv.DictReader(read_csv)
            for logs in csv_file_read:
                r_price = float(logs["precio"])
                r_quantity = int(logs["cantidad"])
                r_subtotal = r_price * r_quantity
                gen_total+= r_subtotal
                sales_quantity += 1
                print(f"ID:{logs['id']} Producto: {logs["producto"]}| Precio: {r_price}| Cantidad: {r_quantity}| Subtotal: {r_subtotal}")
            if sales_quantity > 0 :
                average = gen_total/sales_quantity
                print(f"Promedio de ventas: {average:.2f} - Ganancias totales: {gen_total:.2f}")
            else:
                print("No hay ventas registradas")
    else:
        print("\nNo se ha registrado ninguna venta todavia\n")

#Aqui la funcion para buscar al producto vendido mas caro
def mst_expensive_function():
    verify_csvfile = os.path.isfile(path_to_csv)
    if verify_csvfile:
        with open(path_to_csv, mode = "r") as read_csv:
            csv_file_read = csv.DictReader(read_csv)
            try:
                max_item = next(csv_file_read)
                max_subtotal = float(max_item["subtotal"])
                for logs in csv_file_read:
                    try:
                        current_subtotal = float(logs["subtotal"])
                        if current_subtotal > max_subtotal:
                            max_subtotal = current_subtotal
                            max_item = logs
                    except (ValueError, TypeError):
                        continue #Esto hace que si hay filas de datos con datos corruptos o mal escritos, se las salte
                print(f"La venta de mayor valor es de: {max_item['producto']} (id: {max_item['id']}) con un subtotal de {max_subtotal:.2f}")
            except StopIteration:
                print("No hay ventas registradas.")
    else:
        print("No se encontro el archivo de ventas. Puede generarlo registrando una nueva venta.")

#Aqui la funcion para el video
def vid_walrus():
    video_src = os.path.join(base_dir, "walrust.mp4")
    if os.path.exists(video_src):
        print("\n       ÜH ÜH ÜH")
        os.startfile(video_src)
    else:
        print(f"Buscando en {video_src}")
        print("         Video no encontrado.")

#Aqui la funcion para guardar las columnas de ventas
def save_data(recent_dict):
    verify_csvfile = os.path.isfile(path_to_csv) #Esto revisa si existe o no el archivo csv
    with open(path_to_csv, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=global_field_names)
        if verify_csvfile == False:
            writer.writeheader()
        writer.writerow(recent_dict)

#Aqui la funcion para editar las ventas registradas
def edit_sale():
    verify_csvfile_id = os.path.isfile(path_to_csv)
    if verify_csvfile_id:
        try:
            search_id = int(input("Introduzca la ID de la venta que quiere editar: "))
        except ValueError:
            print("Las IDs solo contienen numeros.")
            return
        
        found = False
        with open(path_to_csv, "r", newline= '') as r_csv_id:
            id_read = csv.DictReader(r_csv_id)
            id_read_list = list(id_read)
            for lkd_ids in id_read_list:
                if search_id == int(lkd_ids["id"]):
                    lkd_ids["producto"] = input(f"Nuevo nombre del producto de la venta {lkd_ids['id']} (anterior: {lkd_ids['producto']}): ") 
                    try:
                        lkd_ids["precio"] = float(input(f"Nuevo precio de la venta {lkd_ids['id']} (anterior: {lkd_ids['precio']}): "))
                    except ValueError:
                        print("Valor invalido.")
                        return
                    try:
                        lkd_ids["cantidad"] = int(input(f"Nueva cantidad vendida en la venta {lkd_ids['id']} (anterior: {lkd_ids['cantidad']}): "))
                    except ValueError:
                        print("Valor invalido.")
                        return
                    lkd_ids["subtotal"] = lkd_ids["precio"] * lkd_ids["cantidad"]
                    found = True
                    break
            if found:
                with open(path_to_csv, "w", newline= '') as new_csv_data:
                    writer = csv.DictWriter(new_csv_data, fieldnames=global_field_names)
                    writer.writeheader()
                    writer.writerows(id_read_list)
                    print("Venta editada exitosamente.")
            else:
                print("ID de venta no encontrada")
        
    else:
        print("No se encontro el registro de ventas.")

#Aqui la funcion para eliminar alguna venta registrada
def delete_sale():
    verify_csvfile_id = os.path.isfile(path_to_csv)
    
    if verify_csvfile_id:
        try:
            delete_id = int(input("Introduzca la ID de la venta que quiere borrar: "))
        except ValueError:
            print("Las IDs solo contienen numeros.\n")
            return

    with open(path_to_csv, "r", newline= '') as r_csv_id:
        id_read = csv.DictReader(r_csv_id)
        id_read_list = list(id_read)
        #id_read_list es una lista de diccionarios y sale_to_delete busca el diccionario con el id a borrar
        sale_to_delete = next((sale for sale in id_read_list if int(sale["id"]) == delete_id), None) #Esto revisa si la id dada por el usuario existe
        #sale_to_delete (si encontro la id dada por el usuario) es igual al diccionario con la id que el usuario quiere borrar
        if sale_to_delete:
            print(f"Esta seguro que quiere borrar la venta con id {sale_to_delete['id']}? \n Producto: {sale_to_delete['producto']} \n Precio: {sale_to_delete['precio']}  \n Cantidad: {sale_to_delete['cantidad']} \n Subtotal: {sale_to_delete['subtotal']}")
            delete_or_not = input("S/N")
            if delete_or_not.lower() in ("s", "si", "yes"):
                #La logica funciona de manera que se crea una nueva lista donde la id borrada jamas existio.
                new_list = [x for x in id_read_list if int(x['id']) != delete_id]
                with open(path_to_csv, "w", newline= '') as del_csv_data:
                    writer = csv.DictWriter(del_csv_data, fieldnames=global_field_names)
                    writer.writeheader()
                    writer.writerows(new_list)
                
                print(f"Venta {delete_id} borrada exitosamente.")
            else:
                print("Operacion cancelada")
                return

print(os.path.abspath(path_to_csv))
print("==REGISTRO DE VENTAS==")
print("1- Registrar una nueva venta")
print("2- Mostrar un reporte de todas las ventas registradas (incluye promedio y total de ventas)")
print("3- Buscar la venta registrada de mayor valor")
print("4- Editar una venta registrada")
print("5- Eliminar una venta registrada")
print("6- Salir")

while True:
    choice = input("\nElija lo que quiere hacer (1-6): ")
    if choice in ("1", "2", "3", "4", "5", "6", "7"):
        if choice == "1":
            res = new_sale()
            if res == True:
                break
        elif choice == "2":
            report()
        elif choice == "3":
            mst_expensive_function()
        elif choice == "4":
            edit_sale()
        elif choice == "5":
            delete_sale()
        elif choice == "6":
            print("Saliendo...")
            break
        elif choice == "7":
            print(r"""		__ ___
             .'. -- . '.
            /U)  __   (O|
           /.'  ()()   '.\._
         .',/;,_.--._.;;) . '--..__
        /  ,///|.__.|.\\\  \ '.  '.''---..___
       /'._ '' ||  ||  '' _'\  :   \   '   . '.
      /        ||  ||        '.,    )   )   :  \
     :'-.__ _  ||  ||   _ __.' _\_ .'  '   '   ,)
     (          '  |'        ( __= ___..-._ ( (.\\
    ('\      .___ ___.      /'.___=          \.\.\
     \\\-..____________..-'' """)
            vid_walrus()
    else:
        print("Debe elejir una de las 6 opciones (o 7 lmao)\n")