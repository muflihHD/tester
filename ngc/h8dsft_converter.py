def converter(suhu_derajat,satuan_awal,satuan_akhir):
    suhu_akhir = 0
    if satuan_awal=='celcius':
        if satuan_akhir=='farhenheit':
            suhu_akhir=(suhu_derajat*1.8)+32
            return suhu_akhir
        if satuan_akhir=='kelvin':
            suhu_akhir=suhu_derajat+273.15
            return suhu_akhir
    if satuan_awal=='kelvin':
        if satuan_akhir=='farnhenheit':
            suhu_akhir=((suhu_derajat-273.15)*1.8)+32
            return suhu_akhir
        if satuan_akhir=='celcius':
            suhu_akhir=suhu_derajat-273.15
            return suhu_akhir
    if satuan_awal=='farhenheit':
        if satuan_akhir=='celcius':
            suhu_akhir=(suhu_derajat - 32)*0.56
            return suhu_akhir
        if satuan_akhir=='kelvin':
            suhu_akhir=((suhu_derajat - 32)*0.56)+273.15
    else:
        suhu_akhir='salah input'
        return suhu_akhir
        
print(converter(100,'celciu','kelvin'))