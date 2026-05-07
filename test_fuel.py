import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from routes.services.fuel_service import fuel_df

print(fuel_df.head())
print(fuel_df.columns)