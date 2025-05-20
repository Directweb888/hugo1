import os
import yaml
import shutil

BASE_DIR = "."
BRAND_DIR = os.path.join(BASE_DIR, "data", "brands")

for filename in os.listdir(BRAND_DIR):
    if filename.endswith(".yaml"):
        brand = filename.replace(".yaml", "")
        with open(os.path.join(BRAND_DIR, filename)) as f:
            data = yaml.safe_load(f)

        build_path = f"build/{brand}"
        os.makedirs(build_path, exist_ok=True)
        shutil.copytree(".", build_path, dirs_exist_ok=True, ignore=shutil.ignore_patterns('build', 'dist', '.git', '__pycache__'))

        config_path = os.path.join(build_path, "config.toml")
        with open(config_path, "w") as out:
            out.write(f'''
baseURL = "https://{brand}.yourdomain.com/"
languageCode = "th"
title = "{data['brand_name']}"

[params]
brand_name = "{data['brand_name']}"
description = "{data['description']}"
cta_text = "{data['cta_text']}"
cta_link = "{data['cta_link']}"
logo_url = "{data['logo_url']}"
primary_color = "{data['primary_color']}"
''')
        print(f"Ready to build Hugo site for {brand} at {build_path}")