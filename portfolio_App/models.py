from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    apelido = models.CharField('Apelido', max_length=50)
    dataNascimento = models.DateField('Data de Nascimento')
    apresentacao = models.TextField('Apresentação')
    servico = models.CharField('Meus serviços', max_length=50)
    conhecimento = models.CharField('Conhecimentos', max_length=50)
    profissao = models.CharField('Profissão', max_length=30)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=30)
    facebook = models.URLField('Facebook')
    instagran = models.URLField('Instagran')
    linkdin = models.URLField('Linkdin')
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    historico = models.ForeignKey('Historico', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    portifolio = models.ForeignKey('Portifolio', on_delete=models.CASCADE)
    curso_tec = models.ForeignKey('Curso_tec', on_delete=models.CASCADE)
    estagio = models.ForeignKey('Estagio', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Historico(models.Model):
    empresa = models.CharField('Nome', max_length=50)
    cargo = models.CharField('Cargo', max_length=50)
    anoInicial = models.IntegerField('Ano inicial')
    anoFim = models.IntegerField('Ano Final')
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.empresa

class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=50)
    numero = models.IntegerField('Número')
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50)

    def __str__(self):
        return self.rua

class Curso(models.Model):
    instituicao = models.CharField('Instituição', max_length=50)
    anoInicial = models.IntegerField('Ano inicial')
    anoFim = models.IntegerField('Ano Final')
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.instituicao

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=80)
    data = models.DateField('Data de publicação')
    texto = models.TextField('Texto')
    imagens = models.ImageField('Imagem')

    def __str__(self):
        return self.titulo

class Portifolio(models.Model):
    titulo = models.CharField('Titulo', max_length=80)
    texto = models.TextField('Texto')
    imagens = models.ImageField('Imagem')

    def __str__(self):
        return self.titulo

class Visitante(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    data = models.CharField('Data', max_length=50)

    def __str__(self):
        return self.nome

class Curso_tec(models.Model):
    instituicao = models.CharField('Instituição', max_length=50)
    ano = models.CharField('Ano', max_length=10)
    carga_horaria = models.CharField('Carga horaria', max_length=20)
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.instituicao

class Estagio(models.Model):
    empresa = models.CharField('Nome', max_length=50)
    cargo = models.CharField('Cargo', max_length=50)
    anoInicial = models.IntegerField('Ano inicial')
    anoFim = models.IntegerField('Ano Final')
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.empresa