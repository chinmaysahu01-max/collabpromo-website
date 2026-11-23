"""Build universal standalone bundle for file:// and http:// compatibility."""
import os
import re

base_dir = r"C:\Users\Chinmay sahu\.gemini\antigravity\scratch\collabpromo-website"
data_path = os.path.join(base_dir, "js", "data.js")
store_path = os.path.join(base_dir, "js", "store.js")
app_path = os.path.join(base_dir, "js", "app.js")
bundle_path = os.path.join(base_dir, "js", "bundle.js")

with open(data_path, "r", encoding="utf-8") as f:
    data_content = f.read()
with open(store_path, "r", encoding="utf-8") as f:
    store_content = f.read()
with open(app_path, "r", encoding="utf-8") as f:
    app_content = f.read()

# Replace exports in data.js
data_clean = re.sub(r"\bexport\s+const\s+", "const ", data_content)

# Remove imports in store.js
store_clean = re.sub(r'import\s+[^;]+;\s*', '', store_content)
store_clean = re.sub(r"\bexport\s+const\s+store\b", "const store", store_clean)

# Remove imports in app.js
app_clean = re.sub(r'import\s+[^;]+;\s*', '', app_content)

bundle_text = f"""// CollabPromo.com - Universal Standalone Bundle
// Compatible with both direct file:// opening and HTTP servers.

(function() {{
  "use strict";

  // === 1. CONFIGURATION & DEMO DATA ===
{data_clean}

  // === 2. PERSISTENCE & DATA STORE ===
{store_clean}

  // === 3. APP CONTROLLER & VIEWS ===
{app_clean}

  // Expose store globally for external scripts or debugging
  window.CollabPromoStore = store;
}})();
"""

with open(bundle_path, "w", encoding="utf-8") as f:
    f.write(bundle_text)

print(f"Generated bundle.js successfully ({len(bundle_text)} bytes).")
