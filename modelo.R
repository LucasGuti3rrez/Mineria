library(tidyverse)

df = read.csv('csvlimpios/lluvia.csv',header = TRUE,sep = ",")

factor(df$zona)
factor(df$estacion)

names(df)

df = tibble::rowid_to_column(df, "ID")

df$lluvia = ifelse(df$mmAguaCaidadiaria>0,yes = 1,no=0)
#Dividimos los datos

cant_datos = dim(df)[1]

cant_entrenamiento = round(cant_datos * 0.7,0)

cant_validacion = round(cant_datos * 0.2,0)

cant_prediccion = round(cant_datos * 0.1,0)

cant_entrenamiento + cant_validacion + cant_prediccion

#Conjunto de datos entrenamiento
datos_entrenamiento = df[sample(nrow(df), size = cant_entrenamiento ),]

df_recortada = subset(df, !(ID %in% datos_entrenamiento$ID))

#Conjunto de datos validacion
datos_validacion = df_recortada[sample(nrow(df_recortada), size = cant_validacion ),]

df_recortada = subset(df_recortada, !(ID %in% datos_validacion$ID))


#Conjunto de datos prediccion
datos_prediccion = df_recortada

datos_prediccion$lluvia = NULL

datos_prediccion$mmAguaCaidadiaria = NULL

#Matriz correlaciones

cor(df[,4:20]) 

#Forward and Backward

m0 = glm(lluvia ~ 1,data = datos_entrenamiento, family ='binomial')

mcompleto = glm(lluvia ~ zona + TemperaturaMax + TemperaturaMin + HumedadRelativaMax + HumedadRelativaMin + PresionAtmosfericaMax + PresionAtmosfericaMin + TemperaturarocioMax + TemperaturarocioMin + VelocidadvientoMax + VelocidadvientoMin + estacion,data = datos_entrenamiento, family ='binomial')

formula_final = step(m0,direction = 'both',scope = formula(mcompleto))

formula_final = formula_final$formula


#Ajustamos el modelo

modelo = glm(formula = formula_final, family = "binomial", data = datos_entrenamiento)
?glm


#################################################################################
########################## Validacion del modelo ################################
#################################################################################

predicciones.validacion = predict(object = modelo, newdata = datos_validacion, type = 'response')

predicciones.validacion = ifelse(predicciones.validacion>=0.5,yes = 1,no=0)

datos_validacion$predict = predicciones.validacion

datos_validacion$comparacion = (datos_validacion$lluvia == datos_validacion$predict)

#Exactitud

sum(datos_validacion$comparacion)/dim(datos_validacion)[1]

#Precision

datos_validacion.lluvia.pred = subset(datos_validacion, predict == 1)

sum(datos_validacion.lluvia.pred$comparacion)/dim(datos_validacion.lluvia.pred)[1]

#Deteccion

datos_validacion.lluvia = subset(datos_validacion, lluvia == 1)

sum(datos_validacion.lluvia$comparacion)/dim(datos_validacion.lluvia)[1]

#Falsa alarma

datos_validacion.nolluvia.pred = subset(datos_validacion, lluvia == 0)

sum(1 - datos_validacion.nolluvia.pred$comparacion)/dim(datos_validacion.nolluvia.pred)[1]

#################################################################################
################################ Prediccion #####################################
#################################################################################
unique(datos_prediccion$nombreEstacion)
df_rancagua = subset(datos_prediccion,nombreEstacion == 'Rancagua')
