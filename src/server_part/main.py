from settings import Settings, SettingsVariations

from test import get

Settings.declare_env(SettingsVariations.prod)
print(Settings.get_settings())
print()
get()
