######## R com MongoDB ######## 
install.packages("rmongodb")
library(rmongodb)

#Estabelecendo a conexão com o banco (localhost)

mongo <- mongo.create()
mongo

mongo.is.connected(mongo)

#Listando as bases
mongo.get.databases(mongo)

#Listando as collections
if(mongo.is.connected(mongo) == TRUE) {
  db <- "stocks"
  mongo.get.database.collections(mongo, db)
  collection <- mongo.get.database.collections(mongo, db)
}

#Conta a quantidade de documentos
mongo.count(mongo, collection)

#Retorna 1 documento
mongo.find.one(mongo, collection)

#Retornar todos os valores de TRPN3
mongo.find(mongo, collection, '{"acao":"TRPN3"}')

cotacao <- vector() 
cursor <- mongo.find(mongo, collection, '{"acao":"TRPN3"}')
while (mongo.cursor.next(cursor)) {
  val <- mongo.cursor.value(cursor)
  cotacao[length(cotacao)+1] <- mongo.bson.value(val, "cotacao")
}
cotacao
plot(cotacao,ylim = c(12.1,14.5),type='l',main = 'Cotação da TRPN3\nvia MongoDB')


#Retornando as datas
data <- vector() 
cursor <- mongo.find(mongo, collection, '{"acao":"TRPN3"}')
while (mongo.cursor.next(cursor)) {
  val <- mongo.cursor.value(cursor)
  data[length(data)+1] <- mongo.bson.value(val, "data")
}

#Converte o formato string para Date
data <- as.Date(data,format="%Y-%m-%d")
plot(data,cotacao, main = "Cotação da TRPN3\nvia MongoDB",
        xlab="Data", ylab="Cotação",
        col=ifelse(cotacao>mean(cotacao),"blue", "red"),
        ylim = c(12.1,14.5))
