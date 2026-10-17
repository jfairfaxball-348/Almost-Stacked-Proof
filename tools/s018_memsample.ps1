# S018: sample total private memory (MB) of lean/lake/checker processes every 8 s until the stop file exists.
param([string]$Out, [string]$Stop)
"utc,total_private_mb,max_proc_mb,max_proc_name,free_phys_mb" | Out-File -Encoding ascii $Out
while (-not (Test-Path $Stop)) {
  $p = Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.ProcessName -match '^(lean|lake|leanchecker.*|leanexport|nanoda_bin|con-ron|con-leche|lean4lean)$' }
  $tot = 0; $mx = 0; $mn = ''
  foreach ($q in $p) { $m = [math]::Round($q.PrivateMemorySize64/1MB); $tot += $m; if ($m -gt $mx) { $mx = $m; $mn = $q.ProcessName } }
  $f = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)
  "$((Get-Date).ToUniversalTime().ToString('s')),$tot,$mx,$mn,$f" | Out-File -Append -Encoding ascii $Out
  Start-Sleep -Seconds 8
}
