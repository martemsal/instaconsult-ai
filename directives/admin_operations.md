# SOP: Admin Operations - InstaConsult AI

This directive defines the processes for managing company access within the InstaConsult AI platform.

## Goals
- Register new companies.
- Manage existing company access levels (Niche, Plan).
- Ensure data integrity in the company database.

## Layer 3 Tools
- `execution/manage_companies.py`: The primary tool for database operations.

## Procedures

### 1. Registering a New Company
When a new client hires the system:
1. Identify the **Company Name**.
2. Identify the **Niche** (Imobiliário, Saúde/Estética, Infoprodutos, Varejo/Loja).
3. Identify the **Plan** (Free, Pro, Enterprise).
4. Run: `python execution/manage_companies.py add "Name" "Niche" "Plan"`.

### 2. Listing Active Companies
To review all active accesses:
1. Run: `python execution/manage_companies.py list`.

### 3. Deleting Company Access
To revoke access:
1. Get the **Company ID** from the list.
2. Run: `python execution/manage_companies.py delete "ID"`.

## Edge Cases
- **Duplicate Names**: The system currently allows duplicates, but IDs are unique.
- **Invalid Niche**: Always ensure the niche matches the established categories for better diagnosis.
