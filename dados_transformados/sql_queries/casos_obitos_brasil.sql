SELECT
  uf as UF,
  state as Estado,
  cases as Casos,
  deaths as Mortes,
  ROUND(deaths / cases, 3) as porcentagem_mortes
FROM
  `wide-exchanger-367908.Covid_Dados.covid_dados_brasil`
ORDER BY Casos DESC