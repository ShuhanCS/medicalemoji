param(
    [string]$InputDeck = "Emoji-2026-Brief-v6.pptx",
    [string]$OutputPdf = "../../../output/pdf/2026-07-12-microsoft-medical-emoji-review-deck.pdf"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$inputPath = [IO.Path]::GetFullPath((Join-Path $scriptDirectory $InputDeck))
$pdfPath = [IO.Path]::GetFullPath((Join-Path $scriptDirectory $OutputPdf))
$finalizedPath = [IO.Path]::Combine(
    [IO.Path]::GetDirectoryName($inputPath),
    [IO.Path]::GetFileNameWithoutExtension($inputPath) + ".finalized.pptx"
)

if (-not (Test-Path -LiteralPath $inputPath)) {
    throw "Input deck not found: $inputPath"
}

New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($pdfPath)) -Force | Out-Null

$powerPoint = $null
$presentation = $null
try {
    $powerPoint = New-Object -ComObject PowerPoint.Application
    $presentation = $powerPoint.Presentations.Open($inputPath, $true, $false, $false)
    $presentation.SaveAs($finalizedPath, 24)
    $presentation.SaveAs($pdfPath, 32)
} finally {
    if ($presentation) { $presentation.Close() }
    if ($powerPoint) { $powerPoint.Quit() }
    if ($presentation) { [Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null }
    if ($powerPoint) { [Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null }
}

Move-Item -LiteralPath $finalizedPath -Destination $inputPath -Force
Write-Output $inputPath
Write-Output $pdfPath
