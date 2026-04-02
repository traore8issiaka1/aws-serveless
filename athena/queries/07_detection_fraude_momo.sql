SELECT msisdn, date(date_heure) AS date_jour,
       COUNT(*) AS nb_transactions_momo
FROM telecom_db.telecom
WHERE type_evenement='MOMO' AND statut='SUCCESS'
GROUP BY msisdn, date(date_heure)
HAVING COUNT(*) > 10
ORDER BY nb_transactions_momo DESC
LIMIT 50;
