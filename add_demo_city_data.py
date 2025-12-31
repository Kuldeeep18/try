#!/usr/bin/env python3
"""
Add demo city data to show how city analytics will look
"""

import sqlite3
import random
import sys
sys.path.append('.')

from app import DATABASE

def add_demo_city_data():
    print("Adding Demo City Data...")
    print("=" * 40)
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    
    # Sample cities with their countries
    demo_cities = [
        ("New York", "United States", 40.7128, -74.0060),
        ("London", "United Kingdom", 51.5074, -0.1278),
        ("Tokyo", "Japan", 35.6762, 139.6503),
        ("Paris", "France", 48.8566, 2.3522),
        ("Sydney", "Australia", -33.8688, 151.2093),
        ("Toronto", "Canada", 43.6532, -79.3832),
        ("Berlin", "Germany", 52.5200, 13.4050),
        ("Mumbai", "India", 19.0760, 72.8777),
        ("São Paulo", "Brazil", -23.5505, -46.6333),
        ("Dubai", "United Arab Emirates", 25.2048, 55.2708),
    ]
    
    # Get some visits to update with city data
    cursor = conn.execute("""
        SELECT id FROM visits 
        WHERE country IS NOT NULL 
        ORDER BY RANDOM() 
        LIMIT 50
    """)
    
    visits_to_update = cursor.fetchall()
    print(f"Updating {len(visits_to_update)} visits with demo city data...")
    
    updated_count = 0
    
    for visit in visits_to_update:
        visit_id = visit['id']
        
        # Randomly select a demo city
        city, country, lat, lng = random.choice(demo_cities)
        
        # Update the visit with city data
        conn.execute("""
            UPDATE visits 
            SET city = ?, country = ?, latitude = ?, longitude = ?
            WHERE id = ?
        """, [city, country, lat, lng, visit_id])
        
        updated_count += 1
    
    conn.commit()
    
    print(f"✅ Updated {updated_count} visits with demo city data!")
    
    # Verify the update
    cursor = conn.execute("SELECT COUNT(*) as count FROM visits WHERE city IS NOT NULL AND city != 'Unknown'")
    city_visits = cursor.fetchone()[0]
    print(f"Total visits with city data: {city_visits}")
    
    # Show city distribution
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
        print("\nDemo city distribution:")
        for city in city_data:
            city_name = f"{city['city']}, {city['country']}"
            print(f"   - {city_name}: {city['count']} visits")
    
    conn.close()
    print("\n" + "=" * 40)
    print("✅ Demo city data added! Check your analytics now.")

if __name__ == "__main__":
    add_demo_city_data()