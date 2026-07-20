import ast
import operator


class CalculatorService:

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.FloorDiv: operator.floordiv,
        ast.USub: operator.neg,
    }

    @classmethod
    def evaluate(cls, expression):
        try:
            node = ast.parse(expression, mode="eval").body
            result = cls._evaluate(node)
            return f"The answer is {result}."
        except Exception:
            return None

    @classmethod
    def _evaluate(cls, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            left = cls._evaluate(node.left)
            right = cls._evaluate(node.right)

            return cls.OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp):
            operand = cls._evaluate(node.operand)
            return cls.OPERATORS[type(node.op)](operand)

        raise ValueError("Invalid expression")