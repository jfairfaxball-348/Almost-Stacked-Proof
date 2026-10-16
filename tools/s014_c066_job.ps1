param([string]$Graph,[int]$Mass)
$ErrorActionPreference = 'Stop'
$layerBase = Join-Path $PWD 'evidence/S014/fano_layers'
[void][System.Reflection.Assembly]::LoadFrom((Join-Path $layerBase 'producer.dll'))
[GraphLayers66]::Run($Graph,$Mass,$layerBase)
