SELECT pays, operateur,
       COUNT(*) AS nb_transactions,
       ROUND(SUM(montant_xof),2) AS revenue_total_xof
FROM telecom_db.telecom
WHERE statut = 'SUCCESS'
GROUP BY pays, operateur
ORDER BY pays, revenue_total_xof DESC;
