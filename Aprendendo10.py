# Precedência dos operadores
# Essa é a famosa ordem que o computador executa

# 1- (n + n), primeiro os parentêses
# 2- **, segundo a exponenciação
# 3- *, /, //, %, todos tem a mesma preferencia, serão executados conforme aparecer primeiro
# 4- + e -, por ultimo o mais e o menos

conta_errada = 1 + 1 ** 5 + 5 # O computador irá realizar primeiro a exponenciação depois a soma, resultando em 7
conta_certa = (1 + 1) ** (5 + 5) # Assim o computador irá fazer primeiro os parentêses, e depois a exponenciação, resultando em 1024

# Os parentêses, são executados de dentro pra fora
exemplo_prts = (1 + (0.5 + 0.5)) # Assim o computador irá somar 0.5 + 0.5, e depois irá somar o resultado da primeira conta, com o número que estava fora, resultando em 2