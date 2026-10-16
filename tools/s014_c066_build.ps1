$ErrorActionPreference = 'Stop'
Add-Type -Path (Join-Path $PWD 'tools/s014_c066_layer.cs') -OutputAssembly (Join-Path $PWD 'evidence/S014/fano_layers/producer.dll')
Write-Output 'Untrusted generic graph producer compiled; controls pending.'
