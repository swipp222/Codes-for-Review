#!/usr/bin/env python3
#automatically download HYCOM data
from pylib import *
close("all")

#--------------------------------------------------------------------
#input
#--------------------------------------------------------------------
StartT,EndT=datenum(2021,6,1),datenum(2021,10,1)
xm=[-100,0]; ym=[0,80]
sdir='.'

#database
url_1='https://tds.marine.rutgers.edu/thredds/roms/doppio/ncss/grid/roms/doppio/'
database=['DopAnV3R3-ini2007_da/his',]

#download hycom data
if not os.path.exists(sdir): os.mkdir(sdir)
for ti in arange(StartT,EndT):
    url='{}/{}?'.format(url_1,database)

    #add variables
    for i in ['zeta','salt','temp','u','v']: url=url+'var={}&'.format(i)

    #add domain
    for i,k in zip(['south','north','west','east'],[*ym,*xm]): url=url+'{}={}&'.format(i,k)

    #horizontal stride and time
    for n in arange(0,24,3):
        fname='{}/hycom_{}_{:02}.nc'.format(sdir,num2date(ti).strftime('%Y_%m_%d'),n)
        furl=url+'horizStride=1&time={}T{:02}%%3A00%3A00Z&timeStride=1&vertCoord=&accept=netcdf4'.format(num2date(ti).strftime('%Y-%m-%d'),n)

        #download doppio data
        if os.path.exists(fname): continue
        try:
           urllib.request.urlretrieve(furl,fname)
           print(fname)
        except:
           pass

print('Done-----------')
