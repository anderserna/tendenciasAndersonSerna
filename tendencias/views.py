from django.shortcuts import render , redirect


from tendencias.models import Recursosh ,Personal_admistativoo, Enfermerass , Medicos_db

# Create your views here.


def enfermeras(request):
    if request.method =='POST':
       presion_arterial = request.POST.get('presion_arterial', '')
       temperatura = request.POST.get('temperatura', '')
       pulso = request.POST.get('pulso', '')
       nivel_oxigeno = request.POST.get('nivel_oxigeno_sangre', '')
       registrar_medicamento = request.POST.get('medicamento_suministrado','')
       fecha_visita = request.POST.get('fecha','')
       hora_visita = request.POST.get('hora','')


       Enfermerass.objects.create(
           presion_arterial=presion_arterial,
           temperatura=temperatura,
           pulso=pulso,
           nivel_oxigeno=nivel_oxigeno,
           registrar_medicamento = registrar_medicamento,
           fecha_visita=fecha_visita,
           hora_visita=hora_visita
       ) 
    return render(request,'enfermeras.html')
        


def personalAdmin(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        cedula = request.POST.get('cedula', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
        genero = request.POST.get('genero', '')
        direccion = request.POST.get('direccion', '')
        telefono = request.POST.get('telefono', '')
        correo = request.POST.get('correo', '')
        nombre_contacto_emergencia = request.POST.get('nombre_contacto_emergencia', '')
        relacion_paciente = request.POST.get('relacion_paciente', '')
        numero_emergencia = request.POST.get('numero_emergencia', '')
        nombre_compania_seguros = request.POST.get('nombre_compania_seguros', '')
        numero_poliza = request.POST.get('numero_poliza', '')
        estado_poliza = request.POST.get('estado_poliza', '')
        fecha_cita = request.POST.get('fecha_cita','')
        hora_cita = request.POST.get('hora_cita','')
        
        Personal_admistativoo.objects.create(
            nombre=nombre,
            cedula=cedula,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            direccion=direccion,
            numero_telefono=telefono,
            correo=correo,
            nombre_emergencia=nombre_contacto_emergencia,
            relacion=relacion_paciente,
            numero_emergencia=numero_emergencia,
            nombre_compañia=nombre_compania_seguros,
            numero_poliza=numero_poliza,
            estado_poliza=estado_poliza,
            fecha_cita=fecha_cita,
            hora_cita=hora_cita

            



        )

    return render(request,'personaladmin.html')


def recursos(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        cedula = request.POST.get('cedula', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
        direccion = request.POST.get('direccion', '')
        telefono = request.POST.get('telefono', '')
        rol = request.POST.get('rol', '')
        usuario = request.POST.get('usuario', '')
        contraseña = request.POST.get('contraseña', '')
        correo = request.POST.get('correo', '')
        licencia = request.POST.get('licencia', '')

        Recursosh.objects.create(
            nombre=nombre,
            cedula=cedula,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            rol=rol,
            usuario=usuario,
            correo=correo,
            contraseña=contraseña,
            licencia=licencia,
        )

    return render(request,'recursos.html')


def login(request):
    if request.method == 'POST':
        # Procesar la autenticación si la solicitud es POST
        username = request.POST.get('username')
        password = request.POST.get('password')


        print(username)
        
        try:
            recursos_humanos = Recursosh.objects.get(usuario=username)
            #globla_cedula_medico = recursos_humanos.cedula
            print(recursos_humanos.contraseña)
        except Recursosh.DoesNotExist:
            recursos_humanos = None
            print('vvvvvvvvvvvvvvvvvvvvvv')
        
    
        if recursos_humanos is not None and recursos_humanos.contraseña == password:
            # Autenticación exitosa, redirige a la página deseada

            print(recursos_humanos.rol)

            if recursos_humanos.rol == 'Recursos humanos':
                return redirect('recursos')
            elif recursos_humanos.rol == 'Personal administrativo':
                return redirect('personalAdmin')
            elif recursos_humanos.rol == 'Enfermera':
                return redirect('enfermeras')
            elif recursos_humanos.rol == 'Medicos':
                return redirect('medicos')
                pass

               #return redirect(reverse('medicos') + f'?mensaje={recursos_humanos.cedula}')

    
    return render(request, 'login.html')


def medicos(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha', '')
        cedula_medicoatendio = request.POST.get('cedula_medico', '')
        motivo_consulta = request.POST.get('motivo_consulta', '')
        sintomatologia = request.POST.get('sintomatologia', '')
        diagnostico = request.POST.get('diagnostico', '')
        numero_orden_medicamento = request.POST.get('numero_orden_medicamentos', '')
        nombre_medicamento = request.POST.get('nombre_medicamento', '')
        dosis = request.POST.get('dosis', '')
        duracion_tratamiento = request.POST.get('duracion', '')
        numero_orden_procedimiento = request.POST.get('numero_orden_procedimiento', '')
        nombre_procedimiento = request.POST.get('nombre_procedimiento', '')
        cantidad_procedimiento = request.POST.get('cantidad_procedimiento', '')
        frecuencia_repite = request.POST.get('frecuencia_procedimiento', '')
        requiere_asistencia_procedimiento = request.POST.get('requiere_asistencia_procedimiento', '')
        numero_orden_ayuda = request.POST.get('numero_orden_ayuda', '')
        cantidad_ayuda = request.POST.get('cantidad_ayuda', '')
        nombre_ayudadiagnostica = request.POST.get('nombre_ayudadiagnostica', '')
        requiere_asistencia_ayuda = request.POST.get('requiere_asistencia_ayuda', '')
       


        Medicos_db.objects.create(
            fecha=fecha,
            cedula_medicoatendio=cedula_medicoatendio,
            motivo_consulta=motivo_consulta,
            sintomatologia=sintomatologia,
            diagnostico=diagnostico,
            numero_orden_medicamento=numero_orden_medicamento,
            nombre_medicamento=nombre_medicamento,
            dosis=dosis,
            duracion_tratamiento=duracion_tratamiento,
            numero_orden_procedimiento=numero_orden_procedimiento,
            nombre_procedimiento=nombre_procedimiento,
            cantidad_procedimiento=cantidad_procedimiento,
            frecuencia_repite=frecuencia_repite,
            requiere_asistencia_procedimiento=requiere_asistencia_procedimiento,
            numero_orden_ayuda=numero_orden_ayuda,
            cantidad_ayuda=cantidad_ayuda,
            nombre_ayudadiagnostica=nombre_ayudadiagnostica,
            requiere_asistencia_ayuda=requiere_asistencia_ayuda,  
            
          
        )

    return render(request,'medico.html')
