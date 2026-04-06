# SOP: InstaConsult AI Analysis Workflow

This directive defines the automated analysis process for Instagram accounts. 

## Rule: Browser Sharing & Stability
**CRITICAL**: Avoid opening multiple browser windows to maintain performance and prevent Instagram's bot detection.

1.  **Check Session**: Before starting any analysis, run `list_browser_pages`.
2.  **Evaluate**:
    *   If a page from `instagram.com` is found: Switch to that tab and verify if it's logged in.
    *   If no Instagram page is found but the browser is open: Open a new tab for Instagram.
    *   If no browser is open: Start a new browser session.

## Analysis Steps

### 1. Context Recognition
- Navigate to the profile home.
- Extract: Bio, Category, and Visually analyze the last 9 posts.
- Store Nicho and Model for tailored suggestions.

### 2. Metrics Extraction
- Navigate to Professional Dashboard (`/reels/` or internal insights).
- Extract 30-day stats: Alcance, Conversion Rate, Link Clicks.

### 3. Strategy Synthesis
- Compare stats with sector benchmarks.
- Evaluate the "Sales Funnel": Bio efficiency, Highlight quality, Pinned post impact.

## 4. Dashboard Integration & Security Check

The agent must act as the "Active Brain" behind the system:
1. **Monitoring**: Periodically run `python execution/check_requests.py`.
2. **Identification**: Note the `Authorized Insta` and `User`.
3. **Security Check (CRITICAL)**: 
   - Open the browser at `instagram.com` and verify the *currently logged-in username*.
   - If the active account **DOES NOT MATCH** the `Authorized Insta`, DO NOT proceed. 
   - Instead, update `companies.json` for that company by setting `analysis_error: "A conta logada no Instagram não corresponde à conta autorizada. Faça login na conta correta ou contate o administrador."`. Set `analysis_pending: false`.
4. **Reaction (If match)**: 
   - Initiate the **360º Strategic Scan** on the logged-in account.
   - Extract data, update `database/last_analysis.json` and `companies.json` (`analysis_pending: false`, `analysis_error: null`).
   - Provide the final Strategic Report to the user via an Artifact.

> [!IMPORTANT]
> The "INICIAR ANÁLISE" button in `dashboard.html` is the primary signal. Treat every click as a high-priority strategic mission.

## Output Structure
Always output an **Executive Report Artifact** as defined in the master prompt.
