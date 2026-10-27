param(
    [Parameter(Mandatory = $false)]
    [string]$ProjectRoot = ".",
    [switch]$CheckOnly
)

$ErrorActionPreference = "Stop"
$root = Resolve-Path $ProjectRoot -ErrorAction Stop
$firebaseJson = Join-Path $root "firebase.json"

if (-not (Test-Path $firebaseJson)) {
    $defaultConfig = @{
        firestore = @{
            rules   = "firestore.rules"
            indexes = "firestore.indexes.json"
        }
        hosting   = @{
            public = "web-app"
            ignore = @("firebase.json", "**/.*", "**/node_modules/**")
        }
    } | ConvertTo-Json -Depth 4
    Set-Content -Path $firebaseJson -Value $defaultConfig -Encoding UTF8
}

$indexesJson = Join-Path $root "firestore.indexes.json"
if (-not (Test-Path $indexesJson)) {
    $defaultIndexes = @{
        indexes        = @()
        fieldOverrides = @()
    } | ConvertTo-Json -Depth 4
    Set-Content -Path $indexesJson -Value $defaultIndexes -Encoding UTF8
}

# Validate JSON syntax
$null = Get-Content $firebaseJson -Raw | ConvertFrom-Json
$null = Get-Content $indexesJson -Raw | ConvertFrom-Json

$firebaseCli = Get-Command firebase -ErrorAction SilentlyContinue
$hasFirebaseCli = $null -ne $firebaseCli

if ($CheckOnly) {
    $report = @{
        status           = "ok"
        mode             = "CheckOnly"
        firebaseJson     = $firebaseJson
        firestoreIndexes = $indexesJson
        firebaseCliFound = $hasFirebaseCli
    } | ConvertTo-Json -Compress
    Write-Output $report
    exit 0
}

if (-not $hasFirebaseCli) {
    Write-Error "Firebase CLI not installed. Run 'npm install -g firebase-tools' first."
    exit 1
}

Push-Location $root
try {
    & firebase deploy --only firestore:indexes
} finally {
    Pop-Location
}
