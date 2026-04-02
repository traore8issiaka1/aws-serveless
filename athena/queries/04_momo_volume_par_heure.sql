SELECT hour(date_heure) AS heure,
       COUNT(*) AS nb_transactions,
       ROUND(SUM(montant_xof),2) AS volume_xof
FROM telecom_db.telecom
WHERE type_evenement='MOMO' AND statut='SUCCESS'
GROUP BY hour(date_heure)
ORDER BY heure;
