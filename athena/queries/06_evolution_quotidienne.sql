SELECT date(date_heure) AS date_jour,
       COUNT(*) AS total_evenements
FROM telecom_db.telecom
GROUP BY date(date_heure)
ORDER BY date_jour;
