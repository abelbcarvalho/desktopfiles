from _typeshed import OpenBinaryModeReading
from core.model.absdesk import AbsDesk


class Desktop(AbsDesk):
    """Classe modelo que recebe as informações
    necessárias para criação de arquivos .desktop.
    abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo arquivo .desktop
        """
        super().__init__()
        self._name = ''
        self._comment = ''
        self._generic_name = ''
        self._exec = ''
        self._types = ''
        self._icon = ''
        self._terminal = ''
        self._categories = ''

    # getters and setters

    @property
    def name(self) -> str:
        """Retorna o nome do .desktop.

        Returns:
            str: Nome do programa
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Insere um nome para o .desktop.

        Args:
            name (str): novo nome
        """
        self._name = name

    @property
    def comment(self) -> str:
        """Retorna a descrição do .desktop.

        Returns:
            str: descrição
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str) -> None:
        """Insere uma nova descrição ao .desktop.

        Args:
            comment (str): descrição
        """
        self._comment = comment

    @property
    def generic_name(self) -> str:
        """Retorna o nome generico da aplicação
        (opcional)

        Returns:
            str: nome generico
        """
        return self._generic_name

    @generic_name.setter
    def generic_name(self, generic_name: str) -> None:
        """Insere um nome genérico qual o .desktop
        fará parte (opcional).

        Args:
            generic_name (str): nome generico
        """
        self._generic_name = generic_name

    @property
    def exec(self) -> str:
        """Retorna o caminho para o executável.

        Returns:
            str: caminho para o executável
        """
        return self._exec

    @exec.setter
    def exec(self, exec: str) -> None:
        """Caminho e o aquivo que será escutado
        pelo .desktop.

        Args:
            exec (str): caminho para o executável
        """
        self._exec = exec

    @property
    def types(self) -> str:
        """Retorna o tipo do aplicativo.

        Returns:
            str: tipo do aplicativo
        """
        return self._types

    @types.setter
    def types(self, types: str) -> None:
        """Insere o tipo ao qual o arquivo
        .desktop representa.

        Args:
            types (str): o tipo do aplicativo
        """
        self._types = types

    @property
    def icon(self) -> str:
        """Retorna o caminho e o arquivo
        de imagem responsável por ser o
        icone do .desktop.

        Returns:
            str: arquivo de imagem do icone.
        """
        return self._icon

    @icon.setter
    def icon(self, icon: str) -> None:
        """Insere o caminho e o arquivo
        de imagem atrelado a ele.

        Args:
            icon (str): caminho para o icone de imagem.
        """
        self._icon = icon

    @property
    def terminal(self) -> str:
        """Retorna o valor já atribuido
        a terminal.

        Returns:
            str: valor de terminal
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal: bool) -> None:
        """Insere um valor booleano, qual
        será convertido em str, para determinar
        se o .desktop deverá abrir ou não uma cli.

        Args:
            terminal (bool): True ou False
        """
        terminal = terminal.__str__()
        self._terminal = terminal.lower()

    @property
    def categories(self) -> str:
        """Retorna o conjunto de categorias
        qual o arquivo .desktop faz parte.

        Returns:
            str: conjunto de categorias
        """
        return self._categories

    @categories.setter
    def categories(self, categories: str) -> None:
        """Insere um novo conjunto de categorias
        que devem ter a seguinte estrutura:
        ex1;ex2;...exn; - sempre terminar com ;

        Args:
            categories (str): conjunto de categorias
        """
        self._categories = categories
