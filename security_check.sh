#!/bin/bash

# Define the target website URL
website_url="http://example.com"

# Function to perform security checks
perform_security_checks() {
    echo "Performing security checks for $website_url..."
    echo ""

    # Check for HTTP response headers
    echo "Checking HTTP response headers..."
    curl -I $website_url

    # Check for common vulnerabilities using Nikto
    echo ""
    echo "Scanning for common vulnerabilities using Nikto..."
    nikto -h $website_url

    # Check for open ports using Nmap
    echo ""
    echo "Scanning for open ports using Nmap..."
    nmap $website_url

    # Add more security checks as needed

    echo ""
    echo "Security checks completed."
}

# Main script
perform_security_checks
