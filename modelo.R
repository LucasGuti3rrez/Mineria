library(tidyverse)

df = read.csv('csvlimpios/lluvia.csv',header = TRUE,sep = ",")

factor(df$zona)
factor(df$estacion)

df.grupo1 = subset(df, grupo == 1)
df.grupo2 = subset(df, grupo == 2)

names(df)

#Forward and Backward

m0 = glm(lluvia ~ 1,data = df.grupo1, family ='binomial')

mcompleto = glm(lluvia ~ zona + TemperaturaMax + TemperaturaMin + HumedadRelativaMax + HumedadRelativaMin + PresionAtmosfericaMax + PresionAtmosfericaMin + TemperaturarocioMax + TemperaturarocioMin + VelocidadvientoMax + VelocidadvientoMin,data = df.grupo1, family ='binomial')

step(m0,direction = 'both',scope = formula(mcompleto))

#Ajustamos el modelo

modelo = glm(formula = lluvia ~ zona + HumedadRelativaMin + HumedadRelativaMax + 
               PresionAtmosfericaMin + TemperaturaMax + TemperaturaMin + 
               TemperaturarocioMax + PresionAtmosfericaMax + VelocidadvientoMax + 
               TemperaturarocioMin, family = "binomial", data = df.grupo1)

## Prediccion ##

#datos con los que ajustamos el modelo

predicciones.grupo1 = predict(object = modelo, newdata = df.grupo1, type = 'response')

predicciones.grupo1 = ifelse(predicciones.grupo1>0.5,yes = 1,no=0)

df.grupo1$predict = predicciones.grupo1

df.grupo1$comparacion = (df.grupo1$lluvia == df.grupo1$predict)*1

#Exactitud

sum(df.grupo1$comparacion)/dim(df.grupo1)[1]

#Precision

df.grupo1.lluvia.pred = subset(df.grupo1, predict == 1)

sum(df.grupo1.lluvia.pred$comparacion)/dim(df.grupo1.lluvia.pred)[1]

#Deteccion

df.grupo1.lluvia = subset(df.grupo1, lluvia == 1)

sum(df.grupo1.lluvia$comparacion)/dim(df.grupo1.lluvia)[1]

#Falsa alarma

df.grupo1.nolluvia.pred = subset(df.grupo1, lluvia == 0)

sum(1 - df.grupo1.nolluvia.pred$comparacion)/dim(df.grupo1.nolluvia.pred)[1]

#################################################################################

#datos diferentes a los que utilizamos para ajustar el modelo

predicciones.grupo2 = predict(object = modelo, newdata = df.grupo2, type = 'response')

predicciones.grupo2 = ifelse(predicciones.grupo2>0.5,yes = 1,no=0)

df.grupo2$predict = predicciones.grupo2

df.grupo2$comparacion = (df.grupo2$lluvia == df.grupo2$predict)

#Exactitud

sum(df.grupo2$comparacion)/dim(df.grupo2)[1]

#Precision

df.grupo2.lluvia.pred = subset(df.grupo2, predict == 1)

sum(df.grupo2.lluvia.pred$comparacion)/dim(df.grupo2.lluvia.pred)[1]

#Deteccion

df.grupo2.lluvia = subset(df.grupo2, lluvia == 1)

sum(df.grupo2.lluvia$comparacion)/dim(df.grupo2.lluvia)[1]

#Falsa alarma

df.grupo2.nolluvia.pred = subset(df.grupo2, lluvia == 0)

sum(1 - df.grupo2.nolluvia.pred$comparacion)/dim(df.grupo2.nolluvia.pred)[1]

###############################################################################





