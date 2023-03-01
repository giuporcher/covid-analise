SELECT
  country AS Pais,
  confirmed AS Casos,
  deaths AS Mortes,
  ROUND(deaths / confirmed, 3) as porcentagem_mortes
FROM
  `wide-exchanger-367908.Covid_Dados.covid_dados_mundo`
ORDER BY
  porcentagem_mortes DESC;
