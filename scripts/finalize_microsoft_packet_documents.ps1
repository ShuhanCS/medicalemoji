param(
    [string]$DocumentDirectory = "../output/doc",
    [string]$PdfDirectory = "../output/pdf"
)

$ErrorActionPreference = "Stop"
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$documentPath = [IO.Path]::GetFullPath((Join-Path $scriptDirectory $DocumentDirectory))
$pdfPath = [IO.Path]::GetFullPath((Join-Path $scriptDirectory $PdfDirectory))
$files = Get-ChildItem -LiteralPath $documentPath -Filter "2026-07-12-microsoft-medical-emoji-*.docx"

if (-not $files) {
    throw "No Microsoft packet DOCX files found under $documentPath"
}

New-Item -ItemType Directory -Path $pdfPath -Force | Out-Null
$word = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    foreach ($file in $files) {
        $document = $null
        try {
            $document = $word.Documents.Open($file.FullName, $false, $false)
            $document.Save()
            $destination = Join-Path $pdfPath ($file.BaseName + ".pdf")
            $document.ExportAsFixedFormat(
                $destination,
                17,
                $false,
                0,
                0,
                1,
                1,
                0,
                $true,
                $true,
                1,
                $true,
                $true,
                $false
            )
            Write-Output $file.FullName
            Write-Output $destination
        } finally {
            if ($document) {
                $document.Close($false)
                [Runtime.InteropServices.Marshal]::ReleaseComObject($document) | Out-Null
            }
        }
    }
} finally {
    if ($word) {
        $word.Quit()
        [Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    }
}
