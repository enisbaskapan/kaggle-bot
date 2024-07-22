import argparse
import json
import os

SETTINGS_FILE = '../settings/settings.json'

parser = argparse.ArgumentParser(description='Update configuration settings.')

parser.add_argument('-m', '--model', required=True, help='Model name')
parser.add_argument('-k', '--apikey', required=False, help='API key')
parser.add_argument('-p', '--provider', required=True, help='Provider name')

args = parser.parse_args()

if os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, 'r') as file:
        settings = json.load(file)
else:
    settings = {}

settings['model'] = args.model
settings['provider'] = args.provider

if args.apikey is not None:
    settings['api_key'] = args.apikey

with open(SETTINGS_FILE, 'w') as file:
    json.dump(settings, file, indent=4)

print("🔨 Settings updated successfully 🔨")
