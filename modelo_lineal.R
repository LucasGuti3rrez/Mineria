library(tidyverse)

df = read.csv('csvlimpios/lluvia.csv',header = TRUE,sep = ",")

factor(df$zona)
factor(df$estacion)

names(df)
df$fecha = NULL
df$aÃ.o = NULL
df$mes = NULL
df$dia = NULL
df$nombreEstacion = NULL

df = tibble::rowid_to_column(df, "ID")

df = subset(df,lluvia == 1)

df$lluvia = NULL


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


datos_entrenamiento$ID = NULL
datos_validacion$ID = NULL
datos_prediccion$ID = NULL
#Forward and Backward

m0 = lm(mmAguaCaidadiaria ~ 1,data = datos_entrenamiento)

mcompleto = lm(mmAguaCaidadiaria ~ .,data = datos_entrenamiento)

formula_final = step(m0,direction = 'both',scope = formula(mcompleto), steps = 6)

formula_final = formula_final$call

#Ajustamos el modelo

modelo = lm(formula = formula_final, data = datos_entrenamiento)
summary(modelo)

predicciones = predict(object = modelo, newdata = datos_validacion)

datos_validacion$predict = predicciones
datos_validacion$comparacion = ( ((datos_validacion$predict + sqrt(var(datos_validacion$predict))) > datos_validacion$mmAguaCaidadiaria) &(datos_validacion$mmAguaCaidadiaria> datos_validacion$predict - sqrt(var(datos_validacion$predict))))


sum(datos_validacion$comparacion)/dim(datos_validacion)[1]


