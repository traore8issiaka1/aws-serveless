SELECT CASE
  WHEN duree_secondes < 60   THEN 'Moins de 1 min'
  WHEN duree_secondes <= 300 THEN '1 a 5 min'
  ELSE 'Plus de 5 min'
END AS categorie, COUNT(*) AS nb_appels
FROM telecom_db.telecom
WHERE type_evenement='CALL'
GROUP BY 1
ORDER BY nb_appels DESC;
