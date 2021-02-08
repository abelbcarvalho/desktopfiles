from abc import ABCMeta


class AbsDesk(metaclass=ABCMeta):
    """Classe Abstrata com os parametros básicos
    para a criação de arquivos .desktop para linux.
    abelbcarvalho
    """

    def __init__(self):
        """Cria os atributos de classe.
        """
        self._struct = {
            'title': '[Desktop Entry]',
            'name': 'Name={}',
            'comment': 'Comment={}',
            'generic': 'GenericName={}',
            'exec': 'Exec={}',
            'type': 'Type={}',
            'icon': 'Icon={}',
            'terminal': 'Terminal={}',
            'categories': 'Categories={}'
        }

    # getter

    @property
    def struct(self) -> dict:
        """Estrutura básica para a
        criação de um arquivo
        executável linux, que possui
        por extensão: .desktop

        Returns:
            dict: todos os parametros
            para a criação de um arquivo
            .desktop
        """
        return self._struct
