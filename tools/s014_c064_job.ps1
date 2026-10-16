param([int]$Dimension,[int]$Mass)
$ErrorActionPreference = 'Stop'
$layerBase = Join-Path $PWD 'evidence/S014/cube_layers_full'
[void][System.Reflection.Assembly]::LoadFrom((Join-Path $layerBase 'producer.dll'))
[CubeLayers64]::Run($Dimension,$Mass,$layerBase)
