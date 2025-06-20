# Tutorial sobre o Git e GitHub
Git é um software para gerenciamento de versão para gerenciamento de arquivos de texto no computador.

## O problema
Git e GitHub buscam resolver problemas ligados a:
- Diversas alterações em projetos
- Reversão de alterações
- Múltiplos contribuidores
- Distribuição de funções

## Instalação
```
sudo apt install git
```

***

## Conceitos
### 1. Commit (checkpoint/save)
- Cada vez que se avança, é possível salvar o progresso (criar versões - versionando).
- Dessa forma, teremos um caminho principal e posíveis caminhos secundários.
![Diagrama em branco (4)](https://github.com/user-attachments/assets/223fb24e-8347-4e04-ac88-a2639565d66a)

### 2. Untracked files
- Arquvos que ainda não foram apresentados ao Git como sendo passíveis a serem versionados.

***

## Comandos
- Tornar a pasta especial (possibilidade de versionar os arquivos dentro dela), inicializando um repositório vazio:
```
git init .
```

- Configurar o e-mail e usuário a ser utilizado:
```
git config --global user.email "email@exemplo.com"
git config --global user.name "seunome"
```

- Verificar o status do repositório:
```
git status
```

### Preparação para o commit:
- OBS. Cada commit terá um identificador único
##### Passo 1: Adicionar o arquivo:
```
git add [arquivo]
```
-> Quero voltar atrás:
```
git reset [arquivo]
```

##### Passo 2: Realiza o commit (checkpoint), juntamente a uma mensagem (descrição):
```
git commit -m "mensagem"
```
- Todos os commits ficam dentro da pasta "./git"
- Posso ver todos os checkpoints com:
```
git log
```
- Para saber o que foi alterado no arquivo:
```
git diff [arquivo]
```

##### Passo 3 (opcional): Criar uma banch (ramificação)
- Estamos fazendo tudo na branch *main*
- Podemos criar e mudar para uma nova branch:
-> Essa nova branch irá clonar os dados a partir da branch de onde você estiver.
```
git checkout -b [nome da banch]
```
- Podemos trocar para a branch que acabamos de criar:
```
git checkout [nome da banch]
```
- Podemos saber em qual branch estamos com apenas:
```
git branch
```
- Podemos deletar uma brnach criada com:
```
git branch -D [nome da banch]
```

##### Observação:
- As informações criadas nessa nova branch não se comunicam com a principal.
- Trocando para a branch *main*, podemos "trazer" as informações de uma outra branch com:
```
git merge [nome da branch]
```
-> Nada acontece com a outra branch
![Diagrama em branco (5)](https://github.com/user-attachments/assets/6f1648e6-e66e-45e2-8166-773c0cf1601f)

***

### Conflitos:
- Vamos imaginar que 2 pessoas fizeram alterações no mesmo arquivo em 2 branchs diferentes e querem importar as diferentes alterações para a branch main:
```
git merge branch01
git merge branch02 
```
-> XXX ISSO RESULTARÁ EM CONFLITO! XXX
- Dentro do arquivo modificado, estará sendo informado o conflito a ser corrigido.
- O problema não é ambos editarem o mesmo arquivo, mas sim ambos editarem a mesma *linha* do arquivo

***

### Subindo o commit para o GitHub
- Autentificação via SSH:

- Envio do Commit:
```
git push origin main
```


***

## GitFlow
- Modelo de fluxo de trabalho para o Git que ajuda a organizar as ramificações de um projeto de desenvolvimento. 
![Diagrama em branco (6)](https://github.com/user-attachments/assets/d31f62c5-58b1-46ee-a803-c16ab9a73ce0)

-> *main*: Contém o código de produção. Só recebe merges de branches estáveis e testadas.

-> *develop*: É a branch de desenvolvimento principal, onde novas funcionalidades são integradas antes de serem lançadas para produção.

-> *feature/* → Para desenvolvimento de novas funcionalidades

### Padrões de Branch:
- 

***

## GitIgnore
- Git entende os arquivos como "vazios" mas podem existir para serem clonados.



