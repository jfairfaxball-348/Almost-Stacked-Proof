# S018: enforce the preregistered 12 GiB cap: kill any lean/checker process whose private memory exceeds 12288 MB; log kills.
param([string]$Log, [string]$Stop)
while (-not (Test-Path $Stop)) {
  Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.ProcessName -match '^(lean|lake|leanchecker.*|leanexport|nanoda_bin|con-ron|con-leche|lean4lean)$' -and $_.PrivateMemorySize64 -gt 12288MB } | ForEach-Object {
    "$((Get-Date).ToUniversalTime().ToString('s')) KILL_CAP $($_.ProcessName) pid=$($_.Id) mb=$([math]::Round($_.PrivateMemorySize64/1MB))" | Out-File -Append -Encoding ascii $Log
    Stop-Process -Id $_.Id -Force
  }
  Start-Sleep -Seconds 2
}
