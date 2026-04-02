# 📡 AWS Serverless – Telecom Data Analytics

> Pipeline d'analyse Big Data des transactions télécom en Afrique de l'Ouest
> Stack : **Amazon S3 · AWS Glue · Amazon Athena · Amazon QuickSight**

## 🗂️ Structure du projet
cat > README.md << 'EOF'
# 📡 AWS Serverless – Telecom Data Analytics

> Pipeline d'analyse Big Data des transactions télécom en Afrique de l'Ouest
> Stack : **Amazon S3 · AWS Glue · Amazon Athena · Amazon QuickSight**

## 🗂️ Structure du projet
```
aws-serveless/
├── generate_data2.py
├── glue/
│   ├── scripts/
│   │   ├── glue_catalog_setup.py
│   │   └── glue_etl_csv_to_parquet.py
│   └── config/
│       └── crawler_config.json
├── athena/
│   ├── athena_runner.py
│   └── queries/
│       ├── 01_top10_antennes_data.sql
│       ├── 02_revenue_pays_operateur.sql
│       ├── 03_taux_echec_evenement.sql
│       ├── 04_momo_volume_par_heure.sql
│       ├── 05_distribution_appels_duree.sql
│       ├── 06_evolution_quotidienne.sql
│       ├── 07_detection_fraude_momo.sql
│       └── 08_parts_marche_momo.sql
└── docs/
    └── schema_architecture.md
```

## 💰 Modèle de coût Athena
- Tarif : 5 $ par téraoctet scanné
- Optimisation CSV → Parquet : économie de 60 à 90%

## 👤 Auteur
traore8issiaka1 – Projet Data Engineering Telecom
