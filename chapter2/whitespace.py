print("Python")

print("\tPython")

print("Languages:\nPython\nC\nJavascript")

print("Languages:\n\tPython\n\tC\n\tJavascript")

favorite_language = ' python '
rstrip_favorite_language = favorite_language.rstrip()
print(f"My favorite language is{rstrip_favorite_language}.")
lstrip_favorite_language = favorite_language.lstrip()
print(f"My favorite language is{lstrip_favorite_language}.")
strip_favorite_language = favorite_language.strip()
print(f"My favorite language is{strip_favorite_language}.")

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)