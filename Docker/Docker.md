# Docker tutorial
## Instalação
### Passo 01: Atualizar os pacotes do sistema
```
sudo apt update && sudo apt upgrade -y
```

### Passo 2: Instalar dependências
```
sudo apt install -y ca-certificates curl gnupg
```

### Passo 3: Remover pacotes não mais necessários (opcional)
```
sudo apt autoremove -y
```

### Passo 4: Adicionar a chave GPG do Docker
```
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### Passo 5: Adicionar o repositório oficial do Docker
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Passo 6: Atualizar a lista de pacotes
```
sudo apt update
```

### Passo 7: Instalar o Docker Engine, CLI e Containerd
```
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Passo 8: Iniciar e habilitar o serviço do Docker
```
sudo systemctl enable --now docker
```

### Verificar a versão do Docker para garantir que ele foi instalado corretamente
```
docker --version
```

## ---
## Como baixar imagens
Acesse: https://hub.docker.com/

```
docker pull [imagem]
```

Exemplo: Executar um container interativo com Python.
```
docker pull python
```
```
docker run -it --rm python
```
-> Visualizar as imagens:
```
docker images
```
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
python       latest    385ccb8304f6   2 days ago     56MB





## ---
## Perguntas
### Devo instalar o Docker em um ambiente versionado pelo conda por exemplo?
Não nesse caso. O Conda é um gerenciador de pacotes e ambientes que funciona bem para instalar e isolar pacotes de Python e algumas dependências do sistema. 
No entanto, o Docker não é um pacote Python, mas sim um serviço que roda no nível do sistema operacional.


## ---
## Projetos
### Análises de metagenômica bacteriana (Python + MySQL)
### Passo 1: Criar a Estrutura do Projeto
Criar arquivos essenciais para o projeto:
```
touch Dockerfile docker-compose.yml app.py requirements.txt
```
Dockerfile → Define a imagem do container Python.

docker-compose.yml → Gerencia os containers (Python + MySQL).

app.py → Código principal da aplicação Python.

requirements.txt → Lista as bibliotecas Python necessárias.





