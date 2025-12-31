import sqlite3

conn = sqlite3.connect('smart_links.db')
cursor = conn.cursor()

# Check all links
cursor.execute('SELECT code, behavior_rule FROM links ORDER BY created_at DESC LIMIT 10')
results = cursor.fetchall()

print('Recent links in database:')
for row in results:
    print(f'  Code: {row[0]}, Rule: {row[1]}')

# Check for any remaining password-protected links
cursor.execute("SELECT code, behavior_rule FROM links WHERE behavior_rule = 'password_protected'")
pwd_results = cursor.fetchall()

print('\nPassword-protected links:')
if pwd_results:
    for row in pwd_results:
        print(f'  Code: {row[0]}, Rule: {row[1]}')
else:
    print('  ✅ No password-protected links found (feature removed)')

# Show available behavior rules
cursor.execute("SELECT DISTINCT behavior_rule FROM links")
rules = cursor.fetchall()
print(f'\nAvailable behavior rules: {", ".join([rule[0] for rule in rules])}')

conn.close()