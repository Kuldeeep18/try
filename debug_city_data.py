#!/usr/bin/env python3
"""
Debug script to check city data in the database
"""

import sqlite3
import sys
sys.path.append('.')

from app import DATABASE

def debug_city_data():
    print("Debugging City Data...")
    print("=" * 50)
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    
    # Check if visits table has the new columns
    print("1. Checking visits table structure:")
    cursor = conn.execute("PRAGMA table_info(visits)")
    columns = cursor.fetchall()
    
    city_col_exists = False
    country_col_exists = False
    
    for col in columns:
        print(f"   - {col[1]} ({col[2]})")
        if col[1] == 'city':
            city_col_exists = True
        if col[1] == 'country':
            country_col_exists = True
    
    print(f"\nCity column exists: {city_col_exists}")
    print(f"Country column exists: {country_col_exists}")
    
    # Check total visits
    cursor = conn.execute("SELECT COUNT(*) as total FROM visits")
    total_visits = cursor.fetchone()[0]
    print(f"\nTotal visits in database: {total_visits}")
    
    if total_visits > 0:
        # Check visits with city data
        cursor = conn.execute("SELECT COUNT(*) as count FROM visits WHERE city IS NOT NULL AND city != 'Unknown'")
        city_visits = cursor.fetchone()[0]
        print(f"Visits with city data: {city_visits}")
        
        # Show sample visits
        print("\n2. Sample visits data:")
        cursor = conn.execute("SELECT region, city, country, ip_hash FROM visits LIMIT 5")
        visits = cursor.fetchall()
        
        for i, visit in enumerate(visits, 1):
            print(f"   Visit {i}:")
            print(f"     Region: {visit['region']}")
            print(f"     City: {visit['city']}")
            print(f"     Country: {visit['country']}")
            print(f"     IP Hash: {visit['ip_hash'][:10]}...")
        
        # Check city distribution query
        print("\n3. City distribution query results:")
        cursor = conn.execute("""
            SELECT city, country, COUNT(*) as count
            FROM visits
            WHERE city IS NOT NULL AND city != 'Unknown'
            GROUP BY city, country
            ORDER BY count DESC
            LIMIT 10
        """)
        
        city_data = cursor.fetchall()
        if city_data:
            for city in city_data:
                city_name = f"{city['city']}, {city['country']}" if city['country'] and city['country'] != 'Unknown' else city['city']
                print(f"   - {city_name}: {city['count']} visits")
        else:
            print("   No city data found!")
    
    conn.close()
    
    print("\n" + "=" * 50)
    print("Debug completed!")

if __name__ == "__main__":
    debug_city_data()