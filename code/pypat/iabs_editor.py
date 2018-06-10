class EditorNotFound(BaseException):
    pass


class Key(object):
    """按键定义
    name: 键名
    effect: 作用
    """

    def __init__(self, name, effect):
        self._name = name
        self._effect = effect

    def name(self):
        return self._name

    def effect(self):
        return self._effect


class VimKey(Key):
    def __init__(self, name, effect):
        print('Vim Keys')
        super().__init__(name, effect)


class EmacsKey(Key):
    def __init__(self, name, effect):
        print('Emacs Keys')
        super().__init__(name, effect)


class Code(object):
    """代码比例
    i.e. c %50, elisp: 79%...
    """

    def rate(self):
        raise NotImplementedError


class VimCode(Code):
    def rate(self):
        return 'c: 52%, VimScript: 48%'


class EmacsCode(Code):
    def rate(self):
        return 'c: 21%, eLisp: 79%'


class EditorFactory(object):
    def create_key(self, name, effect):
        raise NotImplementedError

    def create_code(self):
        raise NotImplementedError


class VimEditor(EditorFactory):
    def create_key(self, name, effect):
        return VimKey(name, effect)

    def create_code(self):
        return VimCode()


class EmacsEditor(EditorFactory):
    def create_key(self, name, effect):
        return EmacsKey(name, effect)

    def create_code(self):
        return EmacsCode()


def test_editor(n):
    # n = 'Vim'
    if n == 'Vim':
        editor = VimEditor()
    elif n == 'Emacs':
        editor = EmacsEditor()
    else:
        raise EditorNotFound

    ka = editor.create_key('a', 'append')
    code = editor.create_code()
    print(ka.name(), ka.effect())
    print(code.rate())


if __name__ == '__main__':
    n = 'Emacs'
    n = 'Vim'
    try:
        test_editor(n)
    except EditorNotFound as e:
        print('Not Supported Editor name!')
