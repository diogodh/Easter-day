#lua 29.53 dias ; 
#10 jan as 19.21h (235.35h)

#lua = 235.35 (29.53 dias)
#lua_x = 235.35 + 708.72 * x
#1 ano = 8765.8128
#10 anos = 8765.8128

#domingo_x = 96 + 168 * x

x = y = domingo = lua = 0
equinox = 1899.83
ano = 8765.8128

ano_pascoa = int(input("Ano: "))
dif_ano = ano_pascoa - 2020
horas_ano = ano + ano * dif_ano
equinox_ano = equinox + ano * dif_ano

while lua < equinox_ano:
	lua = 235.35 + 708.72 * x
	x = x + 1
	
while domingo < lua:
	domingo = 96 + (168 * y)
	y = y + 1

dia = domingo / 24
dia_ano = dia - 365 * dif_ano

if dia_ano > 120.25:
    mes = "Maio"
    dia_ano2 = dia_ano - 120.25
elif dia_ano > 90.25:
    mes = "Abril"
    dia_ano2 = dia_ano - 90.25
elif dia_ano > 59.25:
    mes = "Marco"
    dia_ano2 = dia_ano

print("Dia", int(round(dia_ano2)), "de", mes, "de", ano_pascoa)
