param([int]$Dimension,[int]$Mass)
$ErrorActionPreference = 'Stop'
$layerBase = Join-Path $PWD 'evidence/S014/cube_layers'
[void][System.Reflection.Assembly]::LoadFrom((Join-Path $layerBase 'producer.dll'))
[CubeLayers]::Run($Dimension,$Mass,$layerBase)
