import ast
import operator as op

operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.USub: op.neg,
    ast.UAdd: op.pos, ast.Mod: op.mod
}

def eval_expr(node):
    if isinstance(node, ast.Num): return node.n
    if isinstance(node, ast.Constant): return node.value
    if isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_expr(node.left), eval_expr(node.right))
    if isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_expr(node.operand))
    raise TypeError("Unsupported operation")

def safe_calculate(expression):
    try:
        expr_ast = ast.parse(expression, mode='eval').body
        result = eval_expr(expr_ast)
        return f"🧮 Result: {result}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
