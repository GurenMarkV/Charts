from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv
from django.contrib.auth.models import User

import matplotlib.pyplot as plt,mpld3
#import numpy as np
#import mpld3

#plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
#mpld3.show()

from django.views.generic import View, TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

def capture(request):
    data = {
        "Temp": 30,
        "Altitude": 5300,
    }
    return JsonResponse(data)

class HomeView(TemplateView):
    #def get(self, request, *args, **kwargs):
     #   return render(request, 'charts.html')

    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['time'] = self.reader()[0]
        context['meter'] = self.reader()[1]
        context['pressure'] = self.reader()[2]

        context['accx'] = self.reader()[3]
        context['accy'] = self.reader()[4]
        context['accz'] = self.reader()[5]

        context['gx'] = self.reader()[6]
        context['gy'] = self.reader()[7]
        context['gz'] = self.reader()[8]

        context['gyx'] = self.reader()[9]
        context['gyy'] = self.reader()[10]
        context['gyz'] = self.reader()[11]

        context['temp'] = self.reader()[12]
        context['temp2'] = self.reader()[13]
        return context

    #G:/My Drive/WINTER_2018/Capstone/Charts/temp/arduino.csv
    #C:/Users/Talha/Google Drive/WINTER_2018/Capstone/Charts/temp/arduino.csv

    def reader(self):
        time_data = []
        temp_data = []
        temp2 = []

        alt_data = []
        psi_data = []

        accelo_x = []
        accelo_y = []
        accelo_z = []

        gravity_x = []
        gravity_y = []
        gravity_z = []
            
        gyro_x = []
        gyro_y = []
        gyro_z = []


        location = csv.reader(open("G:/My Drive/WINTER_2018/Capstone/Charts/temp/arduino.csv"),delimiter=",")
        next(location)

        for i in location:

            psi_data.append(float(i[26]))
            time_data.append(float(i[29]))
            alt_data.append(float(i[30]))

            accelo_x.append(float(i[8]))
            accelo_y.append(float(i[9]))
            accelo_z.append(float(i[10]))

            gravity_x.append(float(i[15]))
            gravity_y.append(float(i[16]))
            gravity_z.append(float(i[17]))

            gyro_x.append(float(i[20]))
            gyro_y.append(float(i[21]))
            gyro_z.append(float(i[22]))
           
            temp_data.append(float(i[25]))
            temp2.append(float(i[23]))

           
        return time_data, alt_data, psi_data, accelo_x, accelo_y, accelo_z, gravity_x, gravity_y, gravity_z, gyro_x, gyro_y, gyro_z, temp_data, temp2





