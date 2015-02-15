install.packages("arules")
library(arules)

#Para criar um dataset de teste
t= 100
set.seed(2015)
transacoes <- data.frame(DVD = rbinom(t, 1, .7)
                      , GELADEIRA = rbinom(t, 1, .3)
                      , LIVRO = rbinom(t, 1, .9)
                      , CELULAR = rbinom(t, 1, .6)
                      )


regras <- apriori(as.matrix(transacoes)
                 ,parameter=list(confidence=0.5,support=0.5))

# Para ordenar as regras
regras <- sort(regras,by="support")

# O inspect exibe as regras, neste caso ordenando pela confiança
inspect(sort(head(regras,10),decreasing=T, by="confidence") )

#Para converter o conjunto de regras em um dataframe
regras_df = data.frame(
  lhs = labels(lhs(regras))$elements, #lhs -> antecedente
  rhs = labels(rhs(regras))$elements, #rhs -> consequente
  regras@quality)

head(regras_df,10)

?apriori
