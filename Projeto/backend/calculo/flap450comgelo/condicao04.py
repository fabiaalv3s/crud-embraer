weight = float (input ("Weight: "))
alt = float (input ("Alt: "))
temp = float (input ("Temp: "))
wind = float (input ("Wind: "))
wind2 = int (input("1 - head wind or 2 - tail wind:"))
if wind2 == 1 or wind2 == 2:
    slope = float (input ("Slope: "))
    slope2 = int (input("1 - uphill or 2 - downhill: "))
    if slope2 == 1 or slope2 == 2:
        vap = float (input ("Vap : "))
        reversor = int (input ("Está usando reversor? 1-sim / 2-nao "))
        if reversor == 1 or reversor == 2:

            isa = temp - 15
            qtdAbaixo = 18-weight
            qtdAcima = weight - 18

            #condicao 1 1 1 peso <= 18
            if (wind2 ==  1  and reversor == 1 and weight <= 18 and slope2 == 1):
                    
                calculo = (1399 - ((60 * qtdAbaixo)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) + 372)
                        
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 1 1 1 peso > 18
            if (wind2 ==  1  and reversor == 1 and weight > 18 and slope2 == 1):
                    
                calculo = (1399 + ((59 * qtdAcima)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) + 372)
                        
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 1 1 2 peso > 18
            if (wind2 ==  1  and reversor == 1 and weight > 18 and slope2 == 2):
                    
                calculo = (1399 + ((59 * qtdAcima)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) + 372)
                        
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 1 1 2 peso <= 18
            if (wind2 ==  1  and reversor == 1 and weight <= 18 and slope2 == 2):
                    
                calculo = (1399 - ((60 * qtdAcima)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) + 372)
                        
                print ("Sera necessario: ", calculo, "mts para pousar")

            #condicao 1 2 1 peso > 18
            if (wind2 ==  1  and reversor == 2 and weight > 18 and slope2 == 1):
                    
                calculo = (1399 + ((59 * qtdAcima)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) )
                        
                print ("Sera necessario: ", calculo, "mts para pousar")

            #condicao 1 2 1 peso <= 18
            if (wind2 ==  1  and reversor == 2 and weight <= 18 and slope2 == 1):
                    
                calculo = (1399 + ((59 * qtdAbaixo)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) )
                        
                print ("Sera necessario: ", calculo, "mts para pousar")

            #condicao 1 2 2 peso > 18
            if (wind2 ==  1  and reversor == 2 and weight > 18 and slope2 == 2):

                calculo = (1399 + ((59 * qtdAcima)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5)  (154 * slope)/100 + ((107 * vap)/5) )
                        
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 1 2 2 peso <= 18
            if (wind2 ==  1  and reversor == 2 and weight <= 18 and slope2 == 2):
                    
                calculo = (1399 - ((60 * qtdAbaixo)/1) + ((42 * alt)/1000) - ((15 * temp)/5)
                - ((31 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) )
                        
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 2 2 peso > 18            
            if (wind2 ==  2  and reversor == 2 and weight > 18 and slope2 == 2):
                        
                calculo = (1399 + ((59 * qtdAcima)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) )
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 2 2 peso <= 18            
            if (wind2 ==  2  and reversor == 2 and weight <= 18 and slope2 == 2):
                        
                calculo = (1399 - (( 60 * qtdAbaixo)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) )
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 2 1 peso <= 18            
            if (wind2 ==  2  and reversor == 2 and weight <= 18 and slope2 == 1):
                        
                calculo = (1399 - (( 60 * qtdAbaixo)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) )
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 2 1 peso > 18            
            if (wind2 ==  2  and reversor == 2 and weight > 18 and slope2 == 1):
                        
                calculo = (1399 + (( 59 * qtdAcima)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) )
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 1 2 peso > 18            
            if (wind2 ==  2  and reversor == 1 and weight > 18 and slope2 == 2):
                        
                calculo = (1399 + (( 59 * qtdAcima)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) + 372)
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 1 2 peso <= 18            
            if (wind2 ==  2  and reversor == 1 and weight <= 18 and slope2 == 2):
                        
                calculo = (1399 - (( 60 * qtdAbaixo)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) + (154 * slope)/100 + ((107 * vap)/5) + 372)
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 1 1 peso <= 18            
            if (wind2 ==  2  and reversor == 1 and weight <= 18 and slope2 == 1):
                        
                calculo = (1399 - (( 60 * qtdAbaixo)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) + 372)
                print ("Sera necessario: ", calculo, "mts para pousar")
                
            #condicao 2 1 1 peso > 18            
            if (wind2 ==  2  and reversor == 1 and weight > 18 and slope2 == 1):
                        
                calculo = (1399 + (( 59 * qtdAcima)/1) + ((42 * alt)/1000) + ((35 * temp)/5)
                + ((143 * wind)/5) - (15 * slope)/100 + ((107 * vap)/5) + 372)
                print ("Sera necessario: ", calculo, "mts para pousar")
            
        else:
            print("escolha uma opção válida!")   
    else:
        print("escolha uma opção válida!")           
else:
    print("escolha uma opção válida!")