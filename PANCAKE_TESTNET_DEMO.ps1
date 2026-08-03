# =========================================================
#  Positive Change Institute™
#  Pancake Honeypot Demo & AI Sniper Bot
#  Version: Testnet 1.0
#  All Rights Reserved © 2025
# =========================================================
#  Credits: CEO Christopher S Rowland Sr.
#  Dedicated to: Ashton J Rowland, my son
#  Special Thanks: GeekStinkbreath, OnThruTheStorm
# =========================================================
#  Voice-Friendly Narration: Step-by-step guidance included
# =========================================================

$ErrorActionPreference = "Stop"

Write-Host "=== STARTING FULL TESTNET DEMO WITH WATCHDOG ==="

$DeployDir = Get-Location
$DemoDir = Join-Path $DeployDir "..\pancake-honeypot-demo"
$DeployOutputFile = Join-Path $DeployDir "deployed_token.txt"
$DemoEnv = Join-Path $DemoDir ".env"

Write-Host "Step 0: Ensure your .env contains testnet RPC, private key, router, WBNB, and other necessary variables."

# Step 1: Deploy test token + add liquidity
Write-Host "`nStep 1: Deploying test token to testnet..."
npm run deploy
Write-Host "Deployment finished."

# Step 2: Read deployed token address
if (-Not (Test-Path $DeployOutputFile)) { 
    Write-Error "Error: deployed_token.txt not found. Exiting script." 
    exit 1 
}
$TokenAddr = (Get-Content $DeployOutputFile).Trim()
Write-Host "Step 2: Deployed token address = $TokenAddr"

# Step 3: Update demo container environment
Write-Host "`nStep 3: Updating DEMO_TARGET_TOKEN in demo container .env file..."
$content = Get-Content $DemoEnv
if ($content -match "DEMO_TARGET_TOKEN=") {
    $content = $content -replace "DEMO_TARGET_TOKEN=.*", "DEMO_TARGET_TOKEN=$TokenAddr"
} else {
    $content += "`nDEMO_TARGET_TOKEN=$TokenAddr`n"
}
Set-Content $DemoEnv $content
Write-Host "DEMO_TARGET_TOKEN updated."

# Step 4: Build Docker containers
Write-Host "`nStep 4: Building Docker containers (listener + demo)..."
Set-Location $DemoDir
docker compose build
Write-Host "Docker containers built successfully."

# Step 5: Run demo container once
Write-Host "`nStep 5: Running demo container for test trade..."
docker compose up -d pancake-demo
Write-Host "Demo container started. It will run once and stop automatically after execution."

# Step 6: Start listener watchdog
Write-Host "`nStep 6: Starting listener watchdog..."
Write-Host "The listener container will run continuously and restart automatically if it stops."

while ($true) {
    $listenerStatus = docker inspect -f '{{.State.Running}}' pancake-listener 2>$null
    if ($listenerStatus -ne "true") {
        Write-Host "$(Get-Date -Format u): Listener is stopped or crashed. Restarting..."
        docker compose up -d pancake-listener
        Write-Host "$(Get-Date -Format u): Listener restarted successfully."
    }
    Start-Sleep -Seconds 5
}

# Step 7: Optional logs
Write-Host "`nOptional: To view real-time logs, open a separate terminal and run:"
Write-Host "docker compose logs -f pancake-listener"

# Step 8: Stop containers when finished
Write-Host "`nTo stop all containers safely, run in a separate terminal:"
Write-Host "docker compose down"

# End of Script
Write-Host "`n=== FULL TESTNET DEMO AUTOMATION COMPLETE ==="
Write-Host "Remember: Testnet only. Do not use mainnet private keys. LIVE_BUY should remain disabled until fully tested."
Write-Host "Credits: CEO Christopher S Rowland Sr., dedicated to Ashton J Rowland, with special thanks to GeekStinkbreath and OnThruTheStorm."
