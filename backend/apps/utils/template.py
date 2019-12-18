from django import template


class EvaluateNode(template.Node):
    html_codes = (
        ('"', '&quot;'),
    )

    def __init__(self, variable):
        self.variable = template.Variable(variable)

    def unescape_symbols(self, s):
        for code in self.html_codes:
            s = s.replace(code[1], code[0])
        return s

    def render(self, context):
        content = self.unescape_symbols(
            self.variable.resolve(context)
        )
        t = template.Template(content)
        return t.render(context)
