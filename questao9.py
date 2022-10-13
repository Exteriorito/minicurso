teste1=[-5,-12,0,6]
teste2=[35,-35,5,100,100,50,50]

resultado1=[]
resultado2=[]

temperaturas1=len(teste1)
temperaturas2=len(teste2)

intervalo1=2
intervalo2=4

for i in range ((temperaturas1+1)-intervalo1):
	soma=0
	for j in range (i,i+intervalo1):
    	soma=soma+teste1[j]
   	 
	media=soma/intervalo1
	media=round(media)
	resultado1.append(media)
   	 
for i in range ((temperaturas2+1)-intervalo2):
	soma=0
	for j in range (i,i+intervalo2):
    	soma=soma+teste2[j]
    
	media=soma/intervalo2
	media=round(media)
	resultado2.append(media)
