#  AWS Serverless – Telecom Data Analytics

> Pipeline d'analyse Big Data des transactions télécom en Afrique de l'Ouest
> Stack : **Amazon S3 · AWS Glue · Amazon Athena · Amazon QuickSight**

##  Structure du projet
cat > README.md << 'EOF'
#  AWS Serverless – Telecom Data Analytics

> Pipeline d'analyse Big Data des transactions télécom en Afrique de l'Ouest
> Stack : **Amazon S3 · AWS Glue · Amazon Athena · Amazon QuickSight**

##  Structure du projet
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
##  Objectif du projet

Ce projet vise à mettre en place une architecture Big Data scalable et sans serveur permettant de :

- Stocker des données télécom massives
- Effectuer des transformations ETL
- Interroger les données via SQL
- Produire des analyses exploitables

L’objectif est de démontrer l’efficacité des services serverless pour le traitement de données à grande échelle.

##  Technologies utilisées

- AWS S3 (Stockage)
- AWS Glue (ETL / PySpark)
- AWS Athena (Requêtes SQL)
- Python (génération de données)
- SQL (analyse de données)
- Apache Parquet (format optimisé)

##  Pipeline de traitement

1. Génération des données avec Python  
2. Stockage des fichiers dans S3  
3. Transformation des données via AWS Glue  
4. Conversion en format Parquet  
5. Analyse des données avec AWS Athena (requêtes SQL)

##  Exemples d’analyses réalisées

- Analyse du trafic télécom
- Détection des anomalies
- Statistiques d’utilisation
- Agrégation des données par utilisateur ou région

##  Auteur
traore8issiaka1 – Projet Data Engineering Telecom
