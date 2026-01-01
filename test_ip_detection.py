#!/usr/bin/env python3
"""
Test script to verify IP detection and GeoIP functionality.
"""

import sys
sys.path.append('.')

from app import get_client_ip, detect_region, get_detailed_location
from flask import Flask, request

def test_ip_detection():
    print("Testing IP Detection and GeoIP...")
    print("=" * 50)
    
    # Test various IP addresses
    test_ips = [
        ("8.8.8.8", "Google DNS (US)"),
        ("1.1.1.1", "Cloudflare DNS"),
        ("208.67.222.222", "OpenDNS"),
        ("94.130.180.12", "European IP"),
        ("203.0.113.1", "Documentation IP"),
        ("127.0.0.1", "Localhost"),
        ("192.168.1.1", "Private IP"),
        ("10.0.0.1", "Private IP"),
    ]
    
    print("Testing location detection for various IPs...")
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
    print("✅ IP detection test completed!")
    print("\nTo test on your live site:")
    print("1. Visit: https://yourdomain.com/debug-ip")
    print("2. Check what IP is being detected")
    print("3. Remove the /debug-ip route after testing")

if __name__ == "__main__":
    test_ip_detection()