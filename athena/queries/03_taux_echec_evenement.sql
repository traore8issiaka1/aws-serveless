SELECT type_evenement, COUNT(*) AS total,
       SUM(CASE WHEN statut='FAILED' THEN 1 ELSE 0 END) AS nb_echecs,
       ROUND(100.0*SUM(CASE WHEN statut='FAILED' THEN 1 ELSE 0 END)/COUNT(*),2) AS taux_echec_pct
FROM telecom_db.telecom
GROUP BY type_evenement
ORDER BY taux_echec_pct DESC;
