$ErrorActionPreference = 'Stop'
Add-Type -Path (Join-Path $PWD 'tools/s014_c064_layer.cs') -OutputAssembly (Join-Path $PWD 'evidence/S014/cube_layers_full/producer.dll')
Write-Output 'Untrusted orbit-layer producer library compiled; mathematical controls pending.'
