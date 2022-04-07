## Getting Started
```
    git clone https://github.com/SDMDeveloperSec/Decrypt-Password-Linux.git
```

## Prerequisites
  Sistema operacional: Linux esse script foi testado em Debian 4.19.28-2kali1 (2019-03-18) x86_64 GNU/Linux
  se o seu sistema for Windows ou Freebsd será um pouco diferente mas nada muito complexo.


```
    Debian 4.19.28-2kali1 (2019-03-18) x86_64 GNU/Linux
```

## Execution
```
    python decrypt.py
    
    
    Insira o Salt    : "your_salt"
    Insira o Hash    : "your_string_hash"
    Insira o Path    : "your_wordlist"
    
    Insira o Salt    : "$1$vaLTND2s$"
    Insira o Hash    : "$1$vaLdaasddererqS3s$EVan8F7c4IbHWRK.."
    Insira o Path    : "/usr/share/wordlists/rockyou.txt"
```

##END


```bash
# anotações

- Ignorando os últimos 3 commits para gerar 1 só.

git reset --soft HEAD~3

git rebase -- d significa que durante a reprodução o commit vai ser descartado do bloco de commit combinado final.
git rebase -- p deixa o commit como está. Ele não vai modificar a mensagem ou conteúdo do commit e ainda vai ser um commit individual no histórico de ramificações.
git rebase -- x durante a reprodução, executa um script do shell da linha de comandos em cada commit marcado. Um exemplo útil seria executar o conjunto de teste da base de código em commits específicos, o que poderia ajudar a identificar as regressões durante um rebase.

git rebase --onto <newbase> <oldbase
```
