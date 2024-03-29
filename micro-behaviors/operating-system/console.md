<table>
<tr>
<td><b>ID</b></td>
<td><b>C0033</b></td>
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


# Console

Malware modifies the console. 

## Detection

|Tool: capa|Mapping|APIs|
|---|---|---|
|[set console window title](https://github.com/mandiant/capa-rules/blob/master/host-interaction/gui/console/set-console-window-title.yml)|Console (C0033)|kernel32.SetConsoleTitle|
|[manipulate console buffer](https://github.com/mandiant/capa-rules/blob/master/host-interaction/console/manipulate-console-buffer.yml)|Console (C0033)|kernel32.SetConsoleCursorPosition, kernel32.ReadConsoleOutputCharacter, kernel32.WriteConsoleOutputCharacter, kernel32.WriteConsoleOutput, kernel32.WriteConsoleInput, kernel32.GetStdHandle, System.Console::Write, System.Console::WriteLine|

|Tool: CAPE|Mapping|APIs|
|---|---|---|
|[bcdedit_command](https://github.com/CAPESandbox/community/tree/master/modules/signatures/bcdedit_command.py)|Console (C0033)|ShellExecuteExW, NtCreateUserProcess, CreateProcessInternalW|
