Param(
    [string]$JsonPath = "01_processed_json\batch_01_IDs_001-050_v4.json"
)

if (-not (Test-Path -LiteralPath $JsonPath)) {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $workspaceDir = Split-Path -Parent $scriptDir
    $candidate = Join-Path $workspaceDir $JsonPath
    if (Test-Path -LiteralPath $candidate) {
        $JsonPath = $candidate
    } else {
        Write-Error "JSON file not found at: $JsonPath"
        exit 1
    }
}

$raw = Get-Content -Raw -LiteralPath $JsonPath
$data = $raw | ConvertFrom-Json
$items = @($data)

$totalSentences = 0
$totalWords = 0
$over4 = @()

for ($i = 0; $i -lt $items.Count; $i++) {
    $text = $items[$i].refactored_text
    if (-not $text) { continue }

    $sentences = [regex]::Split($text.Trim(), '(?<=[\.!?])\s+')
    $sentences = $sentences | Where-Object { $_.Trim().Length -gt 0 }
    $sentenceCount = $sentences.Count
    $totalSentences += $sentenceCount
    if ($sentenceCount -gt 4) { $over4 += $items[$i].source_id }

    $normalized = [regex]::Replace($text, '[^\p{L}\p{N}\s]', ' ')
    $words = ($normalized -split '\s+') | Where-Object { $_ -ne '' }
    $wordCount = $words.Count
    $totalWords += $wordCount
}

$avgSentences = [math]::Round($totalSentences / $items.Count, 3)
$avgWords = [math]::Round($totalWords / $items.Count, 1)

Write-Output ("AVG_SENTENCES=" + $avgSentences)
Write-Output ("AVG_WORDS=" + $avgWords)
Write-Output ("OVER4_IDS=" + ($over4 -join ','))
Write-Output ("SAMPLE_12=" + $items[11].refactored_text)
Write-Output ("SAMPLE_33=" + $items[32].refactored_text)
Write-Output ("SAMPLE_48=" + $items[47].refactored_text)


