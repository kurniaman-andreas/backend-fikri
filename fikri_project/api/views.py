from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.db import connection

def get_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM data_kbri")  # Sesuaikan dengan nama tabel
        rows = cursor.fetchall()
    
    # Menentukan nama kolom sesuai dengan tabel Anda
    data = []
    for row in rows:
        data.append({
            "id_perwakilan": row[0],  
            "perwakilan": row[1],      
            "alamat": row[2],          
            "telepon": row[3],         
            "situs_web": row[4],       
            "negara": row[5]           
        })
    
    return JsonResponse(data, safe=False)
