from django.core.management.base import BaseCommand, CommandError
from main_app.models import Country
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://restcountries.com/v3.1/all'
        response = requests.get(url)
        error = ""
        if response.status_code == 200:
            data = response.json()
            for country in data:
                country = Country(
                    official_name=country['name']['official'],
                    common_name=country['name']['common'],
                    region=country['region'],
                    subregion=country.get('subregion', 'unknown'),
                    capital=country.get('capital', 'unknown')[0],
                    independent=country.get('independent', 'unknown'),
                    population=country['population'],
                    area=country['area'],
                    google_maps=country.get('maps').get('googleMaps'),
                    currencies=", ".join(list(country.get('currencies', {}).keys())),
                    languages=", ".join(list(country.get('languages', {}).values())),
                    flag_png=country.get('flags').get('png'),
                    flag_alt=country.get('flags').get('alt', 'unknown')
                )
                country.save()
        else:
            error = 'Error occurred while fetching data from the API'

            self.stdout.write(
                self.style.SUCCESS(f'Finished data population. If error: {error}')
            )