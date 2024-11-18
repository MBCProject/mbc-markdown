<table>
<tr>
<td><b>ID</b></td>
<td><b>C0035</b></td>
</tr>
<tr>
<td><b>Objective(s)</b></td>
<td><b><a href="../operating-system">Operating System</a></b></td>
</tr>
<tr>
<td><b>Related ATT&CK Techniques</b></td>
<td><b>None</b></td>
</tr>
<tr>
<td><b>Version</b></td>
<td><b>2.1</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>5 December 2023</b></td>
</tr>
</table>


# Wallpaper

Malware modifies the wallpaper. 

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[change the wallpaper](https://github.com/mandiant/capa-rules/blob/master/host-interaction/gui/session/wallpaper/change-the-wallpaper.yml)|Wallpaper (C0035)|SystemParametersInfo|

|Tool: CAPE|Class|Mapping|APIs|
|---|---|---|---|
|[modify_desktop_wallpaper](https://github.com/CAPESandbox/community/blob/master/modules/signatures/windows/modifies_wallpaper.py)|ModifiesDesktopWallpaper|Wallpaper (C0035)|SystemParametersInfoA, SystemParametersInfoW|
