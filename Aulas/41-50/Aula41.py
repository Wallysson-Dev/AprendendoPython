'''
Detalhes sobre o interpretador do Python

• python modulo.py - (Executa o módulo(arquivo) digitado)
• python -u(unbuffered) - Ele não 'salva' num "buffer", um pedaço da memória
• python -m biblioteca - O python executa a biblioteca (normalmente "venv") e cria um ambiente virtual com o nome escolhido
    python -m venv nome_ambiente
    Geralmente cada projeto tem um ambiente virtual
• python -c "Algum comando" - Executa um código no terminal
    python -c "print('oi')" - Aspas duplas fora, aspa simples dentro
    Para executar masis de um código, devemos usar o ';'
        Pode ser usado no vscode, porém atrapalha a leitura, e ninguém usa
        python -c "print('oi');print(1+1)"

Modo iterativo do python, não precisa ficar escrevendo código
No modo iterativo nada fica salvo
Para identificar se está no modo iterativo, é só ver se tem '>>>'
Para sair é só escrever 'quit()' ou 'exit()'
É possivel carregar um módulo para o modo iterativo
Caso o código tenha 'while True', ele não irá parar

Para carregar o módulo, se usa
python -i.\Projetos_Próprios\QuizPrimeiraVersão\Quiz.py
O código vai ser executado
Vai abrir o iteravel

Assim no modo iteravel é possivel acessar uma variavel
>>>pontos - Irá mostrar o que tem dentro da variavel

• python --help - Mostra todas "opções" usaveis
• python -c "import this" - Mostra a The Zen of Python, escrito pelo Tim Peters
    É meio que uma "biblia" dos programadores Python

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

Tradução:

O Zen do Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aninhado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade supere a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deveria haver uma — e preferencialmente apenas uma — maneira óbvia de fazer isso.
Embora essa maneira possa não ser óbvia à primeira vista, a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca seja frequentemente melhor do que agora mesmo.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma ótima ideia — vamos usar mais deles!

Explicação:

Bonito é melhor que feio.
    Código organizado e bem escrito é mais fácil de entender.
Explícito é melhor que implícito.
    O código deve deixar claro o que está fazendo.
Simples é melhor que complexo.
    Prefira soluções simples sempre que possível.
Complexo é melhor que complicado.
    Se for complexo, que seja bem estruturado.
Plano é melhor que aninhado.
    Evite muitas camadas de if e loops.
Esparso é melhor que denso.
    Use espaços e quebras de linha para legibilidade.
Legibilidade conta.
    Código deve ser fácil de ler e entender.
Casos especiais não quebram as regras.
    Evite exceções desnecessárias.
A praticidade supera a pureza.
    Soluções práticas são melhores que perfeitas.
Erros não devem passar silenciosamente.
    Erros precisam ser tratados ou exibidos.
A menos que sejam explicitamente silenciados.
    Ignore erros apenas de forma consciente.
Diante da ambiguidade, não adivinhe.
    Seja claro e evite interpretações duplas.
Uma maneira óbvia de fazer.
    Siga o padrão da linguagem.
Pode não ser óbvia no início.
    Com prática, o jeito Python fica natural.
Agora é melhor que nunca.
    É melhor fazer do que adiar.
Mas nunca pode ser melhor que agora.
    Não tenha pressa sem entender o problema.
Difícil de explicar é má ideia.
    Código confuso costuma ser ruim.
Fácil de explicar é boa ideia.
    Código simples costuma ser melhor.
Namespaces são uma ótima ideia.
    Organize seu código em módulos.

'''