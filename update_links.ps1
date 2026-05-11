$mapping = @{}
Get-Content -Path "D:\2ndBrain\mapping.txt" -Encoding UTF8 | ForEach-Object {
    if ($_ -match "\[\[(.+)\]\]\|\[\[(.+)\]\]") {
        $mapping[$Matches[1]] = $Matches[2]
    }
}

$files = Get-ChildItem -Path "D:\2ndBrain\wiki" -Filter "*.md"
$updatedCount = 0

foreach ($file in $files) {
    $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    $content = $encoding.GetString($bytes)
    
    $changed = $false
    foreach ($oldName in $mapping.Keys) {
        $newName = $mapping[$oldName]
        
        # Case 1: Standard link [[oldName]]
        $oldFull = "[[$oldName]]"
        $newFull = "[[$newName]]"
        if ($content.Contains($oldFull)) {
            $content = $content.Replace($oldFull, $newFull)
            $changed = $true
        }
        
        # Case 2: Aliased link [[oldName|alias]]
        $oldAlias = "[[$oldName|"
        $newAlias = "[[$newName|"
        if ($content.Contains($oldAlias)) {
            $content = $content.Replace($oldAlias, $newAlias)
            $changed = $true
        }

        # Case 3: Anchored link [[oldName#anchor]]
        $oldAnchor = "[[$oldName#"
        $newAnchor = "[[$newName#"
        if ($content.Contains($oldAnchor)) {
            $content = $content.Replace($oldAnchor, $newAnchor)
            $changed = $true
        }
    }
    
    if ($changed) {
        [System.IO.File]::WriteAllText($file.FullName, $content, $encoding)
        $updatedCount++
        Write-Output "Updated: $($file.Name)"
    }
}
Write-Output "Total updated files: $updatedCount"
