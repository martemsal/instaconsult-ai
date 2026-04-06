import os
import requests

SUPABASE_URL = "https://aokhxnwaqhdokgncfejn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFva2h4bndhcWhkb2tnbmNmZWpuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NTQ5MTQ5MywiZXhwIjoyMDkxMDY3NDkzfQ.Ey6JMQoiFL9Hoj4wCxZ-6vhix3Ptcv-UAX21FjRZpXw"

def setup_database():
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    # SQL to create tables via the SQL REST API is not directly possible like this, 
    # but we can try to initialize some data or use the SQL Editor if needed.
    # However, I will provide the SQL script for the user to run in the Supabase SQL Editor.
    print("Database URL and Key set. Please run the following SQL in your Supabase SQL Editor:")
    print("-" * 30)
    print("""
CREATE TABLE IF NOT EXISTS companies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    name TEXT NOT NULL,
    insta_handle TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_oauth_connected BOOLEAN DEFAULT FALSE,
    analysis_pending BOOLEAN DEFAULT FALSE,
    analysis_error TEXT
);

CREATE TABLE IF NOT EXISTS analyses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_id UUID REFERENCES companies(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    report_data JSONB NOT NULL,
    status TEXT DEFAULT 'completed'
);
    """)
    print("-" * 30)

if __name__ == "__main__":
    setup_database()
