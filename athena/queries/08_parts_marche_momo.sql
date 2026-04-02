SELECT operateur,
       COUNT(*) AS nb_transactions,
       ROUND(SUM(montant_xof),0) AS revenu_total_xof
FROM telecom_db.telecom
WHERE type_evenement='MOMO' AND statut='SUCCESS'
GROUP BY operateur
ORDER BY revenu_total_xof DESC;
