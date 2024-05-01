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
<td><b>2.2</b></td>
</tr>
<tr>
<td><b>Created</b></td>
<td><b>4 December 2020</b></td>
</tr>
<tr>
<td><b>Last Modified</b></td>
<td><b>30 April 2024</b></td>
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

### C0033 Snippet
<details>
<summary> Operating System::Console </summary>
SHA256: 905b9db8cf5a3001318b28ee5dc674f8f65ca1e4306aab9e331b3bba24e7b8a8
Location: 0x41B4CD
<pre>
lea     eax, [esp + 0x50]       ; load an address into eax
push    eax     ; where to store number of characters read
push    ecx     ; coordinates of console cell on screen where reading text should begin
push    ecx     ; number of screen buffer character cells to read
lea     edx, [esp + 0x2cc]      ; load address into edx
push    edx     ; address of buffer into which characters should be read
push    ecx     ; handle to the console read buffer
mov     dword ptr [esp + 0x68], ecx
call    KERNEL32.DLL::ReadConsoleOutputCharacterA       ; call function to read characters from the console
</pre>
</details>
