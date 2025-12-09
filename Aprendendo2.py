'''
\r\n -> CRLF
\n -> LF
Isso significa quebra de linha
O vscode ja faz automaticamente, porém caso eu queira usa, tem que ser utilizado (end='\n')
'''
print (12, 36, sep='_', end='\n') # -> O "\n" quebra a linha. E a separação vai ser substituida por "_"
print (12, 36, sep='_')# -> O "sep=" faz a separação vai ser substituida por "_"
