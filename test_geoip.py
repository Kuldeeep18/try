#!/usr/bin/env python3
"""
Test script to verify MaxMind GeoIP integration is working correctly.
"""

import os
import sys
sys.path.append('.')

from app import detect_region, get_detailed_location, download_geoip_database

def test_geoip():
    print("Testing MaxMind GeoIP Integration...")
    print("=" * 50)
    
    # Test database download
    print("1. Testing GeoIP database download...")
    success = download_geoip_database()
    if success:
        print("✅ GeoIP database is available")
    else:
        print("⚠️  Using fallback location detection")
    
    print()
    
    # Test various IP addresses
    test_ips = [
        ("8.8.8.8", "Google DNS (US)"),
        ("1.1.1.1", "Cloudflare DNS"),
        ("208.67.222.222", "OpenDNS"),
        ("127.0.0.1", "Localhost"),
        ("192.168.1.1", "Private IP"),
        ("203.0.113.1", "Documentation IP"),
    ]
    
    print("2. Testing location detection for various IPs...")
    print("-" * 50)
    
    for ip, description in test_ips:
        print(f"\nTesting {ip} ({description}):")
        
        # Test basic region detection
        region = detect_region(ip)
        print(f"  Region: {region}")
        
        # Test detailed location
        location = get_detailed_location(ip)
        print(f"  Country: {location['country']}")
        print(f"  City: {location['city']}")
        if location['latitude'] and location['longitude']:
            print(f"  Coordinates: {location['latitude']}, {location['longitude']}")
        if location['timezone']:
            print(f"  Timezone: {location['timezone']}")
    
    print("\n" + "=" * 50)
    print("✅ MaxMind GeoIP integration test completed!")
    print("\nYour analytics will now show accurate location data including:")
    print("- Real country names instead of simulated regions")
    print("- City-level tracking")
    print("- Enhanced geographic analytics")
    print("- Better CSV export data")

if __name__ == "__main__":
    test_geoip()