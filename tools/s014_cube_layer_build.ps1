$ErrorActionPreference = 'Stop'
Add-Type -Path (Join-Path $PWD 'tools/s014_cube_layer.cs') -OutputAssembly (Join-Path $PWD 'evidence/S014/cube_layers/producer.dll')
Write-Output 'Untrusted orbit-layer producer library compiled; mathematical controls pending.'
