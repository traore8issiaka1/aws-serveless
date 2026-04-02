SELECT antenne_id, pays,
       COUNT(*) AS nb_transactions,
       ROUND(SUM(volume_mb),2) AS volume_total_mb
FROM telecom_db.telecom
WHERE type_evenement = 'DATA' AND statut = 'SUCCESS'
GROUP BY antenne_id, pays
ORDER BY volume_total_mb DESC
LIMIT 10;
