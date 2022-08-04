from django.core.management.base import BaseCommand, CommandError
from gastronomia.models import Establecimiento
from django.utils import timezone
import pandas as pd




class Command(BaseCommand):
    help = 'Load data from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+',type=str)
        parser.add_argument('sheet_name', nargs='+', type=str)
    
    def handle(self, *args, **options):
        """
        This command helps to load data from Excel file using this command:
        python manage.py loadingestablecimientos /Users/santiagovinan/Downloads/data_empr.xlsx survey
        """
        start_time = timezone.now()
        print(start_time)
        print(options['file_path'][0])
        print(options['sheet_name'][0])
        #data = pd.read_excel('/Users/santiagovinan/Downloads/data_empr.xlsx', sheet_name='survey')
        data = pd.read_excel(options['file_path'][0], 
            sheet_name=options['sheet_name'][0])
        data['18. Indique el número de mesas que posee el emprendimiento'] = data['18. Indique el número de mesas que posee el emprendimiento'].fillna(0)
        data['19. plazas'] = data['19. plazas'].fillna(0)
        data['24. Precio promedio'] = data['24. Precio promedio'].fillna(0.00)
        estabs = [
            Establecimiento(
                 nombre = row[7],
                 fecha = row[6],
                 ruc = row[8],
                 parroquia = row[9],
                 sector = row[10],
                 telefono = row[11],
                 email = row[12],
                 propietario = row[13],
                 tipo = row[14],
                 redes_sociales = row[16],
                 asociacion = row[17],
                 local = row[19],
                 equipos = row[20],
                 equipos_cocina = row[21],
                 servicios_complementarios = row[22],
                 numero_mesas = row[24],
                 plazas = row[25],
                 banio = row[26],
                 oferta = row[27],
                 tipo_servicio = row[28],
                 menu = row[29],
                 precio_promedio = row[30],
                 proceso = row[31],
                 materias_primas = row[32],
                 tipo_materia_prima = row[33],
                 numero_mujeres = row[34],
                 numero_hombres = row[35],
                 formacion_academica = row[36],
                 personal_capacitado = row[37],
                 frecuencia_capacitacion = row[38],
                 empleados_formacion = row[39],
                 licencia_anual = row[41],
                 url = row[42],
                 longitude = row[44],
                 latitude = row[45]
            )
            for i, row in data.iterrows()     
        ]
        Establecimiento.objects.bulk_create(estabs)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading xlsx file took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
        
