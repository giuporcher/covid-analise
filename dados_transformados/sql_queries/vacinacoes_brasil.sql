SELECT
  FORMAT_DATE("%d-%m-%Y", EXTRACT(DATE from _source.vacina_dataAplicacao)) as vacina_data_aplicacao,
  FORMAT_DATE("%d-%m-%Y", _source.paciente_dataNascimento) as data_nascimento,
  _source.paciente_idade as idade,
  _source.vacina_grupoAtendimento_nome as grupo_atendimento,
  _source.paciente_enumSexoBiologico as sexo,
  _source.paciente_racaCor_valor AS paciente_cor_raca,
  _source.paciente_endereco_nmPais as paciente_pais,
  _source.paciente_endereco_uf as paciente_endereco_uf,
  _source.vacina_fabricante_nome as fabricante_vacina,
  _source.vacina_descricao_dose as vacina_dose,
FROM
  `wide-exchanger-367908.Covid_Dados.covid_vacinacoes_brasil`
ORDER BY idade DESC